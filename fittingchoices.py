"""
Fitting Choices Tutorial Code
Author: Sheila Kannappan
Created: August 2016
"""

# standard imports and naming conventions; uncomment as needed
import numpy as np              # basic numerical analysis
import matplotlib.pyplot as plt # plotting
#import scipy as sp              # extended scientific function
#import scipy.stats as stats     # statistical functions
import numpy.random as npr      # random number generation
#import astropy as ap            # core astronomy library
#import astroML as ml            # machine learning for astronomy
#import astroML.datasets as mld  # datasets
#import pymc                     # bayesian package with MCMC
#import pdb                      # python debugger
#import time                     # python timekeeper
#plt.ion()                       # use if working in ipython under linux

def bisectorslope(fsl,isl):
    # function to compute bisector slope from forward and inverse slopes
    # using formula in Isobe et al (1990)
    bsl1 = (1./(fsl+isl))
    bsl2 = (fsl*isl - 1. + np.sqrt((1.+fsl**2)*(1.+isl**2)))
    bsl = bsl1*bsl2
    return bsl

def rms(modelpts,datapts):
    # function to compute residuals from a model evaluated at same x-values
    resids = modelpts - datapts
    rms = np.sqrt(np.mean(resids**2))
    return rms

def biweight(modelpts,datapts):
    ctune = 9.0
    resids = modelpts - datapts
    med = np.median(resids)
    MAD = np.median(np.abs(resids-med))
    ui=(resids-med)/(ctune*MAD)
    biwt = np.sqrt(len(datapts))*np.sqrt(np.sum(((resids-med)**2*(1-ui**2)**4)))/ \
        np.abs(np.sum(((1-ui**2)*(1-5*ui**2))))
    return biwt

npr.seed(111) # get the same plots every time by fixing the seed

# set up data and plot underlying "true" relation
ndata=100
xx = np.linspace(1,10,ndata)
yy = np.linspace(10,40,ndata)
xlim = np.array([-6,17.])
plt.figure(1,figsize=(10,10))
plt.clf()
plt.xlim(xlim)
plt.plot(xx,yy,'r')

# add random and systematic errors
syserr = np.zeros(ndata)
syserr[npr.randint(0,99,size=5)] = 2.
syserr[npr.randint(0,99,size=5)] = 3.
sigma = 1.
yyscat = yy + npr.normal(0,sigma,ndata) + syserr

# compute and plot forward and inverse fits
plt.figure(2,figsize=(10,10))
plt.clf()
plt.xlim(xlim)
pforward = np.polyfit(xx,yyscat,1)
slopefor = pforward[0]
intfor = pforward[1]
pinverse = np.polyfit(yyscat,xx,1)
slopeinv = 1./pinverse[0]
intinv = -1.*pinverse[1]/pinverse[0]
plt.plot(xx,yyscat,'r.',label="data")
plt.plot(xlim,slopefor*xlim+intfor,'b',label="forward")
plt.plot(xlim,slopeinv*xlim+intinv,'g',label="inverse")
plt.plot(xx,yy,color='black',ls=':',label="true")

# compute and plot bisector fit
slopebis = bisectorslope(slopefor,slopeinv)
intbis = np.mean(yyscat) - slopebis*np.mean(xx)
plt.plot(xlim,slopebis*xlim+intbis,'m--',label="bisector")
plt.legend(loc="best")

# compare rms and biweight
print "forward fit rms %f and biweight %f" % ((rms(slopefor*xx+intfor,yyscat),biweight(slopefor*xx+intfor,yyscat)))
print "inverse fit rms %f and biweight %f" % ((rms(slopeinv*xx+intinv,yyscat),biweight(slopeinv*xx+intinv,yyscat)))
print "bisector fit rms %f and biweight %f" % ((rms(slopebis*xx+intbis,yyscat),biweight(slopebis*xx+intbis,yyscat)))

# All fits appear visually similar but in fact the lowest residuals are for the
# forward fit, which is the correct fit since all scatter is in the y direction
# by construction.

# The scatter is more accurately measured by the biweight, which is less 
# sensitive to outliers and thus comes closer to the true value of 1.

