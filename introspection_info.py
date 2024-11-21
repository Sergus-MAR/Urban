from inspect import getmodule


class AnyClass:
    def __init__(self):
        self.numbers = 100


any_obj = AnyClass()


def introspection_info(obj):
    list_commands = [type, id, vars, dir, getmodule]
    list_name = ['type', 'id', 'attributes', 'methods', 'module']
    resault_dict = {}
    for key, val in (dict(zip(list_name, list_commands))).items():
        resault_dict[key] = val(obj)
    return resault_dict


number_info = introspection_info(any_obj)
print(number_info) 