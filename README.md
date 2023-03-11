
Replace `input_dir` with the path to the directory containing the WAV files you want to combine, and `output_dir` with the path to the directory where you want to save the combined WAV file.

The `duration` argument is the duration of the overlapping gradient in milliseconds. We recommend setting this to `1` to create a short, subtle fade between the files.

The `samples` argument is the number of samples to use for the overlapping gradient. We recommend setting this to `2000` to create a smooth transition between the files.

## Example

Here's an example command to combine WAV files in a directory called `input` and save the output to a directory called `output`:

python audiocombineoverlap.py -i input -o output -d 1 -s 2000

## Note

The choice of the `duration` and `samples` arguments will affect the sound of the final combined audio, so it's recommended to experiment with different values to achieve the desired result.
