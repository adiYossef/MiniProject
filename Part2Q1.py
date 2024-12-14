import numpy as np

def downsample_signal(signal):
    sampling_interval=0.01

    # approximate length of the output array
    target_ratio=0.2

    # Calculate the time points for the original signal
    num_points = len(signal)
    original_time = np.arange(0, num_points * sampling_interval, sampling_interval)
    
    # Find indices of maxima and minima
    extrema_indices = np.where((np.diff(np.sign(np.diff(signal))) != 0))[0] + 1
    
    # Add the first and last points to the extrema indices
    extrema_indices = np.unique(np.concatenate(([0], extrema_indices, [len(signal) - 1])))
    
    # Preserve extrema points
    downsampled_indices = list(extrema_indices)
    
    # Determine additional points needed to reach the target length
    target_length = int(target_ratio * num_points)
    additional_points_needed = max(0, target_length - len(downsampled_indices))
    
    # Uniformly sample additional points between extrema
    if additional_points_needed > 0:
        all_indices = np.arange(len(signal))
        available_indices = np.setdiff1d(all_indices, downsampled_indices)  # Avoid extrema points
        additional_indices = np.linspace(0, len(available_indices) - 1, additional_points_needed, dtype=int)
        downsampled_indices.extend(available_indices[additional_indices])
    
    # Sort all selected indices
    downsampled_indices = np.sort(downsampled_indices)
    
    # Create the downsampled signal
    downsampled_signal = signal[downsampled_indices]
    downsampled_time = original_time[downsampled_indices]
    
    return downsampled_signal, downsampled_time