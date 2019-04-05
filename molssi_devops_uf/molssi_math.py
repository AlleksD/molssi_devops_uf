"""
molssi_math.py
This is demo project for UF MolSSI workshop

Library of math utilities
"""

def my_mean(inp):
    """
    Calculate average of numerical values in the list
    Parameters
    ----------
    inp : list
        input
    """
    result = 0
    count = 0
    for t in inp:
        if isinstance(t, int) or isinstance(t, float):
            result += float(t)
            count += 1
    return result / float(count)

def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
