import numpy as np
from colorama import init
from colorama import Fore

init()  # This is for Windows

def fill(x, n):
    # Add meaningful zeros to x
    # Also expand n till n == 0
    x_type = x.dtype
    n_type = n.dtype
    if 0 in n:
        return x, n
    else:
        if np.amax(n) > 0:
            subn = np.arange(0, n[0])
            n = np.concatenate((subn, n), axis = None)
            subx = np.zeros(subn.size)
            x = np.concatenate((subx, x), axis = None)
        else:
            subn = np.arange(n[-1]+1, 1)
            n = np.concatenate((n, subn), axis = None)
            subx = np.zeros(subn.size)
            x = np.concatenate((x, subx), axis = None)

    return x.astype(x_type), n.astype(n_type)

def print_signal(x, n):
    x, n = fill(x, n) # make sure the signal has meaningful zeros
    # Print x and x(0) is colored green
    zero_pos = int(np.where(n == 0)[0])
    s = '['
    for i in range(x.size):
        if i == zero_pos:
            s = s + Fore.GREEN + str(x[i]) + Fore.WHITE + ' '
        else:
            s = s + str(x[i]) + ' '


    s = s[:-1]
    s = s + ']'
    print(s)
    return ''


# x = np.array([1, 1, 1])
# n = np.array([2, 3, 4])
#
# print_signal(x, n)
#
# x, n = fill(x, n)
