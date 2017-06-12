# Parameter Estimation by Maximum Likelihood Model Fitting 

Most recent version by Sheila Kannappan June 2017, with major contributions from Kathleen Eckert, Rohan Isaac, and Amy Oldenberg.

**Why do we fit models to data?**

-   To understand the underlying distribution of the data
-   To test hypotheses or competing theoretical models
-   To predict values for future observations

In general, any of these goals will often involve _parameter estimation_. In this tutorial we will go through the basics of parameter estimation using frequentist "maximum likelihood" model fitting.

## Background: Least Squares Fitting

"Least squares" fitting is based on the assumption that all the measurement uncertainties &sigma; in a data set are the same, i.e., follow the same Gaussian distribution. In the case of a linear model, the least squares fit gives the slope & y-intercept parameters that minimize the mean square residuals between the data and the model, where the residuals are measured in the y-direction in the case of "forward" fitting. Here the mean square residuals are given by: <img src="https://latex.codecogs.com/png.latex?\mathrm{rms}^2=\frac{1}{N}\sum{\left(y_i-\left(\alpha&space;x_i&plus;\beta\right)\right&space;)^2}"/> where x<sub>i</sub> is the independent variable, y<sub>i</sub> is the dependent variable, and α and β are the slope and y-intercept parameter values. Minimizing the mean square residuals is equivalent to minimizing the rms (root mean square) residuals, and also equivalent to minimizing the &chi;<sup>2</sup>, because of the fact that all &sigma;'s have been assumed to be identical.

Least squares fitting falls within the broader category of parameter estimation known as *Maximum Likelihood Estimation* (MLE). In this method, we measure the likelihood for a given model, typically using the χ<sup>2</sup> statistic:

The likelihood is given by: <img src="https://latex.codecogs.com/png.latex?L=\exp{\frac{-\chi^2}{2}}"/> where <img src="https://latex.codecogs.com/png.latex?\chi^2=\sum\frac{\left(y_{value,i}-y_{model,i}\right)^2}{\sigma_i^2}"/>

To find the MLE solution to our model, we maximize the likelihood function by taking the derivative with respect to each parameter (the slope and y-intercept in the case of a linear fit) and by solving for where each derivative is equal to 0. To simplify the math, we first take the natural log of the likelihood function. For least squares fitting (wherein all &sigma; values are taken to be equal), it is possible to obtain an analytical solution for the slope and y-intercept of a linear model, as shown below.

### Derivation

Take the natural log of the likelihood function <img src="https://latex.codecogs.com/png.latex?\ln(L)=-\frac{1}{2}\chi^2=-\frac{1}{2}\sum\frac{\left(y_i-\left(\alpha&space;x_i&plus;\beta\right)\right&space;)^2}{\sigma_i^2}"/>

Take the derivatives of ln(L) with respect to α and β and set those equations to 0:
<img src="https://latex.codecogs.com/png.latex?\frac{d\ln(L)}{d\alpha}=-\sum\frac{\left(y_i-\left(\alpha&space;x_i&plus;\beta\right)\right)(-x_i)}{\sigma_i^2}=0"/> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; and &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <img src="https://latex.codecogs.com/png.latex?\frac{d\ln(L)}{d\beta}=-\sum\frac{\left(y_i-\left(\alpha&space;x_i&plus;\beta\right)\right)(-1)}{\sigma_i^2}=0"/> .

If we assume the σ<sub>i</sub>'s are all the same, then we have two equations for two unknowns to solve:

**eqn 1:** <img src="https://latex.codecogs.com/png.latex?\sum&space;y_i&space;x_i-\alpha\sum&space;x_i^2-\beta\sum&space;x_i=0"/> 

**eqn 2:** <img src="https://latex.codecogs.com/png.latex?\sum&space;y_i-\alpha\sum&space;x_i-N\beta=0"/> 

Multiply eqn 1 by N and multiply eqn 2 by <img src="https://latex.codecogs.com/png.latex?\sum&space;x_i"/> to get:

**eqn 1** <img src="https://latex.codecogs.com/png.latex?N\sum&space;y_i&space;x_i-N\alpha\sum&space;x_i^2-N\beta\sum&space;x_i=0"/> 

**eqn 2** <img src="https://latex.codecogs.com/png.latex?\sum&space;x_i\sum&space;y_i-\alpha\sum&space;x_i\sum&space;x_i-N\beta\sum&space;x_i=0"/> 

Now we can set these two equations equal to each other:

