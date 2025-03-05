def ft_filter(function, item):
    """
    Filtre les éléments d'une séquence en fonction d'une condition.

    La fonction prend deux arguments :
        - `function` : une fonction qui teste chaque élément. Si `None` est passé, les éléments "vrais" (non nuls) sont conservés.
        - `item` : une séquence (par exemple, une liste) d'éléments à filtrer.

    Retourne un générateur contenant les éléments qui satisfont la condition donnée par `function`.
    """
    if function:
        return (element for element in item if function(element))
    return (element for element in item if element)
