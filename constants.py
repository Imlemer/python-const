from watchpoints import watch
import inspect

class ConstChangedError(BaseException): pass

def raise_const_changed_error(*a):

    raise ConstChangedError('Attempt to change a constant variable')

watch.config(callback = raise_const_changed_error)

class const:

    def __init__(self, value):

        self.value = value

    def activate():

        file_globals = inspect.currentframe().f_back.f_globals

        constants = {x: y for x, y in file_globals.items() if type(y) == const}

        for i in constants.keys():

            watch(file_globals[i])