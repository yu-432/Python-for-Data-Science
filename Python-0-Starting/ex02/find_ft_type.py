def all_thing_is_obj(object: any) -> int:
    type_map = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict",
    }

    object_type = type(object)

    if object_type == str:
        print(f"{object} is in the kitchen :", object_type)
    elif object_type in type_map:
        print(f"{type_map[object_type]} :", object_type)
    else:
        print("Type not found")
    return 42
