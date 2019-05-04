# Python Poisson E-Test

[![Build Status](https://travis-ci.org/nolanbconaway/poisson-etest.svg?branch=master)](https://travis-ci.org/nolanbconaway/poisson-etest)
[![PyPI version](https://badge.fury.io/py/poisson-etest.svg)](https://badge.fury.io/py/poisson-etest)

This library contains a function to compute a two-sample poisson E-test, as defined
in [Krishnamoorthy & Thomson (2004)](http://www.ucs.louisiana.edu/~kxk4695/JSPI-04.pdf).

## Installation & Usage

This library has no external dependencies. Just:

```sh
pip install poisson-etest
```

Test whether two samples of Poisson data were drawn from the same distribution.

```python
>>> from poisson_etest import poisson_etest
>>> sample1_k, sample1_n = 10, 20
>>> sample2_k, sample2_n = 15, 20
>>> poisson_etest(sample1_k, sample2_k, sample1_n, sample2_n)
0.33116214285801826
```

## Implementation Notes

Originally, I edited the [fortran code](http://www.ucs.louisiana.edu/~kxk4695/statcalc/pois2pval.for)
posted on Krishnamoorthy's website so that numpy could wrap it. You can look at the edits
in one of the early commits to this repo.

The fortran code as it stands has a few problems, but I figured it'd be worth getting an
implementation up. Here are some problems that I have noticed:

1. Floats not supported for `k` and `n` values.
2. Odd behavior with large numbers (I saw it at `k = n = 10000`).
3. Odd behavior at `k = 0`.
4. Odd behavior for some positive values of `d` (it can create complex numbers and then
  return NaN).

Later, I reimplemented in pure Python (no external deps!). That solved some problems but
not others:

1. *Solved*: float support for `k` and `n`.
2. *Solved*: large numbers handle just fine (I tested `k = n = 100000`).
3. *Kind of solved*: At least one k must be > 0, otherwise complex numbers are created
and exceptions are thrown downstream.
4. *Not solved*: Nonzero `d` still sometimes creates complex numbers. In the pure python
version an exception is later thrown, so I have disabled that option.
5. *New problem*: it's noticeably slower for large `k` and `n` values (think ~1000).
