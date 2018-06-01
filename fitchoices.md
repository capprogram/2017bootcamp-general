# Realistic Line Fitting in the Frequentist Paradigm
### by Sheila Kannappan, updated June 2017

Up to now, we have considered only the simple case of linear fits to y vs. x where all the error is in the y direction, the errors are known (and equal and Gaussian), there are no systematic errors, and the sample is unbiased. Fitting becomes immensely more complex when we relax these assumptions, as partially discussed in Sections 4.2.6-4.2.7 and Chapter 8 of the Ivezic et al. textbook. When there is scatter in both the x and y axes, there is also a decoupling between the "best fit" and the "best prediction" of y or x (given x or y). Here we will experiment with fake data to get a feel for these issues. 

## A. Best Fits

We'll start with the situation where we are trying to determine the underlying physical relationship between x and y: the "best fit" or MLE fit. Correctly determining the MLE fit in the presence of complex errors and biases requires modifying the Likelihood function used in the fitting to reflect the exact details of the situation (e.g. as in 4.2.7 or [Hogg, Bovy, \& Lang 2010](http://lanl.arxiv.org/abs/1008.4686)). However, inverse and bisector fits, explored below, can offer a "quick and dirty" impression of how much the fit might plausibly change given different assumptions and thus tell you whether doing things correctly is worth the trouble. Unlike a traditional "forward" fit, which minimizes residuals in the y direction, an "inverse" fit minimizes residuals in the x direction, and a "bisector" fit splits the difference.

Using np.linspace, construct two 100-element “data sets” x and y such that x ranges from 1-10 and y ranges from 20-40.  Note that x and y should vary smoothly, with no randomness. If you plot y vs. x, you see the “true” relation with no measurement errors or biases.

Now add random Gaussian scatter to y with a sigma of 1. Also choose ~10 elements of y to give extra “systematic” errors of 2-3 by hand (hint – systematic errors all go in one direction, unlike random errors).  Plot y vs. x. Fit the data using forward, inverse, and bisector fits and overplot the fits. The bisector slope and intercept are given in Table 1 and equation 8 of [Isobe et al. 1990](http://adsabs.harvard.edu/abs/1990ApJ...364..104I). Label the fits and comment on which one appears most correct. In fact the lowest rms scatter corresponds to the most correct fit – why? 

For each fit, compute the rms scatter as well as the biweight scatter in the y-direction (use the formula for the biweight scatter S<sub>BI</sub> from [Beers, Flynn, & Gebhardt 1990](http://adsabs.harvard.edu/abs/1990AJ....100...32B); note that the "x" in their formulae is not the same as your x -- x just measures the scatter a.k.a. "residuals" around the fit, like the galaxy orbital velocities in a cluster are measured relative to the cluster mean velocity). Does the rms or the biweight measure the amplitude of the scatter more accurately?

Now, add Gaussian scatter to x with a sigma of 3 and repeat your fits and scatter measurements. Which type of fit appears most correct now? Consider your “gut feeling” as well as the original true relation. Why might these not agree? Why does the lowest rms scatter in y not correspond to the best fit anymore? Can you see another way of computing the rms scatter by which the best fit would in fact correspond to the lowest scatter? Why do the biweight and rms scatter look similar now?

Finally, add a selection bias on x, such that x cannot be detected below 3. Repeat your fits and again discuss which fit appears most correct vs. is actually most correct.

## B. Best Predictions

All of the above assumed that the goal was to measure the true, underlying relationship between x and y.  What if your goal were instead to find the best predictive relation between the two, for example to predict y with greatest accuracy for a given x. How would the optimal choice of fit type change in this case? Hint: the best prediction fit y(x) would give the value of y at a given x about which we can expect symmetric scatter. Make a plot showing this fit with the final data set from part A (with selection bias etc.). Is the scatter symmetric around your fit at a given x?

To improve the symmetry of the scatter, we may wish to trim the data in x so that we fit only within a range of x where y shows symmetric scatter. Perform such a trimmed fit and compare with your previous results. Notice that the "best prediction" fit does not look like the underlying true relation -- why is this reasonable?

Sample answers are [here](https://github.com/capprogram/2017bootcamp-general/blob/master/fittingchoices.py).
