# 0x02. Minimum Operations

## Description
This project involves solving the problem of finding the minimum number of operations required to achieve a specific result. The operations are defined as follows:
1. **Copy All**
2. **Paste**

## Task
Given a number `n`, write a method that calculates the fewest number of operations needed to result in exactly `n` 'H' characters in the file.

## Example
### For `n = 9`:
The output should be `6` because the operations would be:

1. **Start with 1 'H'**
2. **Copy All** (Operation 1) → Now you have 1 'H'.
3. **Paste** (Operation 2) → 1 'H' becomes 2 'H's.
4. **Paste** (Operation 3) → 2 'H's become 3 'H's.
5. **Copy All** (Operation 4) → Now you have 3 'H's.
6. **Paste** (Operation 5) → 3 'H's become 6 'H's.
7. **Paste** (Operation 6) → 6 'H's become 9 'H's.

Thus, it takes **6 operations** to reach exactly 9 characters in total.

## Usage
To use the function, call it with the desired number `n`:
```python
def minOperations(n):
    operation = 0
    i = 2
    while n > 1:
        if n % i == 0:
            operation += i
            n //= i
        else:
            i += 1
    print(operation)
    return operation

## Author
- Joe404
