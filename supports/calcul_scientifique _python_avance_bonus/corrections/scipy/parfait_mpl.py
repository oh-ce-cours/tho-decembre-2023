import matplotlib.pyplot as plt
import numpy as np

xs = np.linspace(-15, 15, 1000)
ys1 = 20 * np.sin(xs) / xs
ys2 = 10 * np.sinc(xs / 2)

for style in plt.style.available:
    plt.clf()
    plt.style.use(style)
    plt.plot(xs, ys1, label=r"$\frac{\sin(x)}{10 * x}$")
    plt.plot(xs, ys2, label=r"$\frac{\sin(x/10)}{x/10}$")
    plt.title(style)
    plt.legend()
    plt.xlabel("X")
    plt.ylabel("$f(x)$")
    plt.savefig("styles/{}.png".format(style))
