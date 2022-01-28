from tabnanny import verbose


def suma(x, y):
    """
    Test the suma function
    >>> suma(0, 1)
    1
    >>> suma(1, 1)
    2
    >>> suma("a", "b")
    'ab'
    >>> suma(1.0, "b")
    Traceback (most recent call last):
    ...
    TypeError: unsupported operand type(s) for +: 'float' and 'str'
    >>> suma("a", "b")
    'ab'
    """
    return x + y

def palindrome(cadena: str):
    """
    Testing palindrome function
    >>> palindrome ("oro")
    True
    >>> palindrome("laptop")
    False
    >>> palindrome("")
    True
    >>> palindrome("1")
    True
    >>> palindrome("Ana")
    True
    >>> palindrome("La ruta natural")
    True
    >>> palindrome("Aná")
    True
    """
    return cadena.lower().replace(" ", "") == cadena[::-1].lower().replace(" ", "")

if __name__ == "__main__":
    import doctest
    doctest.testmod(name='palindrome', verbose=True)