# add scatter in x
sigmax = 3.
xxscat = xx + npr.normal(0,sigmax,ndata)

# compute and plot forward and inverse fits
plt.figure(3,figsize=(10,10))
plt.clf()
plt.xlim(xlim)
pforward = np.polyfit(xxscat,yyscat,1)
slopefor = pforward[0]
intfor = pforward[1]
pinverse = np.polyfit(yyscat,xxscat,1)
slopeinv = 1./pinverse[0]
intinv = -1.*pinverse[1]/pinverse[0]
plt.plot(xxscat,yyscat,'r.',label="data")
plt.plot(xlim,slopefor*xlim+intfor,'b',label="forward")
plt.plot(xlim,slopeinv*xlim+intinv,'g',label="inverse")
plt.plot(xx,yy,color='black',ls=':',label="true")

# compute and plot bisector fit
slopebis = bisectorslope(slopefor,slopeinv)
intbis = np.mean(yyscat) - slopebis*np.mean(xxscat)
plt.plot(xlim,slopebis*xlim+intbis,'m',label="bisector")
plt.legend(loc="best")

# compare rms and biweight
print "forward fit rms %f and biweight %f" % ((rms(slopefor*xxscat+intfor,yyscat),biweight(slopefor*xxscat+intfor,yyscat)))
print "inverse fit rms %f and biweight %f" % ((rms(slopeinv*xxscat+intinv,yyscat),biweight(slopeinv*xxscat+intinv,yyscat)))
print "bisector fit rms %f and biweight %f" % ((rms(slopebis*xxscat+intbis,yyscat),biweight(slopebis*xxscat+intbis,yyscat)))

# The bisector appears most correct by "gut feeling", but comparing to the true
# slope it appears that in fact the inverse fit is superior. The disagreement is
# probably because the eye naturally minimizes residuals in both x and y. The 
# best fit does not correspond to the fit with lowest scatter in y because now
# both x and y have inherent scatter. Since the scatter in x is larger, we might
# better identify the best fit by minimizing scatter in x. See below.

# compare in x-axis direction
slopeinvx = pinverse[0]
intinvx = pinverse[1]
slopeforx = 1./pforward[0]
intforx = -1.*pforward[1]/pforward[0]
slopebisx = bisectorslope(slopeforx,slopeinvx)
intbisx = np.mean(xxscat) - slopebisx*np.mean(yyscat)
print "forward fit rms-x %f and biweight-x %f" % ((rms(slopeforx*yyscat+intforx,xxscat),biweight(slopeforx*yyscat+intforx,xxscat)))
print "inverse fit rms-x %f and biweight-x %f" % ((rms(slopeinvx*yyscat+intinvx,xxscat),biweight(slopeinvx*yyscat+intinvx,xxscat)))
print "bisector fit rms-x %f and biweight-x %f" % ((rms(slopebisx*yyscat+intbisx,xxscat),biweight(slopebisx*yyscat+intbisx,xxscat)))
# Now that we look at scatter in the x-direction, the inverse fit clearly shows 
# the minimum scatter.

# The biweight and rms look similar because the scatter is dominated by random
# errors rather than systematic errors.

# apply selection bias
xxcut = xxscat[np.where(xxscat > 3.)]
yycut = yyscat[np.where(xxscat > 3.)]

# compute and plot forward and inverse fits
plt.figure(4,figsize=(10,10))
plt.clf()
plt.xlim(xlim)
pforward = np.polyfit(xxcut,yycut,1)
slopefor = pforward[0]
intfor = pforward[1]
pinverse = np.polyfit(yycut,xxcut,1)
slopeinv = 1./pinverse[0]
intinv = -1.*pinverse[1]/pinverse[0]
plt.plot(xxcut,yycut,'r.',label="data")
plt.plot(xlim,slopefor*xlim+intfor,'b',label="forward")
plt.plot(xlim,slopeinv*xlim+intinv,'g',label="inverse")
plt.plot(xx,yy,color='black',ls=':',label="true")

