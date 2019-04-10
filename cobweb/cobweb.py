import numpy as np


def cobweb_plot(function,
                x0=.2,
                domain=(0, 1.0),
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
    domain : tuple of two floats, default (0, 1.0)
        The closed interval specifying the domain of the function you want to
        visualize.
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
    low, high = domain
    # Create function graph
    over_domain = np.arange(*domain, precision)
    lin_out = list(zip(*[(x, x) for x in over_domain]))
    func_out = list(zip(*[(x, function(x)) for x in over_domain]))
    # Starting iterate
    ix = [x0]
    iy = [low]
    x = x0
    for _ in range(num_iter):
        xt = function(x)
        ix.extend([x, xt])
        iy.extend([xt, xt])
        x = xt

    return (ix, iy), func_out, lin_out
