def is_palindrome(value):
    """
    Checks if a given number is a palindrome.

    Args:
        value (int or str): The number to check.

    Returns:
        bool: True if the number is a palindrome, False otherwise.
    """
    value = str(value)
    return value == value[::-1]

def find_max_palindrome():
    """
    Finds the largest palindrome that is a product of two 3-digit numbers.

    Returns:
        int: The largest palindrome found.
    """
    max_palindrome = 0
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            product = i * j
            if product <= max_palindrome:
                break
            if is_palindrome(product):
                max_palindrome = product
    return max_palindrome

def main():
    """
    Main function that finds and prints the largest palindrome product.
    """
    result = find_max_palindrome()
    print("The maximum palindrome number is", result)

if __name__ == "__main__":
    main()
