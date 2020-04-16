import numpy as np
from scipy.signal import convolve as conv

def add(x_1, n_1, x_2, n_2):
    """Add two signals and return.

    Parameters:
    x_1: The first signal
    x_2: The second signal
    n_1: The time values of the first siganl
    n_2: n_1: The time values of the first siganl

    Returns:
    ndarray[float]: The sum of the two signals
    ndarray[int]: The time values of the sum signal
    """
    n = np.arange(min(np.min(n1), np.min(n2)), max(np.max(n1), np.max(n2)) + 1, 1)
    y_1 = np.zeros(n.size)
    y_2 = np.zeros(n.size)
    # numpy is stupid not me, I swear matlab does better here.
    temp1 = n >= np.min(n_1)
    temp2 = n <= np.max(n_1)
    y1[temp1 * temp2 == 1] = x_1
    temp1 = n >= np.min(n2)
    temp2 = n <= np.max(n2)
    y2[temp1 * temp2 == 1] = x_2
    #>
    x = y_1 + y_2
    x = x.astype('float')
    return x, n

def mul(x_1, n_1, x_2, n_2):
     """Multiply two signals and return.

    Parameters:
    x_1: The first signal
    x_2: The second signal
    n_1: The time values of the first siganl
    n_2: n_1: The time values of the first siganl

    Returns:
    ndarray[float]: The product of the two signals
    ndarray[int]: The time values of the product signal
    """
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
# x, n = mul(x1, n1, x2, n2)
# print(x)
# print(n)

def shift(x, n, k):
    """Shift a signal by k units.

    Parameters:
    x: The first signal
    n: The time value of the signal
    k: The amount shifted

    Returns:
    ndarray[float]: The shifted signal
    ndarray[int]: The time values of the shifted signal
    """
    n = n + k
    return x, n

# x1 = np.array([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0])
# n1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# x1, n1 = shift(x1, n1, 1)
# print(x1)
# print(n1)

def fold(x, n):
    """Fold the signal, i.e. reverse it.

    Parameters:
    x: The first signal
    n: The time value of the signal

    Returns:
    ndarray[float]: The sum of the folded signal
    ndarray[int]: The time values of the folded signal
    """
    return np.flip(x), -np.flip(n)

# x1 = np.array([0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0])
# n1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# x1, n1 = fold(x1, n1)
# print(x1)
# print(n1)

def convole(x_1, n_1, x_2, n_2):
    """Convolve two signals and return.

    Parameters:
    x_1: The first signal
    x_2: The second signal
    n_1: The time values of the first siganl
    n_2: n_1: The time values of the first siganl

    Returns:
    ndarray[float]: The result signal
    ndarray[int]: The time values of the result signal
    """
    left = n_1[0] + n_2[0]
    right = n_1[n_1.size-1] + n_2[n_1.size-1]
    n = np.arange(left, right+1, 1)
    x = conv(x_1, x_2)
    return x, n

# x1 = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
# n1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#
# x, n = convole(x1, n1, x1, n1)
# print(x)
# print(n)

def correlate(x_1, n_1, x_2, n_2):
    """Return the correlation of two signals

    Parameters:
    x_1: The first signal
    x_2: The second signal
    n_1: The time values of the first siganl
    n_2: n_1: The time values of the first siganl

    Returns:
    ndarray[float]: The result signal
    ndarray[int]: The time values of the result signal
    """
    x_2, n_2 = fold(x_2, n_2)
    x, n = convole(x_1, n_1, x_2, n_2)
    return x, n

def odd_even(x):
    """Return the odd and the even parts of the signal.

    Parameters:
    x: The input signal

    Returns:
    ndarray[float]: The odd part of the signal
    ndarray[float]: The even part of the signal
    """
    x_odd = 0.5 * (x - np.flip(x))
    x_even = 0.5 * (x + np.flip(x))
    return x_odd, x_even
