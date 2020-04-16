import numpy as np

def dtft(x, n, interval, num):
    """Return the discrete-time Fourier transform of a signal.

    Parameters:
    x: The signal
    n: The time values of input siganl in time domain
    interval: The interval of the signal in frequency domain
    num: The number of equispaced points in `interval`

    Returns:
    ndarray[float]: The signal in frequency domain
    ndarray[int]: The frequency values of signal in frequency domain
    """
    left_w = interval[0]
    right_w = interval[1]
    step_w = (right_w - left_w)/(num - 1)
    w = np.arange(left_w, right_w + step_w, step_w)
    X = x * np.exp(1j * n.T * w)
    return X, w

def frde(x_coeff, y_coeff, interval, num):
    """Return the frequency response from differential equation.

    Parameters:
    x: The first signal
    y: The second signal
    interval: The interval of the signal in frequency domain
    num: The number of equispaced points in `interval`

    Returns:
    ndarray[float]: The signal in frequency domain
    ndarray[int]: The frequency values of signal in frequency domain
    """
    left_w = interval[0]
    right_w = interval[1]
    step_w = (right_w - left_w)/(num - 1)
    w = np.arange(left_r, right_w + step_w, step_w)
    m = np.arange(0, x_coeff.size-1, 1)
    l = np.arange(0, y_coeff.size-1, 1)
    numerator = x_coeff * np.exp(1j * m.T * w)
    denominator = y_coeff * np.exp(1j * l.T * w)
    H = numerator/denominator
    return H, w
