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
#import multiprocessing as mp
import joblib as jl
import time

def newdatafullbootstrap(runindex):
    # NOTE: all print and plot commands removed, would be blocked by
    # multiprocessing wrapper anyway
    nproc = 3
    
    # Generate a fresh seed
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
# duplicate np.polyfit command below can be commented out now
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
    #bootresults = np.zeros((npars,nboot))
    bootres = jl.Parallel(n_jobs = nproc)(jl.delayed(np.polyfit)(xvals[ind[:,iboot]], yvals[ind[:,iboot]], 1) for iboot in xrange(nboot))
    sloperesults,intresults = zip(*bootres)
    #for iboot in xrange(nboot):
    #    bootresults[:,iboot] = np.polyfit(xvals[ind[:,iboot]], yvals[ind[:,iboot]], 1)
    #sloperesults = bootresults[0,:]
    #intresults = bootresults[1,:]
    slopesort = np.argsort(sloperesults)
    slopemed = np.median(sloperesults)
    pct16 = int(round(0.16*nboot))
    pct84 = int(round(0.84*nboot))
    slope68pcterrs = [slopemed-sloperesults[slopesort[pct16]],sloperesults[slopesort[pct84]]-slopemed]
    intsort = np.argsort(intresults)
    intmed = np.median(intresults)
    int68pcterrs = [intmed-intresults[intsort[pct16]],intresults[intsort[pct84]]-intmed]
    
    slope_err_ratio = 0.5*(np.sum(slope68pcterrs))/np.sqrt(covp[0,0])
    int_err_ratio = 0.5*(np.sum(int68pcterrs))/np.sqrt(covp[1,1])
    slope_err_ratio2 = 0.5*(np.sum(slope68pcterrs))/alphaunc
    int_err_ratio2 = 0.5*(np.sum(int68pcterrs))/betaunc
    
    return runindex, slope_err_ratio, int_err_ratio, slope_err_ratio2, int_err_ratio2

def main(nruns, nproc):
    #init_time = time.clock()  # start clock
    #pool = mp.Pool(processes=nproc)
    #setup_time = time.clock() - init_time
    #init_time = time.clock()  # start clock
    #results1 = pool.map(newdatafullbootstrap, range(nruns))
    #elapsed_time1 = time.clock() - init_time
    init_time = time.clock()  # start clock
    results2 = map(newdatafullbootstrap, range(nruns))
    elapsed_time2 = time.clock() - init_time
    init_time = time.clock()  # start clock
    results3=[]
    for ij in xrange(nruns):
        resultsij = newdatafullbootstrap(ij)
        results3.append(resultsij)
    elapsed_time3 = time.clock() - init_time
#    print "pool setup time (ms) %0.3f" % (1000.*setup_time)
#    print "elapsed time mp map (ms) %0.3f" % (1000.*elapsed_time1)
    print "elapsed time map (ms) %0.3f" % (1000.*elapsed_time2)
    print "elapsed time serial (ms) %0.3f" % (1000.*elapsed_time3)
    tupletypes = np.dtype('int, float, float, float, float')
    mixedarray = np.array(results3, dtype=tupletypes)
    runindex = mixedarray['f0']
    slope_err_ratio = mixedarray['f1']
    int_err_ratio = mixedarray['f2']
    slope_err_ratio2 = mixedarray['f3']
    int_err_ratio2 = mixedarray['f4']
    # Plot ratios
    plt.figure(2) 
    plt.clf()
    plt.plot(slope_err_ratio,int_err_ratio,'b*',markersize=10)
    plt.plot(slope_err_ratio2,int_err_ratio2,'r.',markersize=10)
    plt.xlabel("slope error ratio")
    plt.ylabel("intercept error ratio")