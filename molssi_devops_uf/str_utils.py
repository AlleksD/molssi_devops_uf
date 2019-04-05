"""
str_utils.py
This is demo project for UF MolSSI workshop

String utilities
"""

def title_case(inp_str):
    """
    Transforms the input string to start each word from capital letter
    Parameters
    ----------
    inp : string
        string to be changed
		
	Returns
    -------
	result : string
		a string were each word starts from the capital letter
    """
    if isinstance(inp_str, str):
        result = ''
        if len(inp_str) > 0:
            for t in inp_str.split():
                result += t[0].upper() + t[1:].lower() + ' '
            result = result[:-1]
        return result
    else:
        raise TypeError('Invalid formatting. The input should be a string')


