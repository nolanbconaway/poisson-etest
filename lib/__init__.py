"""Implement a two-sample poisson E-test."""
import scipy.stats
import math


def sqrt(x):
    """Compute the square root of a number, allowing negative/complex values."""
    return pow(x, 0.5)


def poisson_etest(
    k1: int, k2: int, n1: int, n2: int, alternative: str = "twosided"
) -> float:
    """Compute the probability two poisson samples are sampled from the same mean.

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
    elif (k1 + k2) == 0:
        raise ValueError("At least one k must be > 0.")

    if alternative not in ("greater", "twosided"):
        raise ValueError("Invalid tails. Must be in (greater, twosided).")
    elif alternative == "greater":
        side = 1
    elif alternative == "twosided":
        side = 2

    # enforce d=0 for now. this is due to issues with complex numbers downstream when
    # (mu0 - mu1) < d. In this case, nan is returned in the fortran code.
    d = 0

    elhatk = (k1 + k2) / (n1 + n2) - d * n1 / (n1 + n2)

    var = k1 / (n1 ** 2) + k2 / (n2 ** 2)
    t_k1k2 = (k1 / n1 - k2 / n2 - d) / sqrt(var)

    pvalue = 0
    elhat1 = n1 * (elhatk + d)
    elhat2 = n2 * elhatk
    i1mode = math.floor(elhat1)
    i2mode = math.floor(elhat2)

    pi1mode = scipy.stats.poisson.pmf(i1mode, elhat1)
    pi1 = pi1mode
    pi2mode = scipy.stats.poisson.pmf(i2mode, elhat2)

    def sumi2(iside, n1, n2, elhat2, t_k1k2, i1, pi1, i2mode, pi2mode, d, pvalue):
        """Replicate the performance of the MATLAB version of the poisson etest code.

        I do not know what this does exactly but first lets just replicate...
        """
        pi2 = pi2mode

        for i2 in range(i2mode, 1001):
            if pi2 < 1e-7:
                break

            elhati1 = i1 / n1
            elhati2 = i2 / n2
            diffi = elhati1 - elhati2 - d
            var = elhati1 / n1 + elhati2 / n2
            if iside == 1:
                if i1 / n1 - i2 / n2 <= d:
                    t_i1i2 = 0.0
                else:
                    t_i1i2 = diffi / sqrt(var)
                print(t_i1i2 - t_k1k2)
                if t_i1i2 >= t_k1k2:
                    pvalue = pvalue + pi1 * pi2

            elif iside == 2:
                if abs(i1 / n1 - i2 / n2) <= d:
                    t_i1i2 = 0.0
                else:
                    t_i1i2 = diffi / sqrt(var)

                if abs(t_i1i2) >= abs(t_k1k2):
                    pvalue = pvalue + pi1 * pi2

            pi2 = elhat2 * pi2 / (i2 + 1)

        i2 = i2mode - 1
        pi2 = i2mode * pi2mode / elhat2

        for i2 in range(i2mode)[::-1]:
            if pi2 < 1e-7:
                return pvalue

            elhati1 = i1 / n1
            elhati2 = i2 / n2
            diffi = elhati1 - elhati2 - d
            var = elhati1 / n1 + elhati2 / n2

            if iside == 1:
                if i1 / n1 - i2 / n2 <= d:
                    t_i1i2 = 0.0
                else:
                    t_i1i2 = diffi / sqrt(var)

                if t_i1i2 >= t_k1k2:
                    pvalue = pvalue + pi1 * pi2
            elif iside == 2:
                if abs(i1 / n1 - i2 / n2) <= d:
                    t_i1i2 = 0.0
                else:
                    t_i1i2 = diffi / sqrt(var)
                if abs(t_i1i2) >= abs(t_k1k2):
                    pvalue = pvalue + pi1 * pi2

            pi2 = i2 * pi2 / elhat2
        return pvalue

    for i1 in range(i1mode, 1000):
        if pi1 < 1e-7:
            break

        pvalue = sumi2(
            side, n1, n2, elhat2, t_k1k2, i1, pi1, i2mode, pi2mode, d, pvalue
        )
        pi1 = elhat1 * pi1 / (i1 + 1)

    i1 = i1mode - 1
    pi1 = i1mode * pi1mode / elhat1

    for i1 in range(i1mode)[::-1]:
        if pi1 < 1e-7:
            break

        pvalue = sumi2(
            side, n1, n2, elhat2, t_k1k2, i1, pi1, i2mode, pi2mode, d, pvalue
        )
        pi1 = i1 * pi1 / elhat1

    return pvalue
