#Python Libraries
For this tutorial, we are going to outline the most common uses for each of the following libraries:

**Numpy** is a library for working with arrays of data.

**Scipy** is a library of techniques for numerical and scientific computing.

**Matplotlib** is a library for making visualizations.

**Seaborn** is a higher-level interface to Matplotlib that can be used to simplify many visualization tasks.

**Important**: While this tutorial provides insight into the basics of these libraries, I recommend digging into the
documentation that is available online.


#NumPy
NumPy is the fundamental package for scientific computing with Python. It contains among other things:

a powerful N-dimensional array object
sophisticated (broadcasting) functions
tools for integrating C/C++ and Fortran code
useful linear algebra, Fourier transform, and random number capabilities
We will focus on the numpy array object.

##Numpy Array
A numpy array is a grid of values, all of the same type, and is indexed by a tuple of nonnegative integers.
The number of dimensions is the rank of the array; the shape of an array is a tuple of integers giving the size
of the array along each dimension.

#SciPy
Numpy provides a high-performance multidimensional array and basic tools to compute with and manipulate these arrays. SciPy builds on this, and provides a large number of functions that operate on numpy arrays and are useful for different types of scientific and engineering applications.

For this course, we will primariyl be using the SciPy.Stats sub-library.

##SciPy.Stats
The SciPy.Stats module contains a large number of probability distributions as well as a growing library of statistical functions such as:

Continuous and Discrete Distributions (i.e Normal, Uniform, Binomial, etc.)

Descriptive Statistcs

Statistical Tests (i.e T-Test)

#MatPlotLib
Matplotlib is a plotting library. In this section give a brief introduction to the matplotlib.pyplot module.

##Seaborn
Seaborn is complimentary to Matplotlib and it specifically targets statistical data visualization. But it goes even further than that: Seaborn extends Matplotlib and makes generating visualizations convenient.

While Matplotlib is a robust solution for various problems, Seaborn utilizes more concise paramesters for ease-of-use.