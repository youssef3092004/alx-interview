# Making Change

This project involves creating a function to determine the minimum number of coins needed to make a given amount of change.

## Requirements

- Python 3.x
- No external libraries

## Function Prototype

```python
def make_change(coins, total):
    """
    Determine the minimum number of coins needed to make change.

    Args:
    coins (list): A list of the values of the coins available.
    total (int): The total amount of change needed.

    Returns:
    int: The minimum number of coins needed to make the change, or -1 if it is not possible.
    """
```

## Example

```python
print(make_change([1, 2, 5], 11))  # Output: 3 (5 + 5 + 1)
print(make_change([2], 3))         # Output: -1 (not possible)
```

## Usage

1. Clone the repository.
2. Navigate to the project directory.
3. Run the function with your desired input.

## License

This project is licensed under the MIT License.
