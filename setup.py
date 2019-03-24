from numpy.distutils.core import Extension

long_description = """
A numpy binding for the Poisson E-Test, described in this paper:

http://www.ucs.louisiana.edu/~kxk4695/JSPI-04.pdf

I basically just minimally edited the original fortran code so that numpy f2py
could pick it up. The original code can be found in an early commit to this repo
or via this link:

http://www.ucs.louisiana.edu/~kxk4695/statcalc/pois2pval.for
"""

fortran_ext = Extension(
    "poisson_etest.poisson_etest_fortran", sources=["lib/poisson_etest.f"]
)

if __name__ == "__main__":
    from numpy.distutils.core import setup

    setup(
        name="poisson_etest",
        version="0.0",
        url="https://github.com/nolanbconaway/poisson-etest",
        packages=["poisson_etest"],
        author="Nolan Conaway",
        author_email="nolanbconaway@gmail.com",
        description="A poisson e-test.",
        keywords=["poisson", "hypothesis testing", "statistics"],
        long_description=long_description,
        ext_modules=[fortran_ext],
        package_dir={"poisson_etest": "lib"},
    )
