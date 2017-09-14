#Libraries
from scipy import signal # for signal processing
from pylab import *


# To filter the noise using the Hanning filter with a win_size size of the window
# win_size is the frequency of sensor values
def filtering(sig, win_size):
    win = signal.hann(win_size)
    win = map(lambda x: float(x), win)
    sig = map(lambda x: float(x), sig)
    win = list(win)
    sig = list(sig)

    filtered = signal.convolve(sig, win, mode='same') / sum(
        win)  # CHANGED THE sig[2:] to sig - to take the whole signal since I am deleting the first rows from EDA_Raw.csv
    return filtered


# To filter the noise using the Bartlett filter with a win_size size of the window
# win_size is the frequency of sensor values
def filtering_bartlett(sig, win_size):
    win = signal.bartlett(win_size)
    win = map(lambda x: float(x), win)
    sig = map(lambda x: float(x), sig)
    win = list(win)
    sig = list(sig)

    filtered = signal.convolve(sig, win, mode='same') / sum(win)
    return filtered


# To filter the noise using the Fourier Transform
def filtering_fir(sig):
    win = signal.firwin(33, 0.4, window='hamming', )  # 32nd+1 order, cutoff frequency
    win = map(lambda x: float(x), win)
    sig = map(lambda x: float(x), sig)

    win = list(win)
    sig = list(sig)

    filt = signal.convolve(sig, win, mode='same') / sum(win)

    return filt


# Smooth function from SciPy cookbook using Bartlett window
def smooth(x, window_len, window):
    """smooth the data using a window with requested size.

    This method is based on the convolution of a scaled window with the signal.
    The signal is prepared by introducing reflected copies of the signal
    (with the window size) in both ends so that transient parts are minimized
    in the begining and end part of the output signal.

    input:
        x: the input signal
        window_len: the dimension of the smoothing window; should be an odd integer
        window: the type of window from 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'
            flat window will produce a moving average smoothing.

    output:
        the smoothed signal

    example:

    t=linspace(-2,2,0.1)
    x=sin(t)+randn(len(t))*0.1
    y=smooth(x)

    see also:

    numpy.hanning, numpy.hamming, numpy.bartlett, numpy.blackman, numpy.convolve
    scipy.signal.lfilter

    TODO: the window parameter could be the window itself if an array instead of a string
    NOTE: length(output) != length(input), to correct this: return y[(window_len/2-1):-(window_len/2)] instead of just y.
    """

    if x.ndim != 1:
        raise ValueError("smooth only accepts 1 dimension arrays.")

    if x.size < window_len:
        raise ValueError("Input vector needs to be bigger than window size.")

    if window_len < 3:
        return x

    if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
        raise ValueError("Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'")

    s = np.r_[x[window_len - 1:0:-1], x, x[-2:-window_len - 1:-1]]
    # print(len(s))
    if window == 'flat':  # moving average
        w = np.ones(window_len, 'd')
    else:
        w = eval('np.' + window + '(window_len)')

    y = np.convolve(w / w.sum(), s, mode='valid')
    return y
