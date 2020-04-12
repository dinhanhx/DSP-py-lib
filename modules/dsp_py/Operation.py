import numpy as np
from scipy.signal import convolve as conv

def Add(x1, n1, x2, n2):
    # x1 and n1 are illumination of first signal
    # x2 and n2 are illumination of second signal
    n = np.arange(min(np.min(n1), np.min(n2)), max(np.max(n1), np.max(n2)) + 1, 1)
    y1 = np.zeros(n.size)
    y2 = np.zeros(n.size)
    # numpy is stupid not me, I swear matlab does better here.
    temp1 = n >= np.min(n1)
    temp2 = n <= np.max(n1)
    y1[temp1 * temp2 == 1] = x1
    temp1 = n >= np.min(n2)
    temp2 = n <= np.max(n2)
    y2[temp1 * temp2 == 1] = x2
    #>
    x = y1 + y2
    x = x.astype('float')
    return x, n

def Mul(x1, n1, x2, n2):
    # x1 and n1 are illumination of first signal
    # x2 and n2 are illumination of second signal
    n = np.arange(min(np.min(n1), np.min(n2)), max(np.max(n1), np.max(n2)) + 1, 1)
    y1 = np.zeros(n.size)
    y2 = np.zeros(n.size)
    # numpy is stupid not me, I swear matlab does better here.
    temp1 = n >= np.min(n1)
    temp2 = n <= np.max(n1)
    y1[temp1 * temp2 == 1] = x1
    temp1 = n >= np.min(n2)
    temp2 = n <= np.max(n2)
    y2[temp1 * temp2 == 1] = x2
    #>
    x = y1 * y2
    x = x.astype('float')
    return x, n

# x1 = np.array([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0])
# n1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#
# x2 = np.array([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0])
# n2 = np.array([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#
# x, n = Mul(x1, n1, x2, n2)
# print(x)
# print(n)

def Shift(x1, n1, k):
    # x1 and n1 are illumination of first signal
    # y(n) = x(n-k)
    n = n1 + k
    return x1, n

# x1 = np.array([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0])
# n1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# x1, n1 = Shift(x1, n1, 1)
# print(x1)
# print(n1)

def Fold(x1, n1):
    # y(n) = x(-n)
    return np.flip(x1), -np.flip(n1)

# x1 = np.array([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0])
# n1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# x1, n1 = Fold(x1, n1)
# print(x1)
# print(n1)

def Convole(x1, n1, x2, n2):
    # x1 and n1 are illumination of first signal
    # x2 and n2 are illumination of second signal
    lb = n1[0] + n2[0]
    rb = n1[n1.size-1] + n2[n1.size-1]
    n = np.arange(lb, rb+1, 1)
    x = conv(x1, x2)
    return x, n

# x1 = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
# n1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#
# x, n = Convole(x1, n1, x1, n1)
# print(x)
# print(n)

def Correlate(x1, n1, x2, n2):
    x2, n2 = Fold(x2, n2)
    x, n = Convole(x1, n1, x2, n2)
    return x, n

def OddEvenSyn(x):
    x_odd = 0.5 * (x - np.flip(x))
    x_even = 0.5 * (x + np.flip(x))
    return x_odd, x_even
