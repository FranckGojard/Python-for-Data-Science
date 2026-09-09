def NULL_not_found(object: any) -> int:
    type_of_things = type(object)
    if object is None :
        print (f"Nothing: {object} {type_of_things}")
    elif object != object :
        print (f"Cheese: {object} {type_of_things}")
    elif type_of_things is int :
        print (f"Zero: {object} {type_of_things}")
    elif type_of_things is str and len(object) == 0:
        print (f"Empty: {type_of_things}")
    elif type_of_things is bool :
        print (f"Fake: {object} {type_of_things}")
    else :
        print ("Type not Found")
        return 1
    return 0