import pytest

from poisson_etest import poisson_etest


# I copied these results from manually running the original fortran. At first lets just
# make sure to replicate the original behavior, warts and all.
@pytest.mark.parametrize(
    "test_args, expected",
    [
        [(10000, 10000, 10000, 10000), 0.24866994128694545],
        [(20, 20, 10, 10), 0.99999975689296305],
        [(10, 10, 10, 10), 0.99999984032412026],
        [(0, 0, 1, 1), 0.00],
        [(100, 10, 10, 100), 2.6904995792779108e-005],
    ],
)
def test_replicate_original_fortan_code(test_args, expected):
    assert pytest.approx(expected, poisson_etest(*test_args))


def test_valuerror_0_n():
    with pytest.raises(ValueError):
        poisson_etest(10, 10, 0, 10)


def test_valuerror_negative_k():
    with pytest.raises(ValueError):
        poisson_etest(10, -10, 10, 10)


def test_valuerror_invalid_alternative():
    with pytest.raises(ValueError):
        poisson_etest(10, 10, 10, 10, alternative="something")


def test_valuerror_negative_d():
    with pytest.raises(ValueError):
        poisson_etest(10, 10, 10, 10, d=-1)
