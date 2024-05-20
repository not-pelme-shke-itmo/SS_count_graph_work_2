import matplotlib.pyplot as plt
import numpy as np

f = lambda x, k: k * x / (1 - k)

plt.style.use('_mpl-gallery')

def clamp(x):
    return min(max(x, -5), 5)

def binsearch(f1, f2):
    def func(x, epsilon):
        return round(f1(x) - f2(x), epsilon)

    l = -100
    r = 100
    epsilon = 15
    while True:
        m = (r - l) / 2 + l
        value = func(m, epsilon)
        if value > 0:
            r = m
        elif value < 0:
            l = m
        else:
            break

    return m

fig, ax = plt.subplots()

ax.autoscale_view(False, False)

for k in range(-10, 10):
    x = np.linspace(-5, 5, 100)
    y = f(x, k)
    ax.plot(x, y, 'b', linestyle='dashed')

for k in map(lambda x: x / 10, range(0, 7)):
    x = np.linspace(-5, 5, 100)
    y = f(x, k)
    ax.plot(x, y, 'b', linestyle='dashed')

x = np.linspace(-5, 5, 100)
ax.plot(0 * x, x, 'b', linestyle='dashed')

for x_0, color in [(-1, 'orange'), (1, 'orange'), (2, 'red'), (-2, 'red'), (3, 'yellow'), (-3, 'yellow')]:
    old_x_0 = x_0
    step = 0.4
    start_k = -100
    y_0 = f(x_0, start_k * step)

    for k in map(lambda x: x * step, range(start_k, 100)):
        prev_k = k - step
        new_k = k + step
        if k == 0 or new_k == 0 or 1 - k == 0 or 1 - new_k == 0:
            continue
        line = lambda x: k * (x - x_0) + y_0
        # intersect_point = (k**2 * x_0 - y_0 * k) / (k * k + k + 1)
        intersect_point = (k * new_k * x_0 - k * x_0 - y_0 * new_k + y_0) / (k * new_k + new_k - k)

        x = np.linspace(clamp(x_0), clamp(intersect_point), 100)

        y = line(x)
        ax.plot(x, y, color=color)
        x_0 = intersect_point
        y_0 = f(x_0, new_k)

    x_0 = old_x_0
    start_k = 100
    y_0 = f(x_0, start_k * step)

    for k in map(lambda x: x * step, range(start_k, 4, -1)):
        new_k = k - step
        if k == 0 or new_k == 0 or 1 - k == 0 or 1 - new_k == 0:
            continue
        line = lambda x: k * (x - x_0) + y_0
        # k'x / (1 - k') = k(x - x0) + y0
        intersect_point = (k * new_k * x_0 - k * x_0 - y_0 * new_k + y_0) / (k * new_k + new_k - k)

        x = np.linspace(clamp(x_0), clamp(intersect_point), 100)

        y = line(x)
        ax.plot(x, y, color=color)
        x_0 = intersect_point
        y_0 = f(x_0, new_k)



plt.show()
