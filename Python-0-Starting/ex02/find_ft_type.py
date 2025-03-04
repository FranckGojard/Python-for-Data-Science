def all_thing_is_obj(object: any) -> int:
    typeObject = type(object)

    if typeObject == list :
        print(f"List : {typeObject}")
    if typeObject == tuple :
        print(f"Tuple : {typeObject}")
    if typeObject == set :
        print(f"Set : {typeObject}")
    if typeObject == dict :
        print(f"Dict : {typeObject}")
    if typeObject == str :
        print(f"{object} is in th kitchen : {typeObject}")
    if typeObject == int :
        print("Type not found")
    return 42