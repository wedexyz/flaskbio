import scipy.signal
from scipy import signal


## filtering
low = 7/100
high = 13/100
pole = 2
samp_freq = 200 
notch_freq = 60.0  
quality_factor = 100.0 

def filters (chanel,pole,low,high):
    b_notch, a_notch = signal.iirnotch(notch_freq, quality_factor, samp_freq)
    dn = signal.filtfilt(b_notch, a_notch, chanel)
    b, a = scipy.signal.butter(pole, [low, high], 'band')
    df = scipy.signal.lfilter(b, a, dn)
  
    return df