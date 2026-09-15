def ft_filter(function, iterable):
    """Return an iterator with the elements accepted by function."""
    if function is None:
        result = [element for element in iterable if element]
    else:
        result = [element for element in iterable if function(element)]
    return iter(result)