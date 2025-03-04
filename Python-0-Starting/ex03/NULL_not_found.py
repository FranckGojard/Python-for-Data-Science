def NULL_not_found(object: any) -> int:
    objectType = type(object)
    if object is None :
        print(f"Nothing: {object} {objectType}")
    elif objectType == float :
        print(f"Cheese: {object} {objectType}")
    elif object == 0 and objectType == int:
        print(f"Zero: {object} {objectType}")
    elif object == '' :
        print(f"Empty: {objectType}")
    elif object is False :
        print(f"Fake: {object} {objectType}")
    else :
        print("Type not Found")
        return 1
    return 0