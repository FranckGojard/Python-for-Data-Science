def all_thing_is_obj(object: any) -> int:
    type_of_thing = type(object)
    if type_of_thing == dict :
        print (f"Dict : {type_of_thing}")
    elif type_of_thing == list :
        print (f"List : {type_of_thing}")
    elif type_of_thing == tuple :
        print (f"Tuple : {type_of_thing}")
    elif type_of_thing == set :
        print (f"Set : {type_of_thing}")
    elif type_of_thing == str :
        print (f"{object} is in the kitchen : {type_of_thing}")
    else :
        print ("Type not found")
    return 42