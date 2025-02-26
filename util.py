from dataclasses import dataclass, is_dataclass

def nested_dataclass(*args, **kwargs):
  def wrapper(cls):
    cls = dataclass(cls, **kwargs)
    original_init = cls.__init__
    def __init__(self, *args, **kwargs):
      empty_object = {}
      for key in cls.__annotations__.keys():
        empty_object[key] = None

      for name, value in kwargs.items():
        field_type = cls.__annotations__.get(name, None)
        if is_dataclass(field_type) and isinstance(value, dict):
          new_obj = field_type(**value)
          empty_object[name] = new_obj
        elif type(field_type) is list and is_dataclass(field_type.__args__[0]):
          new_list = []
          for item in value:
            new_list.append(field_type.__args__[0](**item))
          empty_object[name] = new_list
        else:
          empty_object[name] = value
      original_init(self, *args, **empty_object)
    cls.__init__ = __init__
    return cls
  return wrapper(args[0]) if args else wrapper
