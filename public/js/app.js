// Docomotion Assistant - front end
// Talks to the app's JSON API: GET /api/stats, POST /api/retrieve, POST /api/answer

(() => {
  const $ = (sel) => document.querySelector(sel);
  const messages = $("#messages"), form = $("#form"), input = $("#input"), send = $("#send");
  const trace = $("#trace"), sectionSelect = $("#section");
  const STEPS = ["q-embed", "q-search", "q-prompt", "q-generate"];
  let busy = false;

  const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  const renderMarkdown = (text) =>
    DOMPurify.sanitize(marked.parse(text)).replace(/<a /g, '<a target="_blank" rel="noopener" ');
  const sectionLabel = (name) => {
    if (!name) return "General";
    return name.replace(/^docomotion-for-/, "").replace(/-/g, " ").replace(/\b\w/g, (c) => c.toUpperCase());
  };

  // ---------- color mode (light / dark / auto) ----------
  const media = window.matchMedia("(prefers-color-scheme: dark)");
  const getStoredTheme = () => { try { return localStorage.getItem("theme") || "auto"; } catch (e) { return "auto"; } };
  const setStoredTheme = (t) => { try { localStorage.setItem("theme", t); } catch (e) {} };
  function applyTheme(theme) {
    const resolved = theme === "auto" ? (media.matches ? "dark" : "light") : theme;
    document.documentElement.setAttribute("data-bs-theme", resolved);
    $("#theme-icon").className = "bi " + ({ light: "bi-sun", dark: "bi-moon-stars", auto: "bi-circle-half" }[theme]);
    document.querySelectorAll("[data-theme-value]").forEach((b) =>
      b.classList.toggle("active", b.dataset.themeValue === theme));
  }
  document.querySelectorAll("[data-theme-value]").forEach((b) => b.addEventListener("click", () => {
    setStoredTheme(b.dataset.themeValue);
    applyTheme(b.dataset.themeValue);
  }));
  media.addEventListener("change", () => { if (getStoredTheme() === "auto") applyTheme("auto"); });
  applyTheme(getStoredTheme());

  // ---------- live numbers + section filter ----------
  fetch("/api/stats").then((r) => r.json()).then((s) => {
    if (s.error) throw new Error(s.error);
    document.querySelectorAll("[data-stat]").forEach((el) => {
      const v = s[el.dataset.stat];
      if (v !== undefined) el.textContent = typeof v === "number" ? v.toLocaleString() : v;
    });
    (s.sections || []).forEach((sec) => {
      const opt = document.createElement("option");
      opt.value = sec.name;
      opt.textContent = `${sectionLabel(sec.name)} (${sec.articles})`;
      sectionSelect.appendChild(opt);
    });
  }).catch((e) => {
    const box = $("#stats-error");
    box.textContent = e.message;
    box.classList.remove("d-none");
  });

  // ---------- status + pipeline steps ----------
  function setStatus(text, isBusy) {
    $("#status-text").textContent = text;
    $("#status-dot").classList.toggle("busy", isBusy);
  }
  function setStep(id, state, status = "") {
    const card = document.getElementById(id);
    card.classList.remove("active", "done");
    if (state) card.classList.add(state);
    const icon = state === "active" ? '<span class="spinner-border spinner-border-sm me-1" style="width:.8rem;height:.8rem"></span>'
               : state === "done" ? '<i class="bi bi-check-circle-fill text-success me-1"></i>' : "";
    card.querySelector(".step-status").innerHTML = icon + esc(status);
  }
  const resetSteps = () => STEPS.forEach((id) => setStep(id, null));

  // ---------- chat rendering ----------
  function addRow(kind, html) {
    const row = document.createElement("div");
    row.className = "msg-row " + kind;
    const avatar = kind === "user"
      ? '<span class="avatar avatar-user"><i class="bi bi-person"></i></span>'
      : '<span class="avatar avatar-bot"><i class="bi bi-robot"></i></span>';
    row.innerHTML = avatar + `<div class="bubble">${html}</div>`;
    messages.appendChild(row);
    messages.scrollTop = messages.scrollHeight;
    return row;
  }

  function showWelcome() {
    messages.innerHTML = "";
    messages.appendChild($("#welcome-tpl").content.cloneNode(true));
    messages.querySelectorAll(".suggestion").forEach((b) =>
      b.addEventListener("click", () => ask(b.textContent.trim())));
  }

  function addAnswer(answer, seconds, chunkCount) {
    const row = addRow("bot", renderMarkdown(answer) + `
      <div class="msg-actions">
        <span><i class="bi bi-clock"></i> ${seconds.toFixed(1)}s</span>
        <span><i class="bi bi-layers"></i> ${chunkCount} chunks</span>
        <button type="button" class="ms-auto copy-btn"><i class="bi bi-clipboard"></i> Copy</button>
      </div>`);
    const btn = row.querySelector(".copy-btn");
    btn.addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(answer);
        btn.innerHTML = '<i class="bi bi-check2"></i> Copied';
      } catch (e) {
        btn.innerHTML = '<i class="bi bi-x"></i> Copy failed';
      }
      setTimeout(() => { btn.innerHTML = '<i class="bi bi-clipboard"></i> Copy'; }, 1500);
    });
  }

  // ---------- live trace ----------
  function scoreClass(score) { return score >= 0.8 ? "score-high" : score >= 0.7 ? "score-mid" : "score-low"; }

  function renderTrace(question, section, r) {
    const items = r.chunks.map((c, i) => `
      <div class="accordion-item">
        <h3 class="accordion-header">
          <button class="accordion-button collapsed py-2 gap-3" type="button" data-bs-toggle="collapse" data-bs-target="#chunk-${i}">
            <span class="score-pill ${scoreClass(c.score)}">${c.score.toFixed(3)}</span>
            <span class="progress score-bar d-none d-sm-flex" role="progressbar" aria-label="similarity">
              <span class="progress-bar" style="width:${Math.round(c.score * 100)}%"></span></span>
            <span class="small text-truncate">${esc(c.headings)}</span>
          </button>
        </h3>
        <div id="chunk-${i}" class="accordion-collapse collapse" data-bs-parent="#chunks">
          <div class="accordion-body py-3">
            <div class="d-flex flex-wrap gap-1 mb-2">
              <span class="badge rounded-pill bg-primary-subtle text-primary-emphasis">${esc(sectionLabel(c.section))}</span>
              ${c.keywords.slice(0, 6).map((k) => `<span class="badge rounded-pill bg-body-secondary text-body-secondary fw-normal">${esc(k)}</span>`).join("")}
            </div>
            <div class="chunk-text border rounded-3 p-2 mb-2">${esc(c.text)}</div>
            <a class="small" href="${esc(c.source)}" target="_blank" rel="noopener"><i class="bi bi-box-arrow-up-right"></i> Open source page</a>
          </div>
        </div>
      </div>`).join("");

    trace.innerHTML = `
      <div class="d-flex flex-wrap align-items-center gap-2 mb-3">
        <span class="text-body-secondary small">Question</span>
        <strong>${esc(question)}</strong>
        ${section !== "all" ? `<span class="badge rounded-pill bg-primary-subtle text-primary-emphasis"><i class="bi bi-funnel"></i> ${esc(sectionLabel(section))}</span>` : ""}
      </div>
      <div class="d-flex flex-wrap gap-2 mb-3" id="trace-timings">
        <span class="chip"><i class="bi bi-search"></i> Embed + search ${r.seconds}s</span>
      </div>
      ${r.chunks.length ? `
        <p class="small text-body-secondary mb-2">Top ${r.chunks.length} chunks by similarity (0–1, higher is closer). Open one to see the exact text given to the LLM.</p>
        <div class="accordion" id="chunks">${items}</div>`
      : `<div class="alert alert-secondary small mb-0">No chunks found in this section.</div>`}`;
  }
  const addTiming = (html) => document.getElementById("trace-timings")?.insertAdjacentHTML("beforeend", `<span class="chip">${html}</span>`);

  // ---------- ask flow ----------
  async function postJSON(url, body) {
    const res = await fetch(url, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) });
    const data = await res.json().catch(() => ({ error: res.statusText || "Unexpected server response" }));
    if (!res.ok) throw new Error(data.error || res.statusText);
    return data;
  }

  async function ask(question) {
    question = question.trim();
    if (!question || busy) return;
    busy = true;
    send.disabled = true;
    messages.querySelector(".welcome")?.remove();
    addRow("user", esc(question));
    input.value = "";
    autosize();
    resetSteps();
    const section = sectionSelect.value;
    const pending = addRow("bot", '<div class="typing" aria-label="Thinking"><span></span><span></span><span></span></div>');

    try {
      setStatus("Searching the knowledge base…", true);
      setStep("q-embed", "active", "Calling Voyage AI…");
      setStep("q-search", "active", "Querying Atlas…");
      const r = await postJSON("/api/retrieve", { question, section });
      setStep("q-embed", "done", "Question embedded");
      setStep("q-search", "done", `${r.chunks.length} chunks · ${r.seconds}s`);
      renderTrace(question, section, r);

      setStatus("Writing the answer…", true);
      setStep("q-prompt", "done", `${r.chunks.length} chunks + rules`);
      setStep("q-generate", "active", "Waiting for Gemini…");
      const a = await postJSON("/api/answer", { question, chunk_ids: r.chunks.map((c) => c.id) });
      setStep("q-prompt", "done", `~${a.prompt_tokens_estimate.toLocaleString()} tokens`);
      setStep("q-generate", "done", `Answered in ${a.seconds}s`);
      addTiming(`<i class="bi bi-file-earmark-code"></i> Prompt ~${a.prompt_tokens_estimate.toLocaleString()} tokens`);
      addTiming(`<i class="bi bi-stars"></i> Generate ${a.seconds}s`);

      pending.remove();
      addAnswer(a.answer, r.seconds + a.seconds, r.chunks.length);
    } catch (err) {
      pending.remove();
      STEPS.forEach((id) => {
        if (document.getElementById(id).classList.contains("active")) setStep(id, null, "Failed");
      });
      addRow("error", '<i class="bi bi-exclamation-triangle me-1"></i>' + esc(err.message || "Could not reach the server."));
    } finally {
      busy = false;
      send.disabled = false;
      setStatus("Ready", false);
      input.focus();
    }
  }

  // ---------- composer ----------
  function autosize() {
    input.style.height = "auto";
    input.style.height = Math.min(input.scrollHeight, 140) + "px";
  }
  input.addEventListener("input", autosize);
  input.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); ask(input.value); }
  });
  form.addEventListener("submit", (e) => { e.preventDefault(); ask(input.value); });
  $("#clear").addEventListener("click", () => {
    if (busy) return;
    showWelcome();
    resetSteps();
    trace.innerHTML = `<div class="trace-empty"><i class="bi bi-chat-square-dots d-block mb-2"></i>
      Ask a question to see the chunks the search found, how similar each one is, and how long each step took.</div>`;
    input.focus();
  });

  // "Try it" buttons in the left pane's "Why RAG?" cards send their question to the chat
  document.querySelectorAll("[data-ask]").forEach((b) =>
    b.addEventListener("click", () => {
      ask(b.dataset.ask);
      if (window.matchMedia("(max-width: 991.98px)").matches) messages.scrollIntoView({ behavior: "smooth" });
    }));

  showWelcome();
  input.focus();
})();
