# tiff2jpeg
`tiff2jpeg` is fast batch `tiff` to `jpeg` converter that preserve the folder structure. It purposefully designed to convert hundred of thousand `tiff` images with intricate folder structure, usually comes from microscope raw data such as Mica (Leica), Cell-IQ (Yokogawa), Incucyte (Sartorius), and other microscope system! The script utilize multithreading and other optimization

# Use case scenario
## Problem that we usually face
Imagine you have the folder structure below. Each subfolder contain a lot subfolder (usually from 96 well plate name schema). Inside of each 96 well, you have thousand of `tiff` files. Then, you want to convert into `jpeg` in a new parent folder. 
```
cancer_treated_2023.08.08/
├─ plate_01/
│  ├─ A01_1/
│  ├─ A02_1/
│  ├─ A03_1/
│  ├─ ...
├─ plate_02/
│  ├─ A01_1/
│  ├─ A02_1/
│  ├─ A03_1/
│  ├─ ...
├─ plate_03/
│  ├─ A01_1/
│  ├─ A02_1/
│  ├─ A03_1/
│  ├─ ...
├─ ...
```
## Usage

1. **Setup**: Ensure `tqdm` and `imageio` libraries are installed.
2. **Directories**: Modify `input_dir` and `output_dir` variables to designate your directories containing `.TIFF` images and the desired output location for `.JPEGs`, respectively.
3. **Executor Selection**: Based on workload characteristics and system features, you can opt between `ThreadPoolExecutor` and `ProcessPoolExecutor`. The default executor in the provided code is set to threads. To switch, uncomment the relevant lines in the code.
4. **Adjusting Workers**: Tweak the `max_workers` parameter based on system capacity and performance observations. A recommended starting point is the number of available CPU threads.


# Optimization and Multithreading

## Overview
This code performs image format conversion, changing `.TIFF` files to `.JPEG`, and is optimized for speed using several techniques:

### 1. Image File Handling with `imageio`
- We transitioned from PIL to the `imageio` library. `imageio` provides efficient format conversions, especially when no image transformations are required.

### 2. Directory Creation Optimization
- Instead of repetitively checking and potentially creating a directory for every image, we maintain a set of directories that have already been created. This reduces redundant filesystem interactions.

### 3. Multithreading with `ThreadPoolExecutor`
- Python's built-in `concurrent.futures.ThreadPoolExecutor` is employed to process multiple images concurrently, leveraging multiple CPU threads. Such a parallel processing mechanism is ideal for I/O-bound tasks. When one thread is waiting for I/O tasks to conclude, other threads can continue their processing tasks.

### 4. Multiprocessing with `ProcessPoolExecutor`
- An alternative to threading, the code is also designed to use Python's `ProcessPoolExecutor` for parallel processing. This allows for distribution of work among multiple CPU cores. Though this approach can be more suitable for CPU-intensive tasks, it generally has a higher overhead compared to threading. Therefore, the choice between threading and multiprocessing will depend on specific workload and environmental parameters.

