import pytest

from poisson_etest import poisson_etest


# I copied these results from running the MATLAB code provided by
# https://github.com/leiferlab/testPoisson
@pytest.mark.parametrize(
    "test_args, expected",
    [
        [(0, 1, 1, 2, 1), 0.9999998928],
        [(0, 1, 1, 2, 2), 0.5101744518],
        [(0, 1, 1, 20, 1), 0.9999999266],
        [(0, 1, 1, 20, 2), 0.6042339404],
        [(0, 1, 10, 2, 1), 0.9999999533],
        [(0, 1, 10, 2, 2), 0.5517381704],
        [(0, 1, 10, 20, 1), 0.9999998928],
        [(0, 1, 10, 20, 2), 0.5101744518],
        [(0, 1, 5000, 2, 1), 0.9999999101],
        [(0, 1, 5000, 2, 2), 0.6318678816],
        [(0, 1, 5000, 20, 1), 0.999999882],
        [(0, 1, 5000, 20, 2), 0.6296178739],
        [(0, 10, 1, 2, 1), 0.9999998614],
        [(0, 10, 1, 2, 2), 0.004975386109],
        [(0, 10, 1, 20, 1), 0.9999998655],
        [(0, 10, 1, 20, 2), 0.2989368014],
        [(0, 10, 10, 2, 1), 0.9999999069],
        [(0, 10, 10, 2, 2), 0.06147899597],
        [(0, 10, 10, 20, 1), 0.9999998614],
        [(0, 10, 10, 20, 2), 0.004975386109],
        [(0, 10, 5000, 2, 1), 0.9999999102],
        [(0, 10, 5000, 2, 2), 0.5394087765],
        [(0, 10, 5000, 20, 1), 0.9999999259],
        [(0, 10, 5000, 20, 2), 0.5160991176],
        [(0, 100000, 1, 2, 1), 0.2484965922],
        [(0, 100000, 1, 2, 2), 0],
        [(0, 100000, 1, 20, 1), 0.2461441634],
        [(0, 100000, 1, 20, 2), 0],
        [(0, 100000, 10, 2, 1), 0.2479926353],
        [(0, 100000, 10, 2, 2), 0],
        [(0, 100000, 10, 20, 1), 0.2484965922],
        [(0, 100000, 10, 20, 2), 0],
        [(0, 100000, 5000, 2, 1), 0.4995522283],
        [(0, 100000, 5000, 2, 2), 0],
        [(0, 100000, 5000, 20, 1), 0.4988209711],
        [(0, 100000, 5000, 20, 2), 0],
        [(5, 1, 1, 2, 1), 0.008281185295],
        [(5, 1, 1, 2, 2), 0.08722807307],
        [(5, 1, 1, 20, 1), 8.236703444e-07],
        [(5, 1, 1, 20, 2), 0.5071601154],
        [(5, 1, 10, 2, 1), 0.9999999089],
        [(5, 1, 10, 2, 2), 0.9999999089],
        [(5, 1, 10, 20, 1), 0.008281185295],
        [(5, 1, 10, 20, 2), 0.08722807307],
        [(5, 1, 5000, 2, 1), 0.9999998979],
        [(5, 1, 5000, 2, 2), 0.9961954179],
        [(5, 1, 5000, 20, 1), 0.9999998928],
        [(5, 1, 5000, 20, 2), 0.9846732433],
        [(5, 10, 1, 2, 1), 0.9999998391],
        [(5, 10, 1, 2, 2), 0.9999998391],
        [(5, 10, 1, 20, 1), 0.0002166780385],
        [(5, 10, 1, 20, 2), 0.4890428768],
        [(5, 10, 10, 2, 1), 0.9999997956],
        [(5, 10, 10, 2, 2), 0.07660954201],
        [(5, 10, 10, 20, 1), 0.9999998391],
        [(5, 10, 10, 20, 2), 0.9999998391],
        [(5, 10, 5000, 2, 1), 0.9999999],
        [(5, 10, 5000, 2, 2), 0.9243908898],
        [(5, 10, 5000, 20, 1), 0.9999999354],
        [(5, 10, 5000, 20, 2), 0.8743419296],
        [(5, 100000, 1, 2, 1), 0.2493739875],
        [(5, 100000, 1, 2, 2), 0],
        [(5, 100000, 1, 20, 1), 0.2478542779],
        [(5, 100000, 1, 20, 2), 0],
        [(5, 100000, 10, 2, 1), 0.2481351455],
        [(5, 100000, 10, 2, 2), 0],
        [(5, 100000, 10, 20, 1), 0.2493739875],
        [(5, 100000, 10, 20, 2), 0],
        [(5, 100000, 5000, 2, 1), 0.4995547582],
        [(5, 100000, 5000, 2, 2), 0],
        [(5, 100000, 5000, 20, 1), 0.4988461751],
        [(5, 100000, 5000, 20, 2), 0],
        [(1000, 1, 1, 2, 1), 0],
        [(1000, 1, 1, 2, 2), 0],
        [(1000, 1, 1, 20, 1), 0],
        [(1000, 1, 1, 20, 2), 0],
        [(1000, 1, 10, 2, 1), 0],
        [(1000, 1, 10, 2, 2), 0],
        [(1000, 1, 10, 20, 1), 0],
        [(1000, 1, 10, 20, 2), 0],
        [(1000, 1, 5000, 2, 1), 0.5008435063],
        [(1000, 1, 5000, 2, 2), 0.5008435063],
        [(1000, 1, 5000, 20, 1), 0.01104976397],
        [(1000, 1, 5000, 20, 2), 0.01105231226],
        [(1000, 10, 1, 2, 1), 0],
        [(1000, 10, 1, 2, 2), 0],
        [(1000, 10, 1, 20, 1), 0],
        [(1000, 10, 1, 20, 2), 0],
        [(1000, 10, 10, 2, 1), 0],
        [(1000, 10, 10, 2, 2), 0],
        [(1000, 10, 10, 20, 1), 0],
        [(1000, 10, 10, 20, 2), 0],
        [(1000, 10, 5000, 2, 1), 0.488328822],
        [(1000, 10, 5000, 2, 2), 0.3260825409],
        [(1000, 10, 5000, 20, 1), 0.4835301254],
        [(1000, 10, 5000, 20, 2), 0.04725437545],
        [(1000, 100000, 1, 2, 1), 0.2483978974],
        [(1000, 100000, 1, 2, 2), 0],
        [(1000, 100000, 1, 20, 1), 0.2470150573],
        [(1000, 100000, 1, 20, 2), 0],
        [(1000, 100000, 10, 2, 1), 0.2482858337],
        [(1000, 100000, 10, 2, 2), 0],
        [(1000, 100000, 10, 20, 1), 0.2483978974],
        [(1000, 100000, 10, 20, 2), 0],
        [(1000, 100000, 5000, 2, 1), 0.4988008332],
        [(1000, 100000, 5000, 2, 2), 0],
        [(1000, 100000, 5000, 20, 1), 0.498806657],
        [(1000, 100000, 5000, 20, 2), 0],
    ],
)
def test_replicate_matlab_code(test_args, expected):
    kws = dict(zip(("k1", "k2", "n1", "n2", "alternative"), test_args))
    kws["alternative"] = "greater" if kws["alternative"] == 1 else "twosided"
    assert pytest.approx(expected, poisson_etest(**kws))


# I copied these results from manually running the original fortran. At first lets just
# make sure to replicate the original behavior, warts and all.
@pytest.mark.parametrize(
    "test_args, expected",
    [
        [(10000, 10000, 10000, 10000), 0.24866994128694545],
        [(20, 20, 10, 10), 0.99999975689296305],
        [(10, 10, 10, 10), 0.99999984032412026],
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


def test_valuerror_double_zero_k():
    with pytest.raises(ValueError):
        poisson_etest(0, 0, 10, 10)


def test_valuerror_invalid_alternative():
    with pytest.raises(ValueError):
        poisson_etest(10, 10, 10, 10, alternative="something")
