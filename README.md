# Info

The program uses the "watchpoints" library to track changes of variables and raise an error if a constant changes

# Guide

First, import the class "const" from the "constants" module like so:
```py
from constants import const # Assuming main.py is in the same folder as constants.py

myconst = const(5) # Declare a constant with the "const" class
const.activate() # Call a class method "activate" to activate the program

myconst = 1 # <- This will raise a ConstChangedError

```

Notice that if you do not run the "activate" function, the program will not work!

```py
from constants import const # Assuming main.py is in the same folder as constants.py

myconst = const(5) # Declare a constant with the "const" class

myconst = 1 # <- This will not raise a ConstChangedError, since the "activate" function was not ran
```

Please do not declare constant variables after the "activate" function, since the program will not work.
Please do not run the "activate" function multiple times