# compute and plot bisector fit
slopebis = bisectorslope(slopefor,slopeinv)
intbis = np.mean(yycut) - slopebis*np.mean(xxcut)
plt.plot(xlim,slopebis*xlim+intbis,'m',label="bisector")
plt.legend(loc="best")

# compare rms and biweight
print "forward fit rms %f and biweight %f" % ((rms(slopefor*xxcut+intfor,yycut),biweight(slopefor*xxcut+intfor,yycut)))
print "inverse fit rms %f and biweight %f" % ((rms(slopeinv*xxcut+intinv,yycut),biweight(slopeinv*xxcut+intinv,yycut)))
print "bisector fit rms %f and biweight %f" % ((rms(slopebis*xxcut+intbis,yycut),biweight(slopebis*xxcut+intbis,yycut)))

# compare in x-axis direction
slopeinvx = pinverse[0]
intinvx = pinverse[1]
slopeforx = 1./pforward[0]
intforx = -1.*pforward[1]/pforward[0]
slopebisx = bisectorslope(slopeforx,slopeinvx)
intbisx = np.mean(xxcut) - slopebisx*np.mean(yycut)
print "forward fit rms-x %f and biweight-x %f" % ((rms(slopeforx*yycut+intforx,xxcut),biweight(slopeforx*yycut+intforx,xxcut)))
print "inverse fit rms-x %f and biweight-x %f" % ((rms(slopeinvx*yycut+intinvx,xxcut),biweight(slopeinvx*yycut+intinvx,xxcut)))
print "bisector fit rms-x %f and biweight-x %f" % ((rms(slopebisx*yycut+intbisx,xxcut),biweight(slopebisx*yycut+intbisx,xxcut)))

# The bisector fit is the least awful, but none of the fits is great. It would be
# better to properly model both the errors and the selection bias.

# If we want to predict y, we want to find the middle of the scatter in y at
# each given x, i.e., we want symmetric residuals around the predicted y at 
# each x. This goal implies a forward fit, which minimizes residuals in the y-
# direction. A first pass at this is shown here...

plt.figure(5,figsize=(10,10))
plt.clf()
plt.xlim(xlim)
pforward = np.polyfit(xxcut,yycut,1)
slopefor = pforward[0]
intfor = pforward[1]
plt.plot(xxcut,yycut,'r.',label="data")
plt.plot(xlim,slopefor*xlim+intfor,'b',label="forward")
plt.plot(xx,yy,color='black',ls=':',label="true")
plt.legend(loc="best")

#... but it isn't optimal because asymmetric scatter (in other words,  
# apparent deviations from linearity in the data) skews the fit. If we want
# to stick with a linear prediction, we can improve the prediction over a
# restricted range by trimming the data to exclude high/low values of x
# where there is asymmetric scatter. The prediction is then invalid outside
# the calibration range. Eyeballing it, trimming x>12 should work well for us.

xtofit = xxcut[xxcut < 12]
ytofit = yycut[xxcut < 12]
pforwardtrim = np.polyfit(xtofit,ytofit,1)
slopefortrim = pforwardtrim[0]
intfortrim = pforwardtrim[1]
plt.plot(xlim,slopefortrim*xlim+intfortrim,'g',label="trimmed forward")
plt.plot([12,12],[0,100],color="black",linestyle='--')
plt.legend(loc="best")

# Picking any x, we can see that the trimmed forward fit bisects the scatter in
# y better than the forward fit, as long as x<12. It is noticeable that although 
# the trimmed forward fit gives the best *prediction* of y given x, it does not
# resemble the true underlying y(x) relation. Our prediction aims to find the
# most likely y measurement given a certain x measurement, so it folds in all
# the errors and selection biases of real data *on purpose*, and the prediction
# will only work in a situation with similar errors and biases. In contrast, the
# true y(x) relation is a property of nature, obscured by errors and biases.
# Incidentally, to be truly rigorous, we might want to replace our eyeballed 
# trimming with trimming based on either physical knowledge or statistical 
# optimization. In the latter case we would need to construct a cost function
# that balanced the number of points trimmed against the summed residuals
# of the points not trimmed.