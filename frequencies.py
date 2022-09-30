"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for i in items:
        t = str(i)
        if t not in frequencies:
            frequencies[t] = 0
        frequencies[t] += 1

    return frequencies
