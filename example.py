import argy


@argy
def add_numbers(x, y, subtract=False):
    """Adder of numbers
    Just adds two numbers, nothing really special about it

    :param x: The first number
    :type x: int
    :param y: The second number
    :type y: int
    :param subtract: Should we subtract instead?
    :type subtract: bool
    """
    if not subtract:
        return x + y
    else:
        return x - y
