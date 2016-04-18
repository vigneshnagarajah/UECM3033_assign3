import numpy as np
import sympy as sy
import numpy.polynomial.legendre as npl


# DO NOT CHANGE THE NAME OF gausslegendre() function
def gausslegendre(f, a, b, n=20):
    ans = 0
    
    x, w = npl.leggauss(n)
    t=0.5*(x+1)*(b-a)+a
    
    
    ans=sum(w*f(t))*0.5*(b-a)
    
    
    return ans

if __name__ == "__main__":
    def f(x):
        return (x**2 +7*x)/(1 +np.sqrt(x))**4
    
    def my_integral():
        x = sy.Symbol('x')
        ans = sy.integrate((x**2 +7*x)/(1 +sy.sqrt(x))**4, (x,0, 1))
        return ans
    
    print('Answer:                    I = ', my_integral())
    print('Your implementation gives: I = ', gausslegendre(f, 0,1))