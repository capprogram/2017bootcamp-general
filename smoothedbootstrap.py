"""
Smoothed Bootstrap Function
Author: Sheila Kannappan
adapted from astroML.resample.bootstrap September 2016
"""

import numpy as np
import numpy.random as npr
from astroML.utils import check_random_state

def smoothedbootstrap(data, n_bootstraps, user_statistic, kwargs=None,
              random_state=None):
    """Compute smoothed bootstrapped statistics of a data set.

    Parameters
    ----------
    data : array_like
        A 1-dimensional data array of size n_samples
    n_bootstraps : integer
        the number of bootstrap samples to compute.  Note that internally,
        two arrays of size (n_bootstraps, n_samples) will be allocated.
        For very large numbers of bootstraps, this can cause memory issues.
    user_statistic : function
        The statistic to be computed.  This should take an array of data
        of size (n_bootstraps, n_samples) and return the row-wise statistics
        of the data.
    kwargs : dictionary (optional)
        A dictionary of keyword arguments to be passed to the
        user_statistic function.
    random_state: RandomState or an int seed (0 by default)
        A random number generator instance

    Returns
    -------
    distribution : ndarray
        the bootstrapped distribution of statistics (length = n_bootstraps)
    """
    # we don't set kwargs={} by default in the argument list, because using
    # a mutable type as a default argument can lead to strange results
    if kwargs is None:
        kwargs = {}

    rng = check_random_state(random_state)

    data = np.asarray(data)
    n_datapts = data.size

    if data.ndim != 1:
        raise ValueError("bootstrap expects 1-dimensional data")

    # Generate random indices with repetition
    ind = rng.randint(n_datapts, size=(n_bootstraps, n_datapts))
    
    # smoothing noise
    noisemean = 0.
    noisesigma = np.std(data,ddof=1) / np.sqrt(n_datapts)
    noise = npr.normal(noisemean,noisesigma,(n_bootstraps, n_datapts))
    databroadcast = data[ind] + noise

    # Call the function
    stat_bootstrap = user_statistic(databroadcast, **kwargs)

    # compute the statistic on the data
    return stat_bootstrap
