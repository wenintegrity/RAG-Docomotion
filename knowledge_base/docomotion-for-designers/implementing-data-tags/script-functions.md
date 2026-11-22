---
title: "Script functions"
source: https://www.docomotion.com/support/docomotion-for-designers/implementing-data-tags/script-functions/
section: docomotion-for-designers
last_modified: 2024-01-22T11:15:45
---

# Script functions

### Absolute

(Expression N1)

**Description:** Return the absolute value of a given number.

**Arguments:** Expression N1 is the number to be processed.

**Return:** A character string which holds a number. The function will return the absolute value of Expression N1.

**Examples:**

- `ABSOLUTE(-1000)` → Result: 1000
- `ABSOLUTE(1000.54)` → Result: 1000.54

### Append String

(Expression C1, Expression C2, Expression C3)

**Description:** Append a string to another string.

**Arguments:**

- Expression C1 is the string being appended with the string.
- Expression C2 is the string to append to.
- Expression C3 determines from which side to append the character. Valid values are: ‘R’ (Right), ‘L’ (Left). Default value is ‘L’.

**Return:** A Character string. The function will return the string after being appended with the character from the specified side.

**Examples:**

- `APPEND STRING(abcdabxyz, efgh, L)` → Result: efghabcdabxyz
- `APPEND STRING(abcdabxyz, efgh, R)` → Result: abcdabxyzefgh

### Compress Character

(Expression C1, Expression C2)

**Description:** Replace duplicate appearances of a character in a string with a single appearance.

**Arguments:**

- Expression C1 is the string being searched for the duplicated Expression C2 character.
- Expression C2 is the character being searched in Expression C1 for duplicated appearances.

**Return:** A character string. The function will return the Expression C1 after replacing the duplicated appearances of Expression C2 with a single appearance.

**Examples:**

- `COMPRESS CHARACTER(ab cdabxy z, SPACE)`  →Result: ab cdab xy z
- `COMPRESS CHARACTER(abbbcdabxybz, b)` →Result: abcdabxyzb
- `COMPRESS CHARACTER(00 1000, 0)` →Result: 010

### Integer

(Expression C1)

**Description:** Extract the integer value of a number.

**Arguments:** Expression C1 is the number to be processed.

**Return:** A character string which holds the integer value of Expression C1.

**Examples:**

- `INTEGER(9.35)` →Result: 9
- `INTEGER(9)` →Result: 9

### Mantissa

(Expression N1, Expression N2)

**Description:** Calculate the mantissa value of a number modulus by another number.

**Arguments:**

- Expression N1 is the number modulated by Expression N2.
- Expression N2 is the modulus number used with Expression N1.

**Return:** A character string which holds the mantissa value of Expression N1 modulus Expression N2.

**Examples:**

- `MANTISSA(10,3)` Result: 1
- `MANTISSA(9,3)` Result: 0
- `MANTISSA(55.45,3.27)` Result: 3.13

### Max String Length

(Expression C1, Expression N1, Expression C2)

**Description:** Set the maximum length of a string.

**Arguments:**

- Expression C1 is the string being processed according to the maximum length specified in Expression N1.
- Expression N1 is the maximum allowed length of Expression C1.
- Expression C2 determines from which side to reduce the extra characters according to the maximum length specified in Expression N1. Valid values are: ‘R’ (Right), ‘L’ (Left). Default value is ‘L’.

**Return:** A character string. The function will return Expression C1 after reducing its size to the maximum length specified in Expression N1 from the specified side.

**Examples:**

- `MAX STRING LENGTH(abcdabxyz, 4, L)` Result: abcd
- `MAX STRING LENGTH(abcdabxyz, 4, R)` Result: abxyz
- `MAX STRING LENGTH(abcdabxyz, 15, L)` Result: abcdabxyz

### Pad String

(Expression C1, Expression N1, Expression C2, Expression C3)

**Description:** Add a repeating character to a string according to the maximum desired length of the whole string.

**Arguments:**

- Expression C1 is the string being processed.
- Expression N1 is the desired new length of Expression C1 after padding it with Expression C2.
- Expression C2 is the character to pad Expression C1.
- Expression C3 determines from which side to pad the Expression C2 character. Valid values are: ‘R’ (Right), ‘L’ (Left). The default value is ‘L’.

**Return:** A character string. The function will return Expression C1 after being padded with Expression C2 character to the max length specified in Expression N1 starting from the specified side. If Expression C1 string length is equal or bigger than Expression N1, no padding will be performed.

**Examples:**

- `PAD STRING(abcdabxyz, 15, e, L)` Result: eeeeeebcdabxyz
- `PAD STRING(abcdabxyz, 13, f, R)` Result: abcdabxyzffff
- `PAD STRING(abcdabxyz, 8, g, L)` Result: abcdabxyz

### Power

(Expression N1, Expression N2)

**Description:** Calculate the mathematical power value of a number.

**Arguments:**

- Expression N1 is the number to be processed.
- Expression N2 is the power value to be used with Expression N1.

**Return:** A character string which holds the power Expression N2 of Expression N1.

**Examples:**

- `POWER(9,2)` Result: 81
- `POWER(3,3)` Result: 27

### Remove String

(Expression C1, Expression C2)

**Description:** Remove all occurrences of a given string.

**Arguments:**

- Expression C1 is the string being processed.
- Expression C2 is the string to search for in Expression C1 and remove.

**Return:** A character string. The function will return Expression C1 string after removing all occurrences of Expression C2.

**Examples:**

