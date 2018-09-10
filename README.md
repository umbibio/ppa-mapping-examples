# ppa-mapping-examples
Example code for the use of Partitioning of Poisson Arrivals (PPA) mapping, for calculation of moments in general models of post-transcriptional regulation.

## Setup your environment

To use this code, you will need the package `sympy`, which is a python library for symbolic computation.

To install `sympy`:

``
$ pip install sympy
``

## List of examples

* [Example 01:](Example01_3step-senescence-single-mRNA-arrivals.ipynb)
3 step senescence. mRNA degradation occurs in 3 steps
* [Example 02:](Example02_N-step-senescence-burst-of-b-mRNA-arrivals.ipynb)
N step senescence. Here mRNAs may arrive in batches of `b` mRNA molecules in each arrival
* [Example 03:](Example03_2-step-NuclearRetention.ipynb)
2 step nuclear retention. In this model, each mRNA is first silent until it is exported to the cytoplasm
