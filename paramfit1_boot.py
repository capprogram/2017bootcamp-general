"""
Code for Tutorial on Parameter Estimation by Maximum Likelihood Fitting
Modified by Kathleen Eckert from an activity written by Sheila Kannappan
++version with BOOTSTRAPPING added by Sheila Kannappan June 2017
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.random as npr
from astroML.utils import check_random_state

# Generating fake data set to start with:
alphatrue=2. # slope
betatrue=5.  # intercept
errs=2.5 # sigma (amplitude of errors)

narr=50 # number of data points
xvals = np.arange(narr) + 1. # xvals range from 1-51
yvals = alphatrue*xvals + betatrue + npr.normal(0,errs,narr) # yvals 

# Plot fake data
plt.figure(1) 
plt.clf()
plt.plot(xvals,yvals,'b*',markersize=10)
plt.xlabel("x-values")
plt.ylabel("y-values")

# Determine slope & y-intercept using least squares analytic solution 

alphaest=(np.mean(xvals)*np.mean(yvals)-np.mean(xvals*yvals)) / \
   (np.mean(xvals)**2 -np.mean(xvals**2)) #  from derivation
betaest= np.mean(yvals) - alphaest * np.mean(xvals) # calculate estimate of y-intercept from derivation

# The MLE values of the slope and y-intercept are equivalent to the "least
# squares" fit results.
print("analytical MLE slope = %0.7f" %alphaest)
print("analytical MLE y-intercept = %0.7f" %betaest)

# Overplot the MLE ("best fit") solution
yfitvals=xvals*alphaest+betaest
plt.plot(xvals,yfitvals,'r')

# Compute analytic uncertainties on slope and y-intercept 

alphaunc = np.sqrt(np.sum((yvals - (alphaest*xvals+betaest))**2) / ((narr-2.)*(np.sum((xvals-np.mean(xvals))**2))))
betaunc = np.sqrt((np.sum((yvals - (alphaest*xvals+betaest))**2) / (narr-2.)) * ((1./narr) + (np.mean(xvals)**2)/np.sum((xvals-np.mean(xvals))**2)) )

print("analytical MLE uncertainty on alpha is %0.7f" % (alphaunc))
print("analytical MLE uncertainty on beta is %0.7f" % (betaunc))

print("fractional uncertainty on alpha is %0.7f" % (alphaunc/alphaest))
print("fractional uncertainty on beta is %0.7f" % (betaunc/betaest))

# Solution using python solver np.polyfit
# third parameter is order of fit, 1 for linear
pfit = np.polyfit(xvals, yvals, 1) # returns coeff. of highest order term first

print("               ") # put in some whitespace to make easier to read
print("np.polyfit MLE slope = %0.7f" %pfit[0])
print("np.polyfit MLE y-intercept = %0.7f" %pfit[1])

# Can also obtain parameter uncertainties from the diagonal terms of the covariance
# matrix, which is the inverse of the Hessian matrix and
# can be computed in np.polyfit by setting cov='True'

pfit,covp = np.polyfit(xvals, yvals, 1, cov='True') # returns coeff. of highest power first
# setting cov='True' returns the covariance matrix
print("slope is %0.7f +- %0.7f" % (pfit[0], np.sqrt(covp[0,0])))
print("intercept is %0.7f +- %0.7f" % (pfit[1], np.sqrt(covp[1,1])))

# BOOTSTRAP!

npars = 2 # slope and intercept
nboot = 10000 # usually want at least 1000
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

print("               ") # put in some whitespace to make easier to read
print("bootstrap slope is %0.7f + %0.7f - %0.7f" % (slopemed,slope68pcterrs[0],slope68pcterrs[1]))
print("bootstrap intercept is %0.7f + %0.7f - %0.7f" % (intmed,int68pcterrs[0],int68pcterrs[1]))
print("slope error ratio: %0.5f" % (0.5*(np.sum(slope68pcterrs))/np.sqrt(covp[0,0])))
print("int error ratio: %0.5f" % (0.5*(np.sum(int68pcterrs))/np.sqrt(covp[1,1])))

# running this code repeatedly to generate different data sets reveals that the
# bootstrap uncertainties are less reliable than the analytic and Hessian-
# derived uncertainties, but still perform surprisingly well, even with only
# 50 data points to resample
