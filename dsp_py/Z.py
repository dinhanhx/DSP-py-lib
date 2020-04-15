import numpy as np

def DTZT(x, n, intervalW, numW, intervalR, numR):
    # x and n are representation of signal in time domain
    # intervalW = [lbw, rbw] of w (omega)
    # numW is number of equispaced points from lbw to rbw
    # intervalR = [lbr, rbr] of r (radius)
    # numR is number of equispaced points from lbr to rbr
    # DTZT is more general than DTFT
    lbw = intervalW[0]
    rbw = intervalW[1]
    stepw = (rbw - lbw)/(numW - 1)
    w = np.arange(lbw, rbw+stepw, stepw)

    lbr = intervalR[0]
    rbr = intervalR[1]
    stepr = (rbr - lbr)/(numR - 1)
    r = np.arange(lbr, rbr+stepr, stepr)

    X = np.zeros(r.size, w.size)
    for r_i in range(r.size):
        X[r_i,:] = (x * ((r[r_i]) ** (-1 * n))) * exp(-1j * n.T * w)


    return X, w, r

def ZRespDE(x_coeff, y_coeff, intervalW, numW, intervalR, numR):
    # Z Respone from Difference Equation
    # intervalW = [lbw, rbw] of w (omega)
    # numW is number of equispaced points from lbw to rbw
    # intervalR = [lbr, rbr] of r (radius)
    # numR is number of equispaced points from lbr to rbr
    lbw = intervalW[0]
    rbw = intervalW[1]
    stepw = (rbw - lbw)/(numW - 1)
    w = np.arange(lbw, rbw+stepw, stepw)

    lbr = intervalR[0]
    rbr = intervalR[1]
    stepr = (rbr - lbr)/(numR - 1)
    r = np.arange(lbr, rbr+stepr, stepr)

    m = np.arange(0, x_coeff.size-1, 1)
    l = np.arange(0, y_coeff.size-1, 1)

    H = np.zeros(r.size, w.size)
    for r_i in range(r.size):
        numerator = (x_coeff * ((r[r_i]) ** (-1 * m))) * exp(-1j * m.T * w)
        denominator = (y_coeff * ((r[r_i]) ** (-1 * l))) * exp(-1j * l.T * w)
        H[r_i,:] = numerator / denominator;


    return H, w, r
