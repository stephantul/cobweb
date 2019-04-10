# cobweb

This is some code for generating [cobweb plots](https://en.wikipedia.org/wiki/Cobweb_plot) or, alternatively, [verhulst](https://en.wikipedia.org/wiki/Pierre_Fran%C3%A7ois_Verhulst) diagrams

Cobweb plots show the time-course of a 1-dimensional recursive function over time by plotting the trajectory of the output of the function as it is applied to itself.

# example

In the function, we use the well-known [logistic map](https://en.wikipedia.org/wiki/Logistic_map).
The logistic map exhibits chaotic behavior for most values `r > 3.56995`.

```python
from matplotlib import pyplot as plt
from cobweb import cobweb_plot

def logistic_map(x, r=3.14):
    return x * (1 - x) * r

if __name__ == "__main__":

    xt, func_plot, lin_plot = cobweb_plot(logistic_map,
                                          x0=.2,
                                          domain=(0, 1.0),
                                          num_iter=500)

    plt.plot(*xt, color='red')
    plt.plot(*func_plot, color='black')
    plt.plot(*lin_plot, color='black')
```
