import app1
import app2
import app3

import inspect


def what_import(module):

    print(module.__name__)
    for key in module.__dict__:
        if key.startswith("__") and key.endswith("__"):
            continue
        if inspect.isclass(module.__dict__[key]):
            print("\t", key, module.__dict__[key], "isclass")
        else:
            print("\t", key, module.__dict__[key])


what_import(app2)
what_import(app3)

what_import(app1)
