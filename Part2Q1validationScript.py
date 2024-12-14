import numpy as np
import matplotlib.pyplot as plt
from Part2Q1 import downsample_signal

sampling_interval = 0.01 
frequency = 5 
duration = 1
t = np.arange(0, duration, sampling_interval)
signal = np.sin(2 * np.pi * frequency * t)

downsampled_signal, downsampled_time = downsample_signal(signal)

# Compare lengths
print("Original signal length:", len(signal))
print("Downsampled signal length:", len(downsampled_signal))

# Check target ratio
original_length = len(signal)
downsampled_length = len(downsampled_signal)
target_ratio = 0.2
achieved_ratio = downsampled_length / original_length
print(f"Original Length: {original_length}")
print(f"Downsampled Length: {downsampled_length}")
print(f"Target Ratio: {target_ratio}, Achieved Ratio: {achieved_ratio:.2f}")

# Verify all maxima and minima are present
extrema_indices_original = np.where((np.diff(np.sign(np.diff(signal))) != 0))[0] + 1
extrema_values_original = signal[extrema_indices_original]

# Check if extrema exist in the downsampled signal
extrema_present = all(value in downsampled_signal for value in extrema_values_original)
print(f"All extrema preserved: {extrema_present}")

# Plot the results
plt.figure(figsize=(10, 5))
plt.plot(t, signal, label="Original Signal", alpha=0.7)
plt.scatter(downsampled_time, downsampled_signal, color="red", label="Downsampled Signal (20%)", zorder=5)
plt.title("Downsampled Signal Preserving Maxima and Minima")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()
