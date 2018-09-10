# ppa-mapping-examples
Example code for the use of Partitioning of Poisson Arrivals (PPA) mapping, for calculation of moments in general models of post-transcriptional regulation.

## Setup your environment

To use this code, you will need the package `sympy`, which is a python library for symbolic computation.

To install `sympy`:

``
$ pip install sympy
``

## List of examples

* [Example 01:](blob/master/Example01_3step-Senescense-single-mRNA-arrivals.ipynb)
3 step senescence. mRNA degradation occurs in 3 steps
* [Example 02:](blob/master/Example02_N-step-Senescense-burst-of-b-mRNA-arrivals.ipynb)
N step senescence. Here mRNAs may arrive in batches of `b` mRNA molecules in each arrival
* [Example 03:](blob/master/Example03_2-step-NuclearRetention)
2 step nuclear retention. In this model, each mRNA is first silent until it is exported to the cytoplasm
