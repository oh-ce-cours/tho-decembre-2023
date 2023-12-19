import scipy
from scipy import fftpack
import numpy as np
import matplotlib.pyplot as plt

xs = np.linspace(-10, 100, 50000)

pi_2 = 2 * np.pi
ys = np.cos(pi_2 * xs) + np.cos(pi_2 * 100 * xs)

f = fftpack.fft(ys)
freqs = fftpack.fftfreq(xs.size, xs[1] - xs[0])

plt.plot(freqs, f.real); plt.show()



# passe bande
bw_filter = np.zeros(freqs.shape)
bw_filter[np.abs(freqs) > 20] = 1.0
plt.plot(bw_filter)
plt.show()

f *= bw_filter
plt.plot(freqs, f.real); plt.show()

ys2 = fftpack.ifft(f)

plt.plot(ys2[::100], label="Defiltré")
plt.plot(ys[::100], label="original")
plt.legend()
plt.show()
