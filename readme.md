# poisson-etest

This library contains a function to compute a two-sample poisson E-test, as defined
in [Krishnamoorthy & Thomson (2004)](http://www.ucs.louisiana.edu/~kxk4695/JSPI-04.pdf).

I basically minimally edited the [fortran code](http://www.ucs.louisiana.edu/~kxk4695/statcalc/pois2pval.for) posted on Krishnamoorthy's website so that numpy could wrap it.

The code has a few problems, but i figured it'd be worth getting an intact version up. here are the problems that I have found:

1. Floats not supported.
2. Odd behavior with large numbers (I saw it at k = n = 10000).
3. Odd behavior at k=0.

One day I plan on fixing these issues and putting it in pure python, assuming that doesn't also require a bit hit in efficiency.
