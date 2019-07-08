# Reference code: https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html

%matplotlib inline
import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
# Number of sample points

f_c=1e5
Q = 50
A = 1e-25
Gamma = 2*np.pi*f_c/Q**2
# number of sample points
N = 1000
# sample spacing
T = 1./800

t = np.linspace(-N*T, N*T, N) #N*T
sineGaussian = A*np.exp(-Gamma*t**2)*np.sin(2*np.pi*f_c*t)

plt.plot(t, sineGaussian)
plt.xlabel('time (s)')
plt.ylabel('h(t)')
plt.title('Time Series of sine-Gaussian')
plt.savefig('time_series-1.png',dpi=150)
plt.show()

ASD = fft(sineGaussian)
freq = np.logspace(0.0, 10, N//2)

memory = 1e-23*freq**(-1/2)
memory[np.where(freq > (f_c-(f_c/Q)))] = 0


plt.loglog(freq, np.abs(ASD[0:N//2]), label = 'sine-Gaussian')
plt.loglog(freq[np.where(memory != 0)], memory[np.where(memory != 0)], label = 'memory')
plt.loglog(freq, memory+np.abs(ASD[0:N//2]), label = 'memory + sine-Gaussian')
plt.xlabel('frequency (Hz)')
plt.ylabel('$S^{1/2}_h (f)$ (Hz$^{-1/2}$)')
plt.title('McNeill Figure 3')
plt.ylim(1e-28,1e-18)
plt.legend()
plt.axvline(f_c-(f_c/Q), color = 'orange', linestyle = '--')
plt.savefig('test-FT-2.png', dpi=150)
# plt.grid()
plt.show()
