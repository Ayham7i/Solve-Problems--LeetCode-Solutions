# By Ayham Al-Akhali


# 12. Integer to Roman

**Medium**

---

Seven different symbols represent Roman numerals with the following values:

| Symbol | Value |
| ------ | ----- |
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Roman numerals are formed by appending the conversion of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

- If the value does not start with 4 or 9, select the symbol of the decimal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
- If the value starts with 4 or 9, use the subtraction form separating one symbol subtracted from the following symbol. For example, 4 is (IV) less than (V) (5) and 9 is (IX) less than (X) (10). Only the following subtraction forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD), and 900 (CM).
- Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 4. You cannot append 5 (V) or 50 (L) or 500 (D) multiple times. If you need to append a symbol 4 times use the subtraction form.

Given an integer, convert it to a Roman numeral.

---

### Example 1:

**Input**: num = 3549  
**Output**: "MMMDXLIX"  

**Explanation**:  
3000 = 1000 (M) + 1000 (M) + 100
