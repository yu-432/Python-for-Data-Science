def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: {object} {type(object)}")
        return 0
    elif type(object) is float and object != object:
        print(f"Garlic: {object} {type(object)}")
        return 0
    elif type(object) is bool and object is False:
        print(f"Fake: {object} {type(object)}")
        return 0
    elif type(object) is int and object == 0:
        print(f"Zero: {object} {type(object)}")
        return 0
    elif type(object) is str and object == "":
        print(f"Empty: {type(object)}")
        return 0
    else:
        print("Type not Found")
        return 1
