# Python in a terminal (IPython)

You can complete the tutorial above in a terminal as well, using the ipython command line interface. To get started type the following in a terminal window

    ipython --pylab
    
This starts ipython with some common libraries autoloaded, including:

```python
import numpy as np		# basic numerical analysis
import matplotlib.pyplot as plt	# plotting
```

The `--pylab` flag should set things up so that plots will just automatically open when you make them, but if that doesn't happen, try adding `pylab.ion()` and `plt.show()` to your codes.

This is conveninent if you need to do some interactive work in a terminal, but it does remove some of the interactive features of spyder. You can recover some of the functionality using the following functions

```python
a = np.arange(20)
print type(a)  # prints the data type of a
print dir(a)  # prints all the variables and functions inside of object a
print a.shape  # prints the dimension of a (rows, columns), only works on numpy arrays
```

In addition you can use a number of ipython specific commands to emulate of the features of spyder including
```
%hist  # prints history
np.arange?  # prints doc string of function/object
plt.plot??  # prints source of function/object
```

You can also use regular linux commands by prepending `!` to the beginning. For example
```
!ls
!cd ~/
```

For more details type `%quickref` in an ipython terminal
