"""
Tutorial on Histograms, KDE, and Hypothesis Tests for Comparing Distributions
Author: Sheila Kannappan
June 2017: heavily adapted from the original -- see 
https://github.com/galastrostats/general/blob/master/distributions.md
"""

import numpy as np              # basic numerical analysis
import matplotlib.pyplot as plt # plotting
import scipy.stats as stats     # statistical functions
import numpy.random as npr      # random number generation
#import pdb                      # python debugger
from astroML.plotting import hist # see Ivezic+ pp. 165, 225, 228
from sklearn.neighbors import KernelDensity # see Ivezic+ pp. 251-255

"""
Let's explore the distribution of galaxy colors using ECO.
We'll use the input file "ECO_dr1_subset.csv" which contains these columns:
'NAME', 'CZ', 'LOGMSTAR', 'MODELU_RCORR', 'R90', 'MORPHEL',
'GRPCZ', 'FC', 'LOGMH', 'DEN1MPC'.
"""

data = np.genfromtxt("ECO_dr1_subset.csv", delimiter=",", dtype=None, names=True)
name = data['NAME']
logmstar = data ['LOGMSTAR']
urcolor = data['MODELU_RCORR']
cz = data['CZ']
goodur = (urcolor > -99) & (logmstar > 10.)

colors=urcolor[goodur]

# First plot histograms of u-r color with different bin width "rules"
plt.figure(1)
plt.clf()
hist(colors,bins='freedman',label='freedman',normed=1,histtype='stepfilled',color='green',alpha=0.5)
hist(colors,bins='scott',label='scott',normed=1,histtype='step',color='purple',alpha=0.5,hatch='///')
# note the different format used below so as to save the bin info for Knuth's rule
n0, bins0, patches0 = hist(colors,bins='knuth',label='knuth',normed=1,histtype='stepfilled',color='blue',alpha=0.25)
plt.xlim(0,3)
plt.xlabel("u-r color (mag)")
plt.title("Galaxy Color Distribution")
plt.legend(loc="best")
# As in Fig. 5.20 (p. 227), Scott's rule makes broader bins.

# Now give Kernel Density Estimation a try. KDE is shown in Ivezic+ Fig. 6.1 
# but we'll use this newer version: sklearn.neighbors.KernelDensity -- see
# http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html

bw = 0.5*(bins0[2]-bins0[1]) 
# initially using 0.5*Knuth binsize from above as bandwidth; should test other values

kde = KernelDensity(kernel='epanechnikov',bandwidth=bw).fit(colors[:,np.newaxis])
xx = np.linspace(-2,16,10000)[:,np.newaxis]
logdens = kde.score_samples(xx)
plt.figure(1)
plt.plot(xx,np.exp(logdens),color='green',label='kde')
plt.legend(loc="best")

# The KDE peaks seem to be in between histogram bin peaks for Knuth and
# Freedman, showing the sensitivity of histograms to bin boundaries.
# Scott is broader so fails to define the peak location as clearly.

# Next we'll perform some common-sense checks. For example, do we get the 
# same color distributions in different subvolumes of ECO?

# Compare color distributions for galaxies at closer and further distances
nearby = (cz[goodur] > 5500.) # redshift is a proxy for distance
selenvnear = np.where(nearby)
selenvfar = np.where(~nearby)

plt.figure(2)
plt.clf()
hist(colors[selenvnear],bins='knuth',label='near',normed=1,histtype='stepfilled',color='red',alpha=0.25)
plt.xlim(0,3)
kde = KernelDensity(kernel='epanechnikov',bandwidth=bw).fit(colors[selenvnear][:,np.newaxis])
logdens = kde.score_samples(xx)
plt.plot(xx,np.exp(logdens),'r--')
hist(colors[selenvfar],bins='knuth',label='far',normed=1,histtype='stepfilled',color='blue',alpha=0.25)
kde = KernelDensity(kernel='epanechnikov',bandwidth=bw).fit(colors[selenvfar][:,np.newaxis])
logdens = kde.score_samples(xx)
plt.plot(xx,np.exp(logdens),'b--')

# Use the Kolmogorov-Smirnov and Mann-Whitney U tests to compare distributions
DD, pnullks = stats.ks_2samp(colors[selenvnear],colors[selenvfar])
UU, pnullmw = stats.mannwhitneyu(colors[selenvnear],colors[selenvfar])
plt.text(1.1, 1.7, "K-S pnull = %0.2g" % pnullks, size=14, color='b')
plt.text(1.1, 1.5, "M-W pnull = %0.2g" % pnullmw, size=14, color='b')
plt.xlabel("u-r color (mag)")
plt.legend()

# Yikes! These two samples are not drawn from the same parent distribution, even
# though ECO is volume-limited. How can this be? The near and far regions of ECO
# have different large-scale galaxy densities ("cosmic variance"), affecting 
# galaxy colors. So instead of dividing by distance, let's try dividing randomly.

namegood = name[goodur]

makenew = True
if makenew:
    #pdb.set_trace()
    sample2inds = npr.choice(len(namegood),size=int(round(0.5*len(namegood)-1)),replace=False)
    flag12 = np.zeros(len(namegood),dtype=int)
    flag12[sample2inds] = 1
    flag12 += 1
    # since the random subsamples change each time we re-run, we can uncomment
    # the command below to save a favorite randomization, then set makenew=False
    # for subsequent runs
    # np.savez('samplesplitflag',flag12=flag12)
else:
    input = np.load("samplesplitflag.npz")
    flag12 = input['flag12']
    
sample1inds = np.where(flag12 == 1)
sample2inds = np.where(flag12 == 2)

plt.figure(3)
plt.clf()
n, bins, patches = hist(colors[sample1inds],bins='knuth',label='1',histtype='stepfilled',color='red',alpha=0.25)
hist(colors[sample2inds],bins=bins,label='2',histtype='stepfilled',color='blue',alpha=0.25)
plt.xlim(0,3)
DD, pnullks = stats.ks_2samp(colors[sample1inds],colors[sample2inds])
plt.text(1.1, 200, "K-S pnull = %0.2g" % pnullks, size=14, color='b')
plt.xlabel("u-r color (mag)")
plt.legend()

# rerunning the randomization over and over should give you a sense of how much
# pnull can jump around -- remember the p-value crisis!
