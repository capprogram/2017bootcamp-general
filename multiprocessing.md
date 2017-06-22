# Un-Tutorial on Multiprocessing
by Sheila Kannappan, created June 2017

These notes naturally follow the [Bootstrapping Tutorial](https://github.com/capprogram/2017bootcamp-general/blob/master/bootstrap.md) because once you start bootstrapping, it's easy to create codes with nested Monte Carlos that blow up in compute time, so you might like to take advantage of multiple processors.

This is an _Un-Tutorial_ because the author is in no way an expert on multiprocessing and is simply sharing her own real-time learning process. We will consider only "embarrassingly parallel" applications, i.e., situations where an identical task is repeated many times so could be repeated in parallel rather than serial processing.

You may want to use a server-class machine for this activity, but most desktops and laptops do have 2-4 cores these days.

## Cautionary notes

1) Consider not pursuing this. You will earn much greater speed gains by vectorizing your code than by adding multiprocessing. The time you spend coding _plus_ the time your code spends running equals your total project time, so be sure the potential gains are worth it before spending a lot of time getting multiprocessing to work. Numerous details -- hardware, OS, and package or Python versions -- can affect the efficiency of multiprocessing, so you might have to do a lot of experimenting.     
2) You can cause problems for others by using all the cores on a machine -- always check with other users to find out what is a reasonable maximum you can use. Even if you're alone on a machine, it's wise to leave one core free for the operating system.    
3) If you are using a pseudo-random number generator in multiprocessing, you must initialize the seed in the code, e.g., with `npr.seed()`, or else you will get a bunch of processes spawning all at the same time, all with the same seed, yielding identical results.
4) Timing your code with `%timeit` on the ipython command line works reliably, but for some reason `time.clock()` yields spuriously low execution times for multiprocessing on (some/all?) linux servers. Don't believe speedup factors of 1000 if you only have 8 cores! To use `%timeit` on a script, make sure it's protected (put the main code in a `def main():` block and add a `if __name__ == '__main__': main()` statement at the end), then import it, then call its main function: `%timeit myscript.main()`.

## Multithreading vs. Multiprocessing
As explained in this [jupyter notebook](https://github.com/galastrostats/general/blob/master/PythonMultiprocessing.ipynb) by former UNC undergraduate Sheridan Green, if you're new to this business and working in Python, you'll almost certainly want to be doing _multiprocessing_, not multithreading. Note however that the speed gains from multiprocessing are usually less than N-1 for an N core machine. In fact the timing example given in the jupyter notebook is misleading: if you run [Sheridan's time test code](https://github.com/capprogram/2017bootcamp-general/blob/master/stt.py) on different machines and try different numbers of processors, you will see that your mileage may vary. I have minimally modified his code to allow you to run `%timeit stt.main(nproc)` on the ipython command line, where nproc is a number between 1 and N-1. You can test different machines with his code to see whether they will yield useful speedup factors before bothering to code up your own multiprocessing.

## Bootstrapping on Steroids    
To illustrate what I've learned about multiprocessing, I've constructed a [wrapper code](https://github.com/capprogram/2017bootcamp-general/blob/master/paramfit1_boot_mp.py) for the [bootstrap line-fitting code](https://github.com/capprogram/2017bootcamp-general/blob/master/paramfit1_boot.py) from the [Bootstrapping Tutorial](https://github.com/capprogram/2017bootcamp-general/blob/master/bootstrap.md). The wrapper allows the user to re-run the bootstrapping code on more than one simulated data set. In other words, the code runs two nested Monte Carlos: one that generates simulated data sets, and one that performs bootstrap resampling on each individual simulated data set. Look at the code to see how the parallelization is implemented with the `multiprocessing` package in the "def main" code block. (An alternative package for multiprocessing is `joblib`, which I tried and successfully got working, but it requires installation and uses `multiprocessing` under the hood.) You can compare run times like so:

``` python
  import paramfit1_boot_mp
  %timeit paramfit1_boot_mp.main(40, 4, "both") # to generate 40 data sets, use 4 processors, and use both serial and parallel processing
  %timeit paramfit1_boot_mp.main(40, 4, "p") # to generate 40 data sets, use 4 processors, and use parallel processing
  %timeit paramfit1_boot_mp.main (40, 4, "s") # to generate 40 data sets and use serial processing (number of processors input is not used)
```

Notice that the run times printed by the code itself (computed with `time.clock()`) are not accurate when using multiprocessing.

Incidentally, the plot made by the above codes is actually interesting: it tests how bootstrap uncertainties compare to uncertainties derived more precisely, when averaged over many different randomly generated data sets. That is, the plot looks at the "errors on the errors" from bootstrapping. Examining the plot, how far off do bootstrap uncertainties get for any one data set? Averaged over many data sets, are they biased (meaning they generally run low or high)? What do you notice about the errors on the uncertainties in the slope vs. in the intercept?
