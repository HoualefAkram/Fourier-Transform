import cmath
import matplotlib.pyplot as plt


def FFT(P: list[int]):
    n = len(P)
    print(n)
    if n == 1:
        return P
    w = cmath.exp((2j * cmath.pi) / n)
    Pe, Po = [P[i] for i in range(0, n, 2)], [P[i] for i in range(1, n, 2)]
    ye, yo = FFT(Pe), FFT(Po)
    y = [0] * n
    for j in range(n // 2):
        y[j] = ye[j] + (w**j) * yo[j]
        y[j + n // 2] = ye[j] - (w**j) * yo[j]
    return y


# FFT
def fft(signal):
    N = len(signal)

    if N <= 1:
        return signal

    even = fft(signal[0::2])
    odd = fft(signal[1::2])

    T = [cmath.exp(-2j * cmath.pi * k / N) * odd[k] for k in range(N // 2)]

    return [even[k] + T[k] for k in range(N // 2)] + [
        even[k] - T[k] for k in range(N // 2)
    ]


# Generate x values from -2π to 2π
x = [i * (4 * cmath.pi / 256) - 2 * cmath.pi for i in range(256)]
# Generate cos(2 * x) values (change frequency here)
signal = [cmath.cos(2 * val) for val in x]

# Compute FFT
fft_result = fft(signal)

# Compute frequency axis manually
N = len(signal)
freq = [(i - N // 2) * (1 / (4 * cmath.pi / N)) for i in range(N)]

# Shift FFT result for correct plotting
fft_result_shifted = fft_result[N // 2 :] + fft_result[: N // 2]

# Plot the original signal
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot([val.real for val in x], [val.real for val in signal])
plt.title("Original Signal: cos(2x)")
plt.xlabel("x")
plt.ylabel("cos(2x)")

# Plot the FFT result (magnitude)
plt.subplot(1, 2, 2)
plt.plot(freq, [abs(val) for val in fft_result_shifted])
plt.title("FFT of cos(2x)")
plt.xlabel("Frequency")
plt.ylabel("Magnitude")

plt.tight_layout()
plt.show()
