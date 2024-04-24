# Tattva Language Documentation

## Keywords

### 1. `akshara`
- Keyword used to define a variable or function.
- Example:
  ```tattva
  akshara hesru = 10
  akshara vayassu = 25
  akshara hesru_na_oo = 'Hello, World!'
  ```

### 2. `matte`
- Used for logical AND operation.
- Example:
```tattva
matte 5 > 3 ; True
matte 10 < 5 ; False
```
### 3. `athava`
- Used for logical OR operation.
- Example:
```tattva
athava 5 > 3 ; True
athava 10 < 5 ; False
```

### 5. `aadare`
- Used for conditional statements (equivalent to 'if' in many programming languages).
- Example:
```tattva
aadare 5 > 3 TO
  odu('5 is greater than 3')
  ```

### 6. `illadiddare`
- Used in conditional statements as 'else' (equivalent to 'else' in many programming languages).
- Example:
```tattva
aadare 5 > 10 TO
  odu('5 is greater than 10')
illadiddare
  odu('5 is not greater than 10')
  ```

### 7. `illa_andre`
- Used in conditional statements as 'else if' (equivalent to 'else if' in many programming languages).
- Example:
```tattva
aadare 5 > 10 TO
  odu('5 is greater than 10')
illa_andre 5 < 10 TO
  odu('5 is less than 10')
  ```

### 8. `aguva_varigu`
Used in loops for iterating over a range.
Example:
```tattva
aguva_varigu i mundu_varisu 1 satya_iruva_varigu 10 TO
  odu(i)
```

### 9. `odu`
Used to take input.
Example:
```tattva
akshara hesaru = odu()
```
### 10. `bari`
Used to print  output.
Example:
```tattva
bari("Hello World")
```
### 11. `kaarya`
Used to define a function
Example:
```tattva
kaarya add(x, y) 
  bari(x + y)
```