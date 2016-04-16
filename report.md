UECM3033 Assignment #3 Report
========================================================

- Prepared by: **Lem Wei Hao**
- Tutorial Group: T2

--------------------------------------------------------

## Task 1 --  Gauss-Legendre formula

The reports, codes and supporting documents are to be uploaded to Github at: 

[https://github.com/weihaolem/UECM3033_assign3](https://github.com/your_github_id/UECM3033_assign3)


Explain how you implement your `task1.py` here.

**In task1, I defined a function called gausslegendre() with four parameter which is integral function, lower boudary, upper boundary, and number of sample set in size 20. The function is based on the general form of a Gauss-Legendre quadrature formula:**
	![equation](https://c5.staticflickr.com/2/1612/26189413220_1df700541e.jpg)

**At the result, we are compare the exact value of integral function and Gauss-Legendre quadrature method.**

Explain how you get the weights and nodes used in the Gauss-Legendre quadrature.

**Using built-in module** `numpy.polynomial.legendre.leggauss(deg)` **to produce the value of x and w which is sample points(nodes) and its weights. The result can be tested up to 100, higher degree might lead to problematic.**

---------------------------------------------------------

## Task 2 -- Predator-prey model

Explain how you implement your `task2.py` here, especially how to use `odeint`.


Put your graphs here and explain.

Is the system of ODE sensitive to initial condition? Explain.

-----------------------------------

<sup>last modified: change your date here</sup>
