import random

def adding(a, b):
    """
    Args:
        a: number
        b: number
    Returns:
        Prints the addition result
    """
    result = a + b
    print("Addition result:", result)

def randomizer():
    """
    Returns:
        A random number between 10 and 200
    """
    result = random.randint(10, 200)
    return result

def reducing(a, b):
    """
    Args:
        a: number
        b: number
    Returns:
        Prints the subtraction result
    """
    result = a - b
    print("Subtraction result:", result)

# Example usage:
adding(5, 3)        # Should print: Addition result: 8
print(randomizer()) # Will print a random number between 10 and 200
reducing(10, 4)     # Should print: Subtraction result: 6