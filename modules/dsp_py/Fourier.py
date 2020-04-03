import numpy as np

def DTFT(x, n, range, num):
    # x and n are representation of signal in time domain
    # range = [lbw, rbw] of w (omega)
    # num is number of equispaced points from lbw to rbw
    lbw = range[0]
    rbw = range[1]
    stepw = (rbw - lbw)/(num - 1)
    w = np.arange(lbr, rbw+stepw, stepw)
    X = x * np.exp(1j * n.transpose() * w)
    return X, w

def FreqRespDE(x_coeff, y_coeff, range, num):
    # Frequency Response from Difference Equation
    # range = [lbw, rbw] of w (omega)
    # num is number of equispaced points from lbw to rbw
    lbw = range[0]
    rbw = range[1]
    stepw = (rbw - lbw)/(num - 1)
    w = np.arange(lbr, rbw+stepw, stepw)
    m = np.arange(0, x_coeff.size-1, 1)
    l = np.arange(0, y_coeff.size-1, 1)
    numerator = x_coeff * np.exp(1j * m.transpose() * w)
    denominator = y_coeff * np.exp(1j * l.transpose() * w)
    H = numerator/denominator
    return H, w
