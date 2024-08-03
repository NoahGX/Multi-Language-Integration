import subprocess

# Input array
input_array = ["1", "2", "3", "4", "5"]

### C PROGRAM ###
# Compile and run C program with input array as arguments
subprocess.run(["gcc", "CprogD1.c", "-o", "Cprog"])
process = subprocess.run(["./Cprog"] + input_array, capture_output=True, text=True)
# Store output of C program in Python variable and print
C_output = process.stdout.strip()
print("\nC Program (add 1) output:\n" + C_output)
print("\n");

### HASKELL PROGRAM ###
# Compile and run Haskell program with input array as arguments
subprocess.run(["ghc", "HprogD1.hs"])
process = subprocess.run(["./HprogD1"] + [str(x) for x in input_array], capture_output=True, text=True,)
# Store output of Haskell program in Python variable and print
HS_output = process.stdout.strip()
print("Haskell Program (subtract 1) output:\n" + HS_output)
print("\n");

### PROLOG CODE ###
# Compile and run Prolog code with input array as arguments
prolog_input = "[" + ",".join(map(str, input_array)) + "]."
process = subprocess.run(['swipl', '-q', '-g', 'main', '-t', 'halt', 'PLprogD1.pl'], input=prolog_input, capture_output=True, text=True)
# Store output of Prolog code in Python variable and print
PL_output = process.stdout.strip()
print("Prolog Code (reverse) output:\n" + PL_output)
print("\n");