<img src="https://latex.codecogs.com/png.latex?N\sum&space;y_i&space;x_i-N\alpha\sum&space;x_i^2=\sum&space;x_i\sum&space;y_i-\alpha(\sum&space;x_i)^2"/>

Solving for α and dividing the top and bottom by N<sup>2</sup>:

<img src="https://latex.codecogs.com/png.latex?\alpha=\frac{\bar{x}\bar{y}-\bar{xy}}{\bar{x}^2-\bar{(x^2)}}"/>

where the bar over the variable signifies the mean value of that quantity.

Now we can go back and solve for β:

from **eqn 2** <img src="https://latex.codecogs.com/png.latex?\beta=\bar{y}-\alpha\bar{x}"/> 

____

For more complicated functions or if the uncertainties are not uniform, setting the derivatives of the likelihood equal to zero may not lead to equations that are so easily solved analytically. Thus for more complicated MLE problems we typically use programs such as `np.polyfit` or `mpfit` to determine parameters numerically.

## Tutorial:

Download [paramfit1.py](paramfit1.py). In this code we create fake data with random errors around a line of known slope and y-intercept. We then compute the maximum likelihood estimated slope and y-intercept for the fake data. Fill in lines ending with "?" and answer questions by putting your own comments in the code.

1) Run the program `paramfit1.py` and plot the data. What aspect of a real data set is `npr.normal` used to emulate? What assumption is made in the code that is key to the least squares approach?

2) Read over the derivation for the linear least squares analytical solution (above) and add code to compute the estimated slope and y-intercept based on the fake data set. Plot the maximum likelihood ("best fit") solution on top of the data.

3) For linear least squares fitting, we can obtain analytical formulae for the uncertainties on the slope
and y-intercept estimates, which have been provided below. (See http://mathworld.wolfram.com/LeastSquaresFitting.html for the full derivation.)<br><br>
<img src="https://latex.codecogs.com/png.latex?\sigma_\alpha=\sqrt{\frac{\sum\left(y_i-\left(\alpha&space;x_i&plus;\beta\right)\right&space;)^2}{(N-2)\sum(x_i-\bar{x})^2}}"/><br>
<img src="https://latex.codecogs.com/png.latex?\sigma_\beta=\sqrt{\left(\frac{\sum\left(y_i-\left(\alpha&space;x_i&plus;\beta\right)\right)^2}{N-2}\right)&space;\left(\frac{1}{N}+\frac{(\bar{x})^2}{\sum(x_i-\bar{x})^2}\right)}"/><br><br>
Uncomment the code to compute the uncertainties for the slope and y-intercept analytically. Which parameter has larger fractional
uncertainty?

4) Read up on [np.polyfit](http://docs.scipy.org/doc/numpy/reference/generated/numpy.polynomial.polynomial.polyfit.html) <br><br>
Use `np.polyfit` to compute the MLE slope and y-offset for the data set numerically rather than analytically. Do you get the same result as in the analytical case from #2 above?    
Note that in this example we have assumed that the &sigma; on all data points is the same. This simplified assumption is often not the case. If the uncertainties are different, then we must include each data point's uncertainty within the MLE calculation. Although `np.polyfit` does not automatically take an array of uncertainties on the y value, we can input an optional weight vector: `fit=np.polyfit(xvals, yvals, 1, w=1/sig)` where `sig` is an array containing the uncertainty on each data point. Here the input is `1/sig` rather than `1/sig**2` as you might expect from the equations above. The `np.polyfit` function squares the weight value within the source code.    

5) Now we'll compute the errors on the slope and intercept numerically, for comparison with the analytic calculation in #3. A quick method to determine uncertainties is to have `np.polyfit` compute the covariance matrix:
<img src="https://latex.codecogs.com/png.latex?C=\begin{pmatrix}\sigma_a^2&cov(\alpha,\beta)\\cov(\alpha,\beta)&\sigma_\beta^2\end{pmatrix}"/> which is the inverse of the Hessian Matrix, consisting of second derivatives of the log likelihood with respect to different model parameters. (When these matrices get tricky to compute, we can resort to a more approximate numerical technique such as the bootstrap.)
Add `cov="True"` to the `np.polyfit` function call so that `np.polyfit` will compute the covariance matrix numerically. Print out the uncertainties computed using the covariance matrix. Are they the same as found in the analytical solution? What happens to the uncertainties as you increase/decrease the number of data points? What happens to the _percentage difference_ between the analytical and numerical methods as you increase/decrease the number of data points?

Solutions to the tutorial are in [paramfit1_soln.py](paramfit1_soln.py).
