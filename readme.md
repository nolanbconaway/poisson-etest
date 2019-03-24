# Python Poisson E-Test

[![Build Status](https://travis-ci.org/nolanbconaway/poisson-etest.svg?branch=master)](https://travis-ci.org/nolanbconaway/poisson-etest)
[![PyPI version](https://badge.fury.io/py/poisson-etest.svg)](https://badge.fury.io/py/poisson-etest)

This library contains a function to compute a two-sample poisson E-test, as defined
in [Krishnamoorthy & Thomson (2004)](http://www.ucs.louisiana.edu/~kxk4695/JSPI-04.pdf). I simply  edited the [fortran code](http://www.ucs.louisiana.edu/~kxk4695/statcalc/pois2pval.for) posted on Krishnamoorthy's website so that numpy could wrap it. You can look at the edits in one of the early commits to this repo.

The code as it stands has a few problems, but I figured it'd be worth getting a direct implementation up. Here are some problems that I have noticed:

1. Floats not supported for `k` and `n` values.
2. Odd behavior with large numbers (I saw it at `k = n = 10000`).
3. Odd behavior at `k = 0`.

One day I'll fix these issues by reimplementing in pure python, assuming that doesn't also require a big hit in efficiency.

## Install

```sh
pip install poisson-etest
```
## Usage

Test whether two samples of Poisson data were drawn from the same distribution.

```python
>>> from poisson_etest import poisson_etest
>>> sample1_k, sample1_n = 10, 20
>>> sample2_k, sample2_n = 15, 20
>>> poisson_etest(sample1_k, sample2_k, sample1_n, sample2_n)
0.33116214285801826
```