- `REMOVE STRING(abcdabxyz, ab)` Result: cdxyz
- `REMOVE STRING(abcdabxyz, abc)` Result: dabxyz
- `REMOVE STRING(1000, 0)` Result: 1

### Replace String

(Expression C1, Expression C2, Expression C2)

**Description:** Replace all occurrences of a given string with another string.

**Arguments:**

- Expression C1 is the string being processed.
- Expression C2 is the string to search for in Expression C1 and replace with the string specified in Expression C3.
- Expression C3 is the string to replace Expression C2 in Expression C1.

**Return:** A character string. The function will return Expression C1 string after replacing all occurrences of Expression C2 with Expression C3.

**Examples:**

- `REPLACE STRING(abcdabxyz, ab, gh)` Result: ghcdghxyz
- `REPLACE STRING(abcdabxyz, abc, gh)` Result: ghdabxyz
- `REPLACE STRING(1.1.2008, ., -)` Result: 1-1-2008

### Round

(Expression N1)

**Description:** Round the value of a floating number.

**Arguments:** Expression N1 is the number to be processed.

**Return:** Character string which holds the rounded value of Expression N1.

**Examples:**

- `ROUND(9.49)` Result: 9.00
- `ROUND(9.5)` Result: 9.00
- `ROUND(9.51)` Result: 10.00

### String Length

(Expression C1)

**Description:** Return the length of a given string.

**Arguments:** Expression C1 is the string to be processed.

**Return:** A character string. The function will return the length of Expression C1.

**Examples:**

- `STRING LENGTH(abcde)` Result: 5

### String Position

(Expression C1, Expression C2, Expression C3, Expression N1)

**Description:** Return the starting position of a string within another string.

**Arguments:**

- Expression C1 is the string in which Expression C2 should be searched for.
- Expression C2 is the string being searched in Expression C1 string.
- Expression C3 determines from which side to start the search for Expression C2. Valid values are: ‘R’ (Right), ‘L’ (Left). The default value is ‘L’.
- Expression N1 is the requested appearance number of Expression C2 in Expression C1.

**Return:** A character string. The function will return the position where the Expression C2 string starts in Expression C1. If the Expression C2 cannot be found in Expression C1, the function will return 0 (zero).

**Examples:**

- `STRING POSITION(abcdabxyz, ab, L, 1)` Result: 1
- `STRING POSITION(abcdabxyz, ab, R, 1)` Result: 4
- `STRING POSITION(abcdabxyz, ab, L, 2)` Result: 5
- `STRING POSITION(abcdabxyz, ef, L, 1)` Result: 0

### Sub String

(Expression C1, Expression N1, Expression N2, Expression C2)

**Description:** Extract a string from another string.

**Arguments:**

- Expression C1 is the string to extract from starting from the side specified in Expression C2 using the offset position specified in Expression N1 in length specified by Expression N2.
- Expression N1 is the offset position in Expression C1 to extract the desired string starting from the side specified by Expression C2.
- Expression N2 is the maximum length of the string to extract from Expression C1.
- Expression C2 determines from which side of Expression C1 to calculate the offset position specified in Expression N1. Valid values are: ‘R’ (Right), ‘L’ (Left). Default value is ‘L’.

**Return:** A character string. The function will return the string extracted from Expression C1 according to the offset position specified in Expression N1 and maximum length specified by Expression N2. If the specified maximum length is beyond the Expression C1 boundary, the extracted string length will not exceed this boundary.

**Examples:**

- `SUB STRING(abc dabx yz, 1, 5, L)` Result: abc d
- `SUB STRING(abc dabx yz, 3, 5, L)` Result: c dab
- `SUB STRING(abc dabx yz, 1, 5, R)` Result: bx yz
- `SUB STRING(abc dabx yz, 4, 2, R)` Result: bx
- `SUB STRING(abc dabx yz, 7, 9, L)` Result: bx yz

### Table Column Average

(Expression C)

**Description:** Calculate the average value of all values appearing in a table column.

**Arguments:** Expression C is the name of the table column.

**Return:** Character string which holds a number. The function will return the average value of Expression C.

**Examples:**

- `Table Average(Tag Name)` Result: Average of values

### Table Column Sum

(Expression C)

**Description:** Sum all data tag values of a specific table column.

**Arguments:** Expression C is the name of the table column.

**Return:** Character string which holds a number. The function will return the sum of the values of Expression C.

**Examples:**

- `Table Sum(Tag Name)` Result: Sum of the selected columns

### Table Row Count

(Expression C)

**Description:** Total number of table rows in the input.

**Arguments:** Expression C is the name of the table column.

**Return:** Character string which holds a number. The function will return the number of table rows of Expression C.

**Examples:**

- `Table Row Count(Tag Name)` Result: Number of rows

### Table Row Count

**Description:** Number table row according to the position number of the row in the input.

**Return:** The function returns a row value that corresponds to the row position.

### Trim Character

(Expression C1, Expression C2, Expression C3)

**Description:** Remove a repeated character from a string end(s).

**Return:** A character string. The function will return the Expression C1 string after trimming the Expression C2 repeated character at its end(s).

**Examples:**

- `TRIM(abcdefg, SPACE, B)` Result: abcdefg d
- `TRIM(00001000, 0, L)` Result: c 1000
- `TRIM(abcdefghhhhhh, h, R)` Result: bx abcdefg

### Truncate String

(Expression C1, Expression N1, Expression C2)

**Description:** Cut the length of a string by a specified number of characters.

**Arguments:**

- Expression C1 is the string being cut by Expression N1 number of characters.
- Expression N1 is the number of characters to cut from Expression C1.
- Expression C2 determines from which side of Expression
