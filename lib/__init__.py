"""Implement a two-sample poisson E-test."""

from .poisson_etest_fortran import two_sample_poisson


def poisson_etest(
    k1: int, k2: int, n1: int, n2: int, alternative: str = "twosided", d: float = 0.0
) -> float:
    """Conduct a two_sample_poisson test.

    Parameters
    ----------
    k1 : int
        Count of the first sample.
    k2 : int
        Count of the second sample.
    n1 : int
        Size of the first sample.
    n2 : int
        Size of the second sample.
    alternative : {'twosided', 'greater'}
        Alternative hypothesis. Default "twosided"
    d : float
        The difference of mu1 - mu2 under the null hypothesis.

    Returns
    -------
    float
        P-value of the unconditional test.

    Examples
    --------
    >>> from poisson_etest import poisson_etest
    >>> poisson_etest(20, 20, 10, 10)
    0.99999975689296305
    >>> poisson_etest(100, 10, 10, 100)
    2.6904995792779108e-005

    """
    # handle argument values. These copied from the original fortran code.
    if min(n1, n2) <= 0:
        raise ValueError("n must be > 0.")

    if min(k1, k2) < 0:
        raise ValueError("k must be >= 0.")

    if alternative not in ("greater", "twosided"):
        raise ValueError("Invalid tails. Must be in (greater, twosided).")
    elif alternative == "greater":
        side = 1
    elif alternative == "twosided":
        side = 2

    if d < 0:
        raise ValueError("d must be  >= 0.")

    return two_sample_poisson(k1, k2, n1, n2, side, d)
