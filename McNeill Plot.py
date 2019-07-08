%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

f = np.logspace(0,10,1000)
# x = np.linspace(-10,10)
A = 1e-19
f_c = 6e4
Q = 4.5

sineGaussian = A/2*np.sqrt(Q**2/(2*np.pi*f_c**2))*np.exp(-Q**2/2*((f-f_c)/f_c)**2)

# t = np.logspace(0,10,1000)
# omega = 2
# G = 2*np.pi*f_c/Q
# print(G)
# fcn = np.exp(-G*t**2)
# plt.loglog(t,fcn)
# plt.show()


# print(f_c-(f_c/Q))

memory = 1e-23*f**(-1/2)
memory[np.where(f > (f_c-(f_c/Q)))] = 0

plt.loglog(f, sineGaussian, label = 'sine-Gaussian')
plt.loglog(f[np.where(memory != 0)], memory[np.where(memory != 0)], label = 'memory')
plt.loglog(f, memory+sineGaussian, label = 'memory + sine-Gaussian')
plt.ylim(1e-28,1e-18)
plt.legend()
plt.axvline(f_c-(f_c/Q), color = 'orange', linestyle = '--')
plt.xlabel('frequency (Hz)')
plt.ylabel('$S^{1/2}_h (f)$ (Hz$^{-1/2}$)')
plt.title('McNeill Figure 3')
plt.savefig('McNeill Plot-1.png', dpi=150)
plt.show()
