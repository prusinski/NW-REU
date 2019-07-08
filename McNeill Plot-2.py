%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-10,10,1000)
# x = np.linspace(-10,10)
A = 1 #1e-19
f_c = 0.1 #6e4
Q = 2 #4.5

Gamma = 1 #2*np.pi*f_c/(Q**2)

sineGaussian = np.sin(50.0 * 2.0*np.pi*t) + 0.5*np.sin(80.0 * 2.0*np.pi*t) #A*np.exp(-Gamma*t**2) #np.sin(2*np.pi*f_c*t)
plt.plot(t,sineGaussian, 'o')
plt.show()

frequency = np.fft.fft(sineGaussian)
plt.plot(t,frequency)
plt.show()


# t = np.logspace(0,10,1000)
# omega = 2
# G = 2*np.pi*f_c/Q
# print(G)
# fcn = np.exp(-G*t**2)
# plt.loglog(t,fcn)
# plt.show()


# print(f_c-(f_c/Q))

# memory = 1e-23*f**(-1/2)
# memory[np.where(f > (f_c-(f_c/Q)))] = 0
#
# plt.loglog(f, sineGaussian, label = 'sine-Gaussian')
# plt.loglog(f[np.where(memory != 0)], memory[np.where(memory != 0)], label = 'memory')
# plt.loglog(f, memory+sineGaussian, label = 'memory + sine-Gaussian')
# plt.ylim(1e-28,1e-18)
# plt.legend()
# plt.axvline(f_c-(f_c/Q), color = 'orange', linestyle = '--')
# plt.xlabel('frequency (Hz)')
# plt.ylabel('$S^{1/2}_h (f)$ (Hz$^{-1/2}$)')
# plt.title('McNeill Figure 3')
# plt.savefig('McNeill Plot-2.png', dpi=150)
# plt.show()
