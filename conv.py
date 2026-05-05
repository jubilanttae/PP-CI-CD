"""Converting dec to bin"""


def convert(a: int) -> int:
    """Convert decimal to binary.

    Args: a (int): The decimal number to convert.

    Returns: int: The binary representation of the decimal number."""
    return int(bin(a)[2:])
