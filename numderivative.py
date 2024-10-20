import numpy as np
import matplotlib.pyplot as plt

def fourthorderfirstdegreederivative(x,h):
    """
    Calculate the first derivative of a signal using a 4th order polynomial
    """
    y = np.zeros(len(x))
    for i in range(2, len(x)-2):
        y[i] = (1*x[i-2] - 8*x[i-1] + 8*x[i+1] - x[i+2])/(12*h)

    if len(x) >= 4:
        y[0] = (-3*x[0] + 4*x[1] - x[2])/(2*h)
        y[1] = (-2*x[0] - 3 * x[1] + 6 * x[2] - x[3])/(6*h)
        y[-1] = (3*x[-1] - 4*x[-2] + x[-3])/(2*h)
        y[-2] = (2*x[-1] + 3*x[-2] - 6*x[-3] + x[-4])/(6*h)

    elif 2 <= len(x) & len(x) < 4:
        y[0] = (x[1] - x[0])/(h)
        y[-1] = (x[-1] - x[-2])/(h)
        if len(x) == 3:
            y[1] = (x[2] - x[1])/(h)
    else:
        y[0] = 0
    return y

def derivative_coefficients(n, n_start):
    taylor_table = np.zeros((n+1,n+1))
    for i in range(n+1):
        for j in range(n+1):
            taylor_table[i,j] = ((n_start + j)**i)/np.math.factorial(i)
    rhs_vec = np.zeros((n+1, 1))
    rhs_vec[1] = 1
    return np.linalg.solve(taylor_table, rhs_vec)

def jthderivative_coefficients(n, j, n_start):
    taylor_table = np.zeros((n+1,n+1))
    for i in range(n+1):
        for j in range(n+1):
            taylor_table[i,j] = ((n_start + j)**i)/np.math.factorial(i)
    rhs_vec = np.zeros((n+1, 1))
    rhs_vec[j] = 1
    return np.linalg.solve(taylor_table, rhs_vec)
def nthorderfirstdegreenumderivative(n,x,h):

    y = np.zeros(len(x))
    for i in range((n//2), (len(x)-n//2 - (n % 2))):
        a = derivative_coefficients(n, -n//2)
        y[i] = np.matmul(a.T, x[i-n//2:i+n//2 + (n % 2) + 1])/h

    if len(x) >= n:
        a_array = [] #np.zeros((n // 2, 1))
        a2_array = [] # np.zeros((n // 2 + (n % 2), 1))
        for i in range(n//2):
            a_array.append(derivative_coefficients(n//2 + (n % 2) + i, -i))
            y[i] = np.matmul(a_array[i].T, x[0:n//2 + (n % 2) + i + 1])/h
            a2_array.append(derivative_coefficients(n//2  + i, -(n//2) - i ))
            y[-1-i] = np.matmul(a2_array[i].T, x[-(n//2) - i - 1:])/h

        if (n % 2) == 1:
            a2_array.append(derivative_coefficients(n - 1 , -(n//2)))
            y[-(n//2)-1] = np.matmul(a2_array[-1].T, x[-n:])/h
    else:
        y = nthorderfirstdegreenumderivative(len(x), x, h)

    return y
def nthorderjthdegreenumderivative(n,j, x,h):

    y = np.zeros(len(x))
    for i in range((n//2), (len(x)-n//2 - (n % 2))):
        a = jthderivative_coefficients(n, j, -n//2)
        y[i] = np.matmul(a.T, x[i-n//2:i+n//2 + (n % 2) + 1])/h

    if len(x) >= n:
        a_array = [] #np.zeros((n // 2, 1))
        a2_array = [] # np.zeros((n // 2 + (n % 2), 1))
        for i in range(n//2):
            a_array.append(derivative_coefficients(n//2 + (n % 2) + i, -i))
            y[i] = np.matmul(a_array[i].T, x[0:n//2 + (n % 2) + i + 1])/h
            a2_array.append(derivative_coefficients(n//2  + i, -(n//2) - i ))
            y[-1-i] = np.matmul(a2_array[i].T, x[-(n//2) - i - 1:])/h

        if (n % 2) == 1:
            a2_array.append(derivative_coefficients(n - 1 , -(n//2)))
            y[-(n//2)-1] = np.matmul(a2_array[-1].T, x[-n:])/h
    else:
        y = nthorderfirstdegreenumderivative(len(x), x, h)

    return y
