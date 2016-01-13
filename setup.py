from setuptools import setup

setup(
    name="parsec_wsdb",
    version=0.1,
    author="Simon Gibbons",
    author_email="sljg2@ast.cam.ac.uk",
    packages=['parsec_wsdb'],
    install_requires=['astropy', 'atpy', 'numpy', 'pygresql']
)
