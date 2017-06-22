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
As explained in this [jupyter notebook](https://github.com/galastrostats/general/blob/master/PythonMultiprocessing.ipynb) by former UNC undergraduate Sheridan Green, if you're new to this business and working in Python, you'll almost certainly want to be doing _multiprocessing_, not multithreading. Note however that the speed gains from multiprocessing are usually less than N-1 for an N core machine. In fact the timing example given in the jupyter notebook is misleading: if you run [Sheridan's time test code](https://github.com/capprogram/2017bootcamp-general/blob/master/stt.py) on different machines and with varying numbers of processors, you will see that your mileage may vary. I have minimally modified his code to allow you to run `%timeit stt.main(nproc)` on the ipython command line, where nproc is a number between 1 and N-1. You can test different machines with this code to see whether they will yield useful speedup factors before bothering to code up your own multiprocessing.

## Bootstrapping on Steroids    
To illustrate what I've learned about multiprocessing, I've constructed a wrapper for the code from the [Bootstrapping Tutorial](https://github.com/capprogram/2017bootcamp-general/blob/master/bootstrap.md), which allows the user to re-run the bootstrapping code on more than one simulated data set. In other words, the code runs two nested Monte Carlos: one that generates simulated data sets, and one that performs bootstrap resampling on each individual simulated data set. You can use `%timeit` on the codes below to compare a few different ways of approaching the parallel vs. serial processing.



Incidentally, the output plotted by this code is worth studying, as it tests whether bootstrap uncertainties are systematically biased low or high compared to true uncertainties. For any one data set, how badly off can bootstrap uncertainties be? Averaged over many data sets how well do they do in the mean?
