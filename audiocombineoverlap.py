import os
import argparse
import numpy as np
from scipy.io import wavfile

# Set up arg parser
parser = argparse.ArgumentParser(description='Combine multiple WAV files with an overlapping gradient')
parser.add_argument('-i','--input_dir', type=str, help='The directory containing input WAV files')
parser.add_argument('-o', '--output_dir', type=str, help='The directory to write the combined WAV file to')
parser.add_argument('-d', '--duration', type=int, default=50, help='The duration of the overlapping gradient in milliseconds')
parser.add_argument('-s', '--samples', type=int, default=1000, help='The number of samples to use for the overlapping gradient')

args = parser.parse_args()

# Load all the WAV files in the input directory
files = [f for f in os.listdir(args.input_dir) if f.endswith('.wav')]

# Get sample rate from the first file
_, data = wavfile.read(os.path.join(args.input_dir, files[0]))
sample_rate = _

audio_data = []
for f in files:
    _, data = wavfile.read(os.path.join(args.input_dir, f))
    audio_data.append(data)

# Calculate the total length of the combined audio signal
total_samples = sum([len(d) for d in audio_data])

# Create an empty array to hold the combined audio signal
combined_audio = np.zeros(total_samples, dtype=np.int16)

# Loop through each WAV file and add to the combined audio signal
offset = 0
for i, data in enumerate(audio_data):
    # Calculate the number of samples to use for the overlapping gradient
    gradient_samples = int(args.duration / 1000 * len(data))
    
    # Create the overlapping gradient
    gradient = np.linspace(0, 1, gradient_samples)
    
    # Concatenate the overlapping gradient and the original audio data
    data_start = (data[:gradient_samples] * gradient).astype(np.int16)
    data_end = (data[-gradient_samples:] * gradient[::-1]).astype(np.int16)
    data = np.concatenate((data_start, data[gradient_samples:-gradient_samples], data_end))
    
    # Add the modified data to the combined audio signal
    combined_audio[offset:offset+len(data)] += data
    offset += len(data)

# Save the combined audio signal to a WAV file
if not os.path.exists(args.output_dir):
    os.makedirs(args.output_dir)
output_file = os.path.join(args.output_dir, 'combined.wav')
wavfile.write(output_file, sample_rate, combined_audio)
