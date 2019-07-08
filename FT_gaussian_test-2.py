%matplotlib inline
from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt

# T = 1./800
f_c = 1e5
Q = 0.01
A = 10.
sigma = 2*np.pi*f_c/Q

# N = 1000 # number of points
#
# t = np.linspace(0.0,N*T,N)

# sineGaussian = A/(np.sqrt(2*np.pi)*sigma)*np.exp(-(t-f_c)**2/(2*sigma**2))*np.sin(2*np.pi*f_c*t)



from scipy.fftpack import fft

# Number of sample points
N = int(1e4)
# sample spacing
T = 1e-6
x = np.linspace(1.0, N*T, N)
y = A/(np.sqrt(2*np.pi)*sigma)*np.exp(-(x-f_c)**2/(2*sigma**2))*np.sin(2*np.pi*f_c*x) #np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)

plt.plot(x,y)
plt.show()

yf = np.fft.fft(y)
xf = np.linspace(0.0, 1.0/(2*T), N//2)
import matplotlib.pyplot as plt
plt.loglog(xf, 2.0/N * np.sqrt(2./T) * np.abs(yf[0:N//2]))
# plt.grid()
plt.show()
