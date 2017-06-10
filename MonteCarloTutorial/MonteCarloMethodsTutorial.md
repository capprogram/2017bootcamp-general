# Monte Carlo Methods

### Sheila Kannappan

> _&quot;Monte Carlo methods&quot; is a term covering pretty much any use of pseudo-randomness to help solve any kind of problem._ – Niall O&#39;Higgins

Copy all &quot;.py&quot; files in https://github.com/capprogram/2017bootcamp-general/tree/master/MonteCarloTutorial to your own working space – these files include partial answers to the exercises below, left incomplete for you to finish. Select exercises have solutions provided with a &quot;.solns&quot; extension. You should perform this tutorial in Anaconda under Linux, Mac, or Windows.

# I. Random Number Generators

There are two ways to generate random numbers:

- physical measurements that are expected to be random (e.g., coin flips)
- computational algorithms that produce long sequences of apparently random results, in fact completely determined by an initial &quot;seed&quot; value

The latter are often called _pseudo-random_ number generators.

Look over the description of the &quot;random&quot; package for python here: [http://docs.python.org/2/library/random.html](http://docs.python.org/2/library/random.html)

Check out the Mersenne Twister on the internet – it&#39;s not an amusement park ride!

**Exercise 1:** Use _random.random_ to generate a variable x consisting of 10 random numbers between 0 and 1. Repeat to create a second random variable y, and plot x and y against each other. Verify that there is no correlation.

**Exercise 2:** Use _random.seed_ to control the random numbers in x and y such that they are identical. Plot x and y against each other and verify that there is a perfect correlation.

**Exercise 3:** Use _random.gauss_ to generate a variable u (for &quot;uncertainty&quot;) consisting of 1000 random numbers with mean zero and standard deviation &sigma; = 1. Create a histogram of the values to verify that they look like a Gaussian distribution <img src="https://latex.codecogs.com/png.latex?\frac{1}{\sigma\sqrt{2\pi}}\exp{\left(-\frac{u^2}{2\sigma^2}&space;\right&space;)}" />
.

![](https://github.com/capprogram/2017bootcamp-general/blob/master/MonteCarloTutorial/gaussianconfidenceintervals.png)

The Gaussian distribution is the most commonly used model for random uncertainties (non-systematic errors/noise) in data.  In particular:

1. The error bars on data values are typically set to equal the expected &plusmn;1&sigma; variations due to random measurement errors/noise _(caveat: some research fields use &plusmn;2&sigma; error bars)_

2. The signal-to-noise (S/N) ratios for data values representing &quot;detections&quot; are typically given in terms of the background noise (i.e., S/N=3 means S=3&sigma; (caveat: if the signal is extended in time/space/&lambda;/etc., it is really a sum of several data points and you must use error propagation rules)

From the diagram, we see a S/N&gt;3 "detection" has only 0.1% probability of occurring by chance, so people generally say a measurement at S/N=3 is detected &quot;at 99.9% confidence.&quot; (Strictly speaking this is incorrect; see reading on the p-value crisis.)

For data values, the error bars are referred to as &quot;confidence intervals.&quot; From the diagram, &plusmn;1&sigma; corresponds to a &quot;68% confidence interval.&quot;

_Recall that the python package &quot;numpy&quot; enables array math. The solutions to Exercises 3 &amp; 4 illustrate some of what you can do with numpy._

Import numpy and use it to compute and overplot the expected Gaussian function shape on top of the histogram you made.

**Exercise 4:** Use numpy to convert u into an array and use numpy&#39;s _where_ function to determine what percentage of the time the variable u lies inside &plusmn;1&sigma;. If you have an array of data with error bars equal to u, how often should the fit line go through the error bars?

## II. Areas or Volumes of Enclosed Regions

A basic application of random number generation is in measuring the areas or volumes of enclosed regions, especially non-rectangular regions for which a direct measurement would be difficult. The method is to choose points randomly in a rectangular region enclosing the region of interest, then find the fraction of the points that land inside the region of interest in order to assess its subarea/subvolume.

**Exercise 1:** Use _random.uniform_ to measure the area of a circle with radius 1 and thus to measure the value of &pi;. How many darts do you need to get a good, consistent estimate?

**Exercise 2:** Use numpy&#39;s array version of random to measure the area under the Gaussian from -1&sigma; to +1&sigma;. Think about why this area is equal to the percentage of u values between &plusmn;1&sigma; even though u was created with _random.gauss_.

## III. Random Selection from a Non-Uniform Distribution

It may happen that you want to select random numbers from a distribution of your own. For example, suppose we want the distribution of radius values for a set of points drawn randomly from within a circle as shown below.

The probability of a point having a given radius increases with the area of the annulus that radius lies in, so <img src="https://latex.codecogs.com/png.latex?\inline&space;p(r)dr=\frac{2\pi&space;rdr}{\pi&space;R^2}" />where R is the radius of the circle. (Note that the integral <img src="https://latex.codecogs.com/png.latex?\inline&space;\int_0^Rp(r)dr=1" /> as is required for a probability distribution.) The trick to computing the (non-uniform) probability distribution for _r_ is to map values _x_ from a uniform distribution [0, 1] onto the values of _r_ in such a way that the correct frequency of values is produced. A one-to-one mapping in which the _integrated_ probability out to _r_ in [0, R] is equal to the integrated probability out to _x_ in [0, 1] does the trick. In &quot;inverse transform sampling,&quot; we first generate values using a uniform random number generator, then map them to values drawn from another probability distribution using this integral mapping.

![](https://github.com/capprogram/2017bootcamp-general/blob/master/MonteCarloTutorial/randomdotsincircle.png)

**Exercise 1:** First, use numpy&#39;s version of _random_ to select radii randomly in a circle by inverse transform sampling. Second, compare the distribution of radii selected by this method to the distribution of radii obtained by selecting &quot;hits&quot; in a circle as in Exercise 1 from Part II. (Note – the second task requires that you generate a new block of code, not just tweak the code provided. You should try to find bits of earlier code that you can copy/imitate/modify to make an array of radii, then plot the new radii in a histogram on top of a histogram of the original radii.) How do the histograms compare? Explain.

**Exercise 2:** Use numpy&#39;s version of _random_ to select values from a Gaussian distribution using inverse transform sampling. In this exercise you are essentially recreating _random.gauss_. Hint: the integral of a Gaussian function centered on 0 is

<img src="https://latex.codecogs.com/png.latex?\int_{-\infty}^u\frac{1}{\sigma\sqrt{2\pi}}\exp{\left(-\frac{u^2}{2\sigma^2}\right)}du=0.5+0.5&space;erf(u/\sqrt{2})" />

You can import &quot;erf&quot; from scipy.special.

## IV. For Further Inquiry

Random number generation is useful in many contexts. For example, you may wish to generate mock data sets with realistic scatter to test algorithms. Simulated data play an important role in planning and testing experiments.

[http://www.ligo.org/news/blind-injection.php](http://www.ligo.org/news/blind-injection.php)

Another technique that relies on Monte Carlo methods is &quot;bootstrapping,&quot; actually a family of techniques all of which use random resampling of a real data set to estimate the uncertainties on parameters or model fits characterizing that data set. We'll return to bootstrapping in another tutorial.

[http://en.wikipedia.org/wiki/Bootstrapping\_%28statistics%29](http://en.wikipedia.org/wiki/Bootstrapping_%28statistics%29)
