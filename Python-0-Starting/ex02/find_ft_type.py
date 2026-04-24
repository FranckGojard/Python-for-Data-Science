def all_thing_is_obj(object: any) -> int:
    type_of_object = type(object)
    if type_of_object == list:
        print("List :", list)
    elif type_of_object == tuple:
        print("Tuple :", tuple)
    elif type_of_object == set:
        print("Set :", set)
    elif type_of_object == dict:
        print("Dict :", dict)
    elif type_of_object == str:
        print(f"{object} is in the kitchen :", str)
    else:
        print("Type not found")
    return (42)
