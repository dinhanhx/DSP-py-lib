import numpy as np

def dtzt(x, n, interval_w, num_w, interval_r, num_r):
    """Return the discrete-time z-transform of a signal.

    Parameters:
    x: The signal
    n: The time values of input siganl in time domain
    interval_w: The interval of the signal in z domain
    num_w: The number of equispaced points in `interval_w
    interval_r: The radius of the signal in z domain
    num_r: The number of equispaced points in `interval_r`

    Returns:
    ndarray[float]: The signal in frequency domain
    ndarray[int]: The frequency values of signal in frequency domain
    """
    left_w = interval_w[0]
    right_w = interval_w[1]
    step_w = (right_w - left_w)/(num_w - 1)
    w = np.arange(left_w, right_w+step_w, step_w)

    left_r = interval_r[0]
    right_r = interval_r[1]
    step_r = (right_r - left_r)/(num_r - 1)
    r = np.arange(left_r, right_r+step_r, step_r)

    X = np.zeros(r.size, w.size)
    for r_i in range(r.size):
        X[r_i,:] = (x * ((r[r_i]) ** (-1 * n))) * exp(-1j * n.T * w)


    return X, w, r

def zrde(x_coeff, y_coeff, interval_w, num_w, interval_r, num_r):
    """Return the z response from differential equation.

    Parameters:
    x: The first signal
    y: The second signal
    interval_w: The interval of the signal in z domain
    num_w: The number of equispaced points in `interval_w
    interval_r: The radius of the signal in z domain
    num_r: The number of equispaced points in `interval_r`

    Returns:
    ndarray[float]: The signal in z domain
    ndarray[int]: The frequency values of signal in z domain
    """
    left_w = interval_w[0]
    right_w = interval_w[1]
    step_w = (right_w - left_w)/(num_w - 1)
    w = np.arange(left_w, right_w + step_w, step_w)

    left_r = interval_r[0]
    right_r = interval_r[1]
    step_r = (right_r - left_r)/(num_r - 1)
    r = np.arange(left_r, right_r+step_r, step_r)

    m = np.arange(0, x_coeff.size-1, 1)
    l = np.arange(0, y_coeff.size-1, 1)

    H = np.zeros(r.size, w.size)
    for r_i in range(r.size):
        numerator = (x_coeff * ((r[r_i]) ** (-1 * m))) * exp(-1j * m.T * w)
        denominator = (y_coeff * ((r[r_i]) ** (-1 * l))) * exp(-1j * l.T * w)
        H[r_i,:] = numerator / denominator;


    return H, w, r
