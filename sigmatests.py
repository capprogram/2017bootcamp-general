"""
Tests of measuring sigma with np.std, bootstrap, and smoothed bootstrap
Author: Sheila Kannappan
created September 2016
"""
# standard imports and naming conventions; uncomment as needed
import numpy as np              # basic numerical analysis
import matplotlib.pyplot as plt # plotting
#import scipy as sp              # extended scientific function
import scipy.stats as stats     # statistical functions
#import numpy.random as npr      # random number generation
#import astropy as ap            # core astronomy library
import astroML.resample as mlre # machine learning for astronomy
#import astroML.datasets as mld  # datasets
#import pymc                     # bayesian package with MCMC
#import pdb                      # python debugger
#import time                     # python timekeeper
#plt.ion()                       # use if working in ipython under linux
from smoothedbootstrap import smoothedbootstrap

Ndata=5
Nbootstrap=2000

truemean = 0.
truesigma = 1.

nruns = 1000
sigstddev = np.zeros(nruns)
sigboot = np.zeros(nruns)
sigsmboot = np.zeros(nruns)

for irun in xrange(nruns):
    np.random.seed()
    data = stats.norm(truemean, truesigma).rvs(Ndata)
    sigstddev[irun] = np.std(data,ddof=1)
    sigboot[irun] = np.median(mlre.bootstrap(data, Nbootstrap,  np.std, kwargs=dict(axis=1, ddof=1)))
    sigsmboot[irun] = np.median(smoothedbootstrap(data, Nbootstrap,  np.std, kwargs=dict(axis=1, ddof=1)))
#    code here in loop looks at all bootstrap results for a single run (single data set)
    if irun == 17: # choose 17 as an example run for no particular reason
        fig0, ax0 = plt.subplots(figsize=(5, 3.75))
        ax0.hist(smoothedbootstrap(data, Nbootstrap,  np.std, kwargs=dict(axis=1, ddof=1)), bins=50, normed=True, histtype='step',
            color='green', lw=2, label=r'$\sigma\ {\rm (sm. bootstrap)}$')
        ax0.hist(mlre.bootstrap(data, Nbootstrap,  np.std, kwargs=dict(axis=1, ddof=1)), bins=50, normed=True, histtype='step',
           color='red', lw=2, label=r'$\sigma\ {\rm (bootstrap)}$')

# code below looks at the median bootstrap results for all nruns data sets (one median per run)
fig, ax = plt.subplots(figsize=(5, 3.75))
ax.hist(sigstddev, bins=50, normed=True, histtype='step',
        color='blue', ls='dashed', label=r'$\sigma\ {\rm (stddev)}$')
ax.hist(sigboot, bins=50, normed=True, histtype='step',
        color='red', label=r'$\sigma\ {\rm (bootstrap)}$')
ax.hist(sigsmboot, bins=50, normed=True, histtype='step',
        color='green', lw=2, label=r'$\sigma\ {\rm (sm. bootstrap)}$')
ax.legend()

fig2, ax2 = plt.subplots(figsize=(5, 3.75))
ax2.hist(sigboot/sigstddev, bins=50, normed=True, histtype='step',
        color='red', label=r'$\sigma\ {\rm (bootstrap)}$')
ax2.hist(sigsmboot/sigstddev, bins=50, normed=True, histtype='step',
        color='green', lw=2, label=r'$\sigma\ {\rm (sm. bootstrap)}$')
ax2.legend(loc='upper left')