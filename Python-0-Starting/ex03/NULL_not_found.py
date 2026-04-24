def NULL_not_found(object: any) -> int:
    type_of = type(object)
    if object is None:
        print(f"Nothing: None {type_of}")
    elif type_of == float and object != object:
        print(f"Cheese: nan {type_of}")
    elif object == 0 and type_of == int:
        print(f"Zero: 0 {type_of}")
    elif object == '' and type_of == str:
        print(f"Empty: {type_of}")
    elif object is False and type_of == bool:
        print(f"Fake: False {type_of}")
    else:
        print("Type not Found")
        return 1
    return 0
