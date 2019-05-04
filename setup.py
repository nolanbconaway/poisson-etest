from setuptools import setup, find_packages

long_description = """
A function implementing the Poisson E-Test, described in this paper:

http://www.ucs.louisiana.edu/~kxk4695/JSPI-04.pdf
"""

install_requires = []
test_requires = ["pytest"] + install_requires

if __name__ == "__main__":

    setup(
        name="poisson_etest",
        version="0.01",
        url="https://github.com/nolanbconaway/poisson-etest",
        packages=["poisson_etest"],
        author="Nolan Conaway",
        author_email="nolanbconaway@gmail.com",
        description="A poisson e-test.",
        keywords=["poisson", "hypothesis testing", "statistics"],
        long_description=long_description,
        package_dir={"poisson_etest": "lib"},
        install_requires=install_requires,
        extras_require={"test": test_requires},
    )
