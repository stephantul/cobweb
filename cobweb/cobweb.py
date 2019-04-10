import numpy as np


def cobweb_plot(function,
                x0=.2,
                num_iter=500,
                precision=.001):
    """
    Generate the cobweb plot for a given function.

    Parameters
    ----------
    function : callable
        A function that takes as input a single number and returns a single
        number. The domain and codomain of the functions are assumed to be
        the same.
    x0 : float, default .2
        The first value used as input to the function.
    num_iter : int, default 500
        The number of iterations to run over.
    precision : float, default 1e-3
        The interval with which to probe the function for plotting the function
        graph. The actual number of intervals probed is:
        (max - min) / precision
        If your function is expensive to evaluate, lower the precision.

    Returns
    -------
    iterates : list
        The points indicating the function trajectory.
    func_out : list
        The points indicating the function.
    lin_out : list
        The points indicating the horizontal line.

    """
    # Starting iterate
    ix = [x0]
    iy = [0]
    x = x0
    for _ in range(num_iter):
        xt = function(x)
        ix.extend([x, xt])
        iy.extend([xt, xt])
        x = xt

    low, high = np.min([ix, iy]), np.max([ix, iy])
    low = min(low, 0)
    high = max(high, 1.0)
    # Create function graph
    over_domain = np.arange(low, high, precision)
    iy[0] = low
    lin_out = list(zip(*[(x, x) for x in over_domain]))
    func_out = list(zip(*[(x, function(x)) for x in over_domain]))

    return (ix, iy), func_out, lin_out
