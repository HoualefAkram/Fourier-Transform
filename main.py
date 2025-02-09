from matplotlib import pyplot as plt
from cmath import exp, cos, pi


def linspace(start, end, items):
    if items == 1:
        return [start]
    step = (end - start) / (items - 1)
    return [start + i * step for i in range(items)]


def DFT(P):
    output = []
    N = len(P)
    for k in range(N):
        Fk = 0
        for n in range(N):
            Fk += P[n] * exp(-(2j * pi * k * n) / N)
        output.append(Fk)
    return output


def fftshift(arr):
    N = len(arr)
    half = N // 2
    left = arr[half:]
    right = arr[:half]
    return left + right


# number of sampling points
N = 5012

# interval of sampling (starting from 0)
T = 5
t_line = linspace(0, T, N)

# sampling time
Ts = T / (N - 1)
# sampling frequency
Fs = 1 / Ts
print(f"Fs = {Fs}")
# cosine frequency
F = 20
y = [cos(2 * pi * F * t) for t in t_line]


f_line = linspace(-Fs / 2, Fs / 2, len(t_line))
fourier = DFT(y)
fourier_magnitude = [abs(f) for f in fourier]
fourier_shifted = fftshift(fourier_magnitude)

plt.subplot(2, 1, 1)
plt.plot(t_line, y)
plt.subplot(2, 1, 2)
plt.plot(f_line, fourier_shifted)
plt.show()
