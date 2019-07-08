# Reference code: https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html

%matplotlib inline
import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
# Number of sample points

f_c=3e5
Q = 100
A = 1e-25
Gamma = 2*np.pi*f_c/Q**2

N = 1000
# sample spacing
freq_range = 1/2000
T = N*freq_range
t = np.linspace(0.0, T, N)
sineGaussian = A*np.exp(-Gamma*t**2)*np.sin(2*np.pi*f_c*t)
ASD = fft(sineGaussian)
freq = np.logspace(0.0, 10, N//2)

plt.loglog(freq, np.abs(ASD[0:N//2]))
plt.xlabel('frequency (Hz)')
plt.ylabel('$S^{1/2}_h (f)$ (Hz$^{-1/2}$)')
plt.title('McNeill Figure 3')
plt.ylim(1e-28,1e-18)
# plt.savefig('test-FT-1.png', dpi=150)
# plt.grid()
plt.show()
