# Programming Best Practices

## Goals

* Easy debugging
* Easy modification
* Understandability (now, after passage of time, and to another person)
* Speed

## Strategies
* Plan – consider likely rate-limiting steps and best methodology before starting
* Modularize – test subcomponents and use branches in Git
* Check variable values, types, array sizes by hand (print statements or interrupted run)
* Don’t assume “running” = “working”; brainstorm sanity checks
* Use meaningful variable names (more than one letter!) that are not too similar
* Keep standard defaults: e.g. i, j reserved for integer loop counters
* Replace hardwired numbers with constant names at top of code or even in separate file
* Write comments (including to bookend command sets, e.g. in if-then)
* Take advantage of helpful visual appearance: white space, syntax highlighting
* Avoid loops when unnecessary (possible tradeoff with understandability)
* Manage I/O and memory; eliminate large arrays when no longer needed
* Use print and system time statements to find out where code fails/slows

## Python-specific tips ##
* avoid "import" for scripts -- they will run at the time of import! use the "def main" protocol if you want your code to be both callable like a script and importable like a package -- see [this link](https://en.wikibooks.org/wiki/Python_Programming/Modules)
* don't define a function in the middle of a program, even though python lets you -- doing this muddles whether variables are defined inside or outside the function
* you can't use the variable name "lambda", it's a reserved word
* do not use tabs as white space; standard indentation of code levels is 4 spaces (this is a matter of preference, but standardizing is essential when collaborating)
* when speed is critical use libraries written in C and/or packages and functions set up to multi-thread
* debug using the python debugger module "pdb" ([quick tutorial here](https://pythonconquerstheuniverse.wordpress.com/category/python-debugger/))
* time code using the system clock, for example: 

```python
import numpy as np
import time

init_time = time.clock()  # start clock
x = np.linspace(0,100,1000000)
y = np.sqrt(x)

elap_time = time.clock() - init_time  # finds difference

print "Time elapsed is %0.3f ms" % (elap_time*1000)  # converts to ms
```

or in ipython try using the [`%time`](https://ipython.org/ipython-doc/3/interactive/magics.html#magic-time) and [`%timeit`](https://ipython.org/ipython-doc/3/interactive/magics.html#magic-timeit) magics

__Note that for complicated code, %timeit is more reliable than time.clock(). You should use a protected version of the code if you want to run %timeit on the ipython command line (for example, you can type `import templatecodeprotected` then `%timeit templatecodeprotected.main()`).__
