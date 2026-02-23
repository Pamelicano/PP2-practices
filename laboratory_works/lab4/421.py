import importlib

n = int(input())
for _ in range(n):
    module_path, attr = input().split()
    try:
        mod = importlib.import_module(module_path)
    except ModuleNotFoundError:
        print("MODULE_NOT_FOUND")
        continue
    
    if not hasattr(mod, attr):
        print("ATTRIBUTE_NOT_FOUND")
    else:
        value = getattr(mod, attr)
        if callable(value):
            print("CALLABLE")
        else:
            print("VALUE")