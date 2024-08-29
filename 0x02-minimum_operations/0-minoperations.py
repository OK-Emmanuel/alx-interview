#!/usr/bin/python3
"""The minimum operations coding challenge.
"""


def minOperations(n: int) -> int:
    """Computes the fewest number of operations needed to result
    in exactly n H characters.
    """
    if not isinstance(n, int):
        return 0

    operations = 0
    clipboard = 0
    characters_created = 1

    while characters_created < n:
        if clipboard == 0:
            # Initial copy and paste
            clipboard = characters_created
            characters_created += clipboard
            operations += 2
        elif n - characters_created > 0 and (n - characters_created) % characters_created == 0:
            # Copy all and paste
            clipboard = characters_created
            characters_created += clipboard
            operations += 2
        elif clipboard > 0:
            # Paste
            characters_created += clipboard
            operations += 1

    return operations
