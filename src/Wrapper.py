import subprocess

# Specify full path to MATLAB executable
matlab_executable = '/Applications/MATLAB_R2023b.app/bin/matlab'

# Load MATLAB CODE 1
with open('matlabcode1.m', 'r') as file1:
    matlabcode1 = file1.read()
# Set up MATLAB environment and run first MATLAB script
Matlab_process1 = subprocess.run([matlab_executable, "-batch", "run('matlabcode1.m'); pause(1);"], capture_output=True)
print("Starting process...")
print("Running MATLAB CODE 1")

# Read values from text file
with open('input.txt', 'r') as file2:
    line = file2.readline()
    input_array = [str(value) for value in line.split()]

### C PROGRAM ###
# Compile and run C program with input array as arguments
subprocess.run(["gcc", "Cprog.c", "-o", "Cprog"])
C_Process = subprocess.run(["./Cprog"] + input_array, capture_output=True, text=True)
# Store output of C program in Python variable
C_output = C_Process.stdout.strip()
# Save Python variable to text file
with open('c_output.txt', 'w') as f:
    f.write(C_output)
print("Running C CODE")

### HASKELL PROGRAM ###
# Compile and run Haskell program with input array as arguments
subprocess.run(["ghc", "Hprog.hs"])
H_process = subprocess.run(["./Hprog"] + [str(x) for x in input_array], capture_output=True, text=True,)
# Store output of Haskell program in Python variable
H_output = H_process.stdout.strip()
# Save Python variable to text file
with open('haskell_output.txt', 'w') as f:
    f.write(H_output)
print("Running Haskell CODE")

### PROLOG CODE ###
# Compile and run Prolog code with input array as arguments
prolog_input = "[" + ",".join(map(str, input_array)) + "]."
PL_process = subprocess.run(['swipl', '-q', '-g', 'main', '-t', 'halt', 'PLprog.pl'], input=prolog_input, capture_output=True, text=True)
# Store output of Prolog code in Python variable
PL_output = PL_process.stdout.strip()
# Save Python variable to text file
with open('prolog_output.txt', 'w') as f:
    f.write(PL_output)
print("Running Prolog CODE")

# Load MATLAB CODE 2
with open('matlabcode2.m', 'r') as file3:
    matlabcode2 = file3.read()
# Set up MATLAB environment and run second MATLAB script
Matlab_process2 = subprocess.run([matlab_executable, "-batch", "run('matlabcode2.m'); pause(1);"], capture_output=True)
print("Running MATLAB CODE 2")

# Inform user that program has terminated
print("Terminating process...")
print("Done.")