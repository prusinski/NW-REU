%matplotlib inline
from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt

T = 3000.
f_c = 150
Q = 1.
A = 10.
sigma = 2*np.pi*f_c/Q

N = 100 # number of points

t = np.linspace(-T,T,N)

sineGaussian = A/(np.sqrt(2*np.pi)*sigma)*np.exp(-(t-f_c)**2/(2*sigma**2))*np.sin(2*np.pi*f_c*t)

plt.plot(t,sineGaussian)
plt.show()

freq = np.logspace(1,10,N//2+1)
out = np.fft.rfft(sineGaussian)
normalization = (2./N)*1./np.sqrt(T) # rfft gives N/2 points so A/N/2 = 2/N
plt.loglog(freq,normalization*np.abs(out))
plt.show()
