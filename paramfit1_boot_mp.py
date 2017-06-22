"""
Code for Tutorial on Parameter Estimation by Maximum Likelihood Fitting
Modified by Kathleen Eckert from an activity written by Sheila Kannappan
++version with BOOTSTRAPPING added by Sheila Kannappan June 2017
++version with MULTIPROCESSING added by Sheila Kannappan June 2017
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.random as npr
from astroML.utils import check_random_state
import multiprocessing as mp
import time

def newdatafullbootstrap(runindex):
    # put original code inside "newdatafullbootstrap" function
    # runindex isn't important, just a way to label the different code runs
    # NOTE: all print and plot commands removed from original, would be 
    # blocked by multiprocessing wrapper anyway
    
    # Get a fresh seed
    npr.seed()
    
    # Generating fake data set to start with:
    alphatrue=2. # slope
    betatrue=5.  # intercept
    errs=2.5 # sigma (amplitude of errors)
    
    narr=50 # number of data points
    xvals = np.arange(narr) + 1. # xvals range from 1-51
    yvals = alphatrue*xvals + betatrue + npr.normal(0,errs,narr) # yvals 
    
    # Determine slope & y-intercept using least squares analytic solution 
    alphaest=(np.mean(xvals)*np.mean(yvals)-np.mean(xvals*yvals)) / \
       (np.mean(xvals)**2 -np.mean(xvals**2)) #  from derivation
    betaest= np.mean(yvals) - alphaest * np.mean(xvals) # calculate estimate of y-intercept from derivation
    # The MLE values of the slope and y-intercept are equivalent to the "least
    # squares" fit results.
    
    # Compute analytic uncertainties on slope and y-intercept 
    alphaunc = np.sqrt(np.sum((yvals - (alphaest*xvals+betaest))**2) / ((narr-2.)*(np.sum((xvals-np.mean(xvals))**2))))
    betaunc = np.sqrt((np.sum((yvals - (alphaest*xvals+betaest))**2) / (narr-2.)) * ((1./narr) + (np.mean(xvals)**2)/np.sum((xvals-np.mean(xvals))**2)) )
    
    # Solution using python solver np.polyfit
    # third parameter is order of fit, 1 for linear
# comment out duplicate np.polyfit command below
#    pfit = np.polyfit(xvals, yvals, 1) # returns coeff. of highest order term first
    
    # Can also obtain parameter uncertainties from the diagonal terms of the covariance
    # matrix, which is the inverse of the Hessian matrix and
    # can be computed in np.polyfit by setting cov='True'
    pfit,covp = np.polyfit(xvals, yvals, 1, cov='True') # returns coeff. of highest power first
    # setting cov='True' returns the covariance matrix
    
    # BOOTSTRAP!
    
    npars = 2 # slope and intercept
    nboot = 1000 # usually want at least 1000
    rng = check_random_state(None)
    ind = rng.randint(narr, size=(narr,nboot))
    bootresults = np.zeros((npars,nboot))
    for iboot in xrange(nboot):
        bootresults[:,iboot] = np.polyfit(xvals[ind[:,iboot]], yvals[ind[:,iboot]], 1)
    sloperesults = bootresults[0,:]
    intresults = bootresults[1,:]
    slopesort = np.argsort(sloperesults)
    slopemed = np.median(sloperesults)
    pct16 = int(round(0.16*nboot))
    pct84 = int(round(0.84*nboot))
    slope68pcterrs = [slopemed-sloperesults[slopesort[pct16]],sloperesults[slopesort[pct84]]-slopemed]
    intsort = np.argsort(intresults)
    intmed = np.median(intresults)
    int68pcterrs = [intmed-intresults[intsort[pct16]],intresults[intsort[pct84]]-intmed]
    
    # compute and return ratios of bootstrap error to fitted 
    # (Hessian-derived) and analytically computed errors
    slope_err_ratio = 0.5*(np.sum(slope68pcterrs))/np.sqrt(covp[0,0])
    int_err_ratio = 0.5*(np.sum(int68pcterrs))/np.sqrt(covp[1,1])
    slope_err_ratio2 = 0.5*(np.sum(slope68pcterrs))/alphaunc
    int_err_ratio2 = 0.5*(np.sum(int68pcterrs))/betaunc
    return runindex, slope_err_ratio, int_err_ratio, slope_err_ratio2, int_err_ratio2

def main(nruns, nproc, parallel_or_serial):
    if ((parallel_or_serial == "p") | (parallel_or_serial == "both")):
        init_time = time.clock()  # start clock
        pool = mp.Pool(processes=nproc)
        setup_time = time.clock() - init_time
        init_time = time.clock()  # start clock
        results1 = pool.map(newdatafullbootstrap, range(nruns))
        elapsed_time1 = time.clock() - init_time
    if ((parallel_or_serial == "s") | (parallel_or_serial == "both")):
        init_time = time.clock()  # start clock
        results2 = map(newdatafullbootstrap, range(nruns))
        elapsed_time2 = time.clock() - init_time
#    uncomment lines below incl. print statement to compare serial map to loop
#    if ((parallel_or_serial == "s") | (parallel_or_serial == "both")):
#        init_time = time.clock()  # start clock
#        results3=[]
#        for ij in xrange(nruns):
#            resultsij = newdatafullbootstrap(ij)
#            results3.append(resultsij)
#        elapsed_time3 = time.clock() - init_time
    print "number of data generation runs %r" % (nruns)
    if ((parallel_or_serial == "p") | (parallel_or_serial == "both")):
        print "number of processors for multiprocessing %r" % (nproc)
        print "pool setup time (ms) %0.3f" % (1000.*setup_time)
        print "elapsed time mp map (ms) %0.3f" % (1000.*elapsed_time1)
    if ((parallel_or_serial == "s") | (parallel_or_serial == "both")):
        print "elapsed time serial map (ms) %0.3f" % (1000.*elapsed_time2)
#        print "elapsed time serial loop (ms) %0.3f" % (1000.*elapsed_time3)
    tupletypes = np.dtype('int, float, float, float, float')
    if ((parallel_or_serial == "p") | (parallel_or_serial == "both")):
        mixedarray = np.array(results1, dtype=tupletypes)
    else:
        mixedarray = np.array(results2, dtype=tupletypes)
    runindex = mixedarray['f0']
    slope_err_ratio = mixedarray['f1']
    int_err_ratio = mixedarray['f2']
    slope_err_ratio2 = mixedarray['f3']
    int_err_ratio2 = mixedarray['f4']
    # Plot ratios
    plt.figure(1) 
    plt.clf()
    plt.plot(slope_err_ratio,int_err_ratio,'b*',markersize=10,label="ratio of bootstrap:fit error")
    plt.plot(slope_err_ratio2,int_err_ratio2,'r.',markersize=10,label="ratio of bootstrap:analytic error")
    plt.legend(loc="best")
    plt.xlabel("slope error ratio")
    plt.ylabel("intercept error ratio")

if __name__ == '__main__':
    main(30,3,"both") # if called standalone run with default nruns=30, nproc=3,
                      # parallel_or_serial = "both" (vs. "p" or "s")
