# Un-Tutorial on Multiprocessing
by Sheila Kannappan, created June 2017

These notes naturally follow the [Bootstrapping Tutorial](https://github.com/capprogram/2017bootcamp-general/blob/master/bootstrap.md) because once you start bootstrapping, it's easy to create codes with nested Monte Carlos that blow up in compute time, so you might like to take advantage of multiple processors.

This is an _Un-Tutorial_ because the author is in no way an expert on multiprocessing and is simply sharing her own real-time learning process.

## Cautionary notes

1) You will earn much greater speed gains by vectorizing your code than by adding multiprocessing. Scour your code for unnecessary loops before worrying about multiprocessing.    
2) The time you spend coding _plus_ the time you spend running code equals your total computing time, so think carefully about whether the potential gains are worth it before spending a lot of time getting multiprocessing to work.    
3) You can make people really mad by using all the cores on a machine -- always check with other users to find out what is a reasonable maximum you can use. Even if you're alone on a machine, it's wise to leave one core free for the operating system.    
4) Numerous details -- hardware, OS, and package or Python versions -- may strongly dictate the efficiency of multiprocessing. You may have to do some experimenting to get worthwhile speedup factors.    
5) Timing your code with `%timeit` on the ipython command line works reliably, but for some reason `time.clock()` yields spuriously low execution times on many linux servers. Don't believe speedup factors of 1000 if you only have 8 cores!

## Multithreading vs. Multiprocessing
As explained in this [jupyter notebook](https://github.com/galastrostats/general/blob/master/PythonMultiprocessing.ipynb) by former UNC undergraduate Sheridan Green, if you're new to this business and working in Python, you'll almost certainly want to be doing _multiprocessing_, not multithreading. Note however that the speed gains from multiprocessing are usually less than N-1 for an N core machine. In fact the timing example given in the jupyter notebook is misleading: if you run [Sheridan's time test code](https://github.com/capprogram/2017bootcamp-general/blob/master/stt.py) on different machines and try different numbers of processors, you will see that your mileage may vary. I have minimally modified his code to allow you to run `%timeit stt.main(nproc)` on the ipython command line, where nproc is a number between 1 and N-1. You can test different machines with his code to see whether they will yield useful speedup factors before bothering to code up your own multiprocessing.

## Bootstrapping on Steroids    
To illustrate what I've learned about multiprocessing, I've constructed a wrapper code for the [bootstrap line-fitting code](https://github.com/capprogram/2017bootcamp-general/blob/master/paramfit1_boot.py) from the [Bootstrapping Tutorial](https://github.com/capprogram/2017bootcamp-general/blob/master/bootstrap.md). The wrapper allows the user to re-run the bootstrapping code on more than one simulated data set. In other words, the code runs two nested Monte Carlos: one that generates simulated data sets, and one that performs bootstrap resampling on each individual simulated data set. You can compare the different implementations of this code linked below using `%timeit`.



Incidentally, the plot made by the wrapped bootstrapping code is actually interesting: it tests how bootstrap uncertainties compare to uncertainties derived more precisely, when averaged over many different randomly generated data sets. That is, the plot looks at the "errors in the errors" from bootstrapping. Examining the plot, how far off can bootstrap uncertainties get for any one data set? Averaged over many data sets, are they biased (meaning they generally run low or high)? What do you notice about the errors uncertainties in the slope vs. in the intercept?
