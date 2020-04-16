import numpy as np

def delta(n0, left, right):
    """Return the Dirac delta signal.

    Parameters:
    n0: Value for the impulse, i.e. where the signal value is 1
    left: Left bound of the signal
    right: Rright bound of the signal

    Returns:
    ndarray[float]: The values of the signal
    ndarray[int]: The interval of the signal from left bound
    to right bound
    """
    n = np.arange(left, right+1, 1)
    x = np.array((n - n0) == 0)
    x = x.astype('float')
    return x, n

def unit_step(n0, left, right):
    """Return the unit step signal.

    Parameters:
    n0: Where the signal starts having value 1
    left: Left bound of the signal
    right: Rright bound of the signal

    Returns:
    ndarray[float]: The values of the signal
    ndarray[int]: The interval of the signal from left bound
    to right bound
    """
    n = np.arange(left, right + 1, 1)
    x = np.array((n - n0) >= 0)
    x = x.astype('float')
    return x, n

def rectangle(n0, n1, left, reft):
    """Return the rectangle signal.

    Parameters:
    n0: Where the rectangle signal starts
    n1: Where the rectangle signal stops
    left: Left bound of the signal
    right: Rright bound of the signal

    Returns:
    ndarray[float]: The values of the signal
    ndarray[int]: The interval of the signal from left bound
    to right bound
    """
    n = np.arange(left, right+1, 1) 
    # numpy is stupid not me, I swear matlab does better here.
    temp1 = n - n0 >= 0
    temp2 = n1 - n >= 0
    x = np.array(temp1 * temp2)
    #>
    x = x.astype('float')
    return x, n

def exponential(mantissa, base, power, left, reft):
    """Return the exponential signal.

    The signal's value will be `mantissa * base ^ (power * time)`.

    Parameters:
    mantissa: The mantissa, i.e. the scale of the signal
    base: The exponential base
    power: The exponential power
    left: Left bound of the signal
    right: Rright bound of the signal

    Returns:
    ndarray[float]: The values of the signal
    ndarray[int]: The interval of the signal from left bound
    to right bound
    """
    n = np.arange(left, right+1, 1)
    x = mantissa * (base ** (power * n))
    return x, n

def complex_exponential(mantissa, phi, omega, lb, rb):
    """Return the exponential signal.

    The signal's value will be `mantissa * e^(phi + j * omega)`,
    where e is natural logarithm constant and j is the imaginary unit.

    Parameters:
    mantissa: The mantissa, i.e. the scale of the signal
    phi: The shifted phase of the complex signal
    omega: The angular component of the signal
    left: Left bound of the signal
    right: Rright bound of the signal

    Returns:
    ndarray[float]: The values of the signal
    ndarray[int]: The interval of the signal from left bound
    to right bound
    """
    n = np.arange(left, right+1, 1)
    x = mantissa * np.exp((phi + 1j * omega) * n)
    return x, n

def sin(amplitude, omega, phase, left, right):
    """Return a sinusoidal signal.

    Parameters:
    amplitude: The amplitude of the signal
    omega: The angular rate of the signal
    phase: The shifted phase of the signal
    left: Left bound of the signal
    right: Rright bound of the signal

    Returns:
    ndarray[float]: The values of the signal
    ndarray[int]: The interval of the signal from left bound
    to right bound
    """
    n = np.arange(left, right+1, 1)
    x = amplitude * np.sin(omega * n + phase)
    return x, n

def cos(A, w, p, lb, rb):
    """Return a cosinusoidal signal.

    Parameters:
    amplitude: The amplitude of the signal
    omega: The angular rate of the signal
    phase: The shifted phase of the signal
    left: Left bound of the signal
    right: Rright bound of the signal

    Returns:
    ndarray[float]: The values of the signal
    ndarray[int]: The interval of the signal from left bound
    to right bound
    """
    n = np.arange(left, right+1, 1)
    x = amplitude * np.cos(omega * n + phase)
    return x, n
