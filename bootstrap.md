# Bootstrapping Tutorial
by Sheila Kannappan and Rohan Isaac

Bootstrapping can be used to estimate uncertainties in any kind of statistic by recalculating it repeatedly with the input data set resampled each time (with replacement, so [2, 7, 8, 4, 11] could become [7, 11, 11, 4, 2]). In what follows we will see bootstrapping used to measure (i) the uncertainty in a correlation test result, (ii) the uncertainty in the standard deviation of a data set, and (iii) the uncertainty in a fitted parameter. Consult Section 4.5 of the Ivezic et al. textbook for further discussion on both the bootstrap and the jackknife, a less common alternative.

## Part I: Method Analysis

Download the python code to generate Figures 3.24 and 4.3 in the book. Each of these figures uses bootstrapping, but Fig. 3.24 does not use the AstroML bootstrap function (astroML.resample.bootstrap) and instead constructs the bootstrap manually.

1. Find the source code for `astroML.resample.bootstrap` (the function used in Fig. 4.3) and explain its methodology compared to the methodology in the code for Fig. 3.24. [CAREFUL: The code uses a variable name `n_samples` that is misleading -- this variable really represents the number of data points. In fact `n_bootstraps` is the number of samples that will be drawn from the n_samples data points.] Why is it not possible to use `astroML.resample.bootstrap` in the code for Fig. 3.24?

2. The code for Fig. 3.24 contains some sloppy coding that we have encouraged you to avoid. Download and revise it to follow better coding principles. (You may wish to reduce the number of iterations while testing it, and you can remove the pickle decorator.) At this point you may be tempted (as your instructors were) to try to reduce the amount of looping in the code to speed it up. Why does this code require a loop for the actual bootstrap calculation although `astroML.resample.bootstrap` has no loops?

## Part II: The Smoothed Bootstrap

Bootstrapping can be unreliable for small samples. Let's explore how to obtain a more reliable estimate of &sigma; for a small sample, using "smoothed bootstrapping."

1. Construct an initial random sample of 5 points drawn from a Gaussian with mean = 0 and &sigma; = 1. Compare the directly computed &sigma; for this sample from `np.std` to the input ("true") &sigma; as well as to the &sigma; found using `astroML.resample.bootstrap` with `np.std`. (GOTCHA: Read the documentation for `np.std` to set the parameter ddof properly -- the default value is not the preferred one. You also may need to specify an axis for np.std, because np.std flattens arrays by default.) Bootstrapping outputs an entire distribution of values (one for each bootstrap iteration) so you can think of the median value as the &sigma; estimate and the 16th and 84th percentiles as bounding the 68% confidence interval. Perform 1000 runs with 5 different starting data points each time, and perform 2000 bootstrap resamples of the 5 data points within each run. Plot histograms to look at how the 2000 bootstrapped values from np.std vary within a run and how the median values vary over all 1000 runs.

2. Using the discussion in section 2 of [Hesterberg (2004)](https://github.com/galastrostats/general/blob/master/JSM04-bootknife.pdf) and modeling your code on `astroML.resample.bootstrap`, construct a utility code called `smoothedbootstrap`. Test your smoothedbootstrap code on the sample from question 1 to determine whether it performs better than the ordinary bootstrap at recovering &sigma;. Plot the distributions and ratios of the various &sigma; estimates to compare them. If the residual bias in the smoothed bootstrap (and in the usual standard deviation) bothers you, visit [this page](https://en.wikipedia.org/wiki/Unbiased_estimation_of_standard_deviation).    

Note that Hesterberg introduces a hybrid of the bootstrap and the jackknife called the "bootknife" as well.

## Part III: Errors in Fitted Parameters

Revisit your code from the [tutorial on parameter estimation by maximum likelihood fitting](https://github.com/capprogram/2017bootcamp-general/blob/master/frequentist_paramfitting_tutorial.md), in which we computed errors on the slope and intercept of a line fit using both a pure analytic solution and a numerical estimate based on the Hessian matrix. Augment the code to obtain bootstrap estimates of the slope and intercept uncertainties and compare these with your analytic and Hessian matrix results.


Here are some codes you can compare your work with:    
[modified code for Fig. 3.24](https://github.com/capprogram/2017bootcamp-general/blob/master/fig3.24.mod.py)    
[smoothed bootstrap utility code](https://github.com/capprogram/2017bootcamp-general/blob/master/smoothedbootstrap.py)    
[&sigma; comparison code](https://github.com/capprogram/2017bootcamp-general/blob/master/sigmatests.py)    
[bootstrapped line fitting code](https://github.com/capprogram/2017bootcamp-general/blob/master/paramfit1_boot.py)    
