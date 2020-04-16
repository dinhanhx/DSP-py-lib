import numpy as np

def dtft(x, n, interval, num):
    # x and n are representation of signal in time domain
    # interval = [lbw, rbw] of w (omega)
    # num is number of equispaced points from lbw to rbw
    lbw = interval[0]
    rbw = interval[1]
    stepw = (rbw - lbw)/(num - 1)
    w = np.arange(lbw, rbw+stepw, stepw)
    X = x * np.exp(1j * n.T * w)
    return X, w

def frde(x_coeff, y_coeff, interval, num):
    # Frequency Response from Difference Equation
    # range = [lbw, rbw] of w (omega)
    # num is number of equispaced points from lbw to rbw
    lbw = interval[0]
    rbw = interval[1]
    stepw = (rbw - lbw)/(num - 1)
    w = np.arange(lbr, rbw+stepw, stepw)
    m = np.arange(0, x_coeff.size-1, 1)
    l = np.arange(0, y_coeff.size-1, 1)
    numerator = x_coeff * np.exp(1j * m.T * w)
    denominator = y_coeff * np.exp(1j * l.T * w)
    H = numerator/denominator
    return H, w
