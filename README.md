# Numerical Geophysical Fluid Dynamics

I will use this project space to explore numerical geophysical fluid dynamics (GFD) concepts. This has always been the most fascinating subject to me, and I've often wondered about the utility of using numerical models to teach GFD concepts. I need to explore best practices and re-learn a lot of these concepts myself, but I think this can be a great educational tool.

## Ramping Up

In the `ramping_up` directory, I've created notebooks covering some basic concepts before starting to build more complicated models. The notebooks are:

1. Simple Cosine Wave - how to simulate a simple cosine wave in Python
2. Advection of a Cosine Wave - how to apply the advection model to a cosine wave in Python
3. Modularized Advection of a Cosine Wave - simple repackaging of the previous section into a class structure to show how we can modularize the code
4. Upwind Scheme - applying the upwind differencing scheme to the advection of a cosine wave

## Shallow Water

In the `shallow_water` directory, I've created notebooks that gradually build in complexity of the [shallow water equations](https://en.wikipedia.org/wiki/Shallow_water_equations). A lot of this code is developed from [code I found on GitHub](https://github.com/jostbr/shallow-water) from user "jostbr". The notebooks are:

1. Basic SWE - Shallow water equations modeled with no rotation, no shear, and no friction, and no other complications (e.g., flat floor)
2. Adding Coriolis - Same as basic SWE but with rotation now included 