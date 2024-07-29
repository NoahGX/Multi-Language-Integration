# Multi Language Integration

#### Overview
This project utilizes a combination of programming languages (MATLAB, C, Haskell, Prolog) to perform a series of image manipulations. The core Python script, `Wrapper.py`, orchestrates the entire process, invoking the necessary compilers and runtimes for each language to process an image, transform it, and compile the results. The final output is a grid display of the original and processed images, showcasing the distinct capabilities of each language.

#### Features
  - **MATLAB Integration**: Uses MATLAB scripts to handle image resizing and reshaping.
  - **C Programming**: Processes the image data to create a black and white version.
  - **Haskell Programming**: Transforms the image by flipping colors.
  - **Prolog Programming**: Rotates the image.
  - **Comprehensive Output**: Combines outputs from different languages in a single image grid.

#### Usage
To run the project:
  ```
  python Wrapper.py
  ```
This command initiates the sequence described in the Overview, compiling and running code across different languages, and generating the final image outputs.

#### Prerequisites
  - **Python 3.x**: Ensure Python is installed.
  - **MATLAB**: Version R2023b or similar, adjust the path in the script if necessary.
  - **GCC**: For compiling the C program.
  - **GHC**: For compiling Haskell code.
  - **SWI-Prolog**: For running Prolog scripts.

#### Input
The initial input is a grayscale image, specified in the MATLAB script (`matlabcode1.m`), but can be changed if needed. This image is resized, reshaped into a 1D array, and written to `input.txt`, which serves as the input for the subsequent programs.

#### Output
The output files of the program are:
  - **Intermediate Text Files**: Each program (C, Haskell, Prolog) writes its output to a text file.
  - **Final Image**: A composite image displaying the original alongside each processed version, saved as `output_image.png`.

#### Notes
  - Ensure MATLAB is properly configured to execute scripts.
  - Ensure all paths (MATLAB executable, image files) are correctly set for your system environment.
  - Adjust the executable names and paths if different compilers or interpreters are used.