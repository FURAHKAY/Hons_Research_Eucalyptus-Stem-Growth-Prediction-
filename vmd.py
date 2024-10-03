import matplotlib.pyplot as plt
from os.path import exists
from os.path import dirname
from os.path import join

# Open the file for reading
script_dir = dirname(__file__) 
filename = "gyrate.txt"
f = open(filename, 'r')  # Use single quotes around the file path

# Initialize an empty list to store temperature values
y = []

# Read temperature values from each line of the file
for line in f:
    y.append(float(line.rstrip('\n')))  # Convert each line to float and remove newline character

# Close the file
f.close()

# Plot the temperature values
fig, ax = plt.subplots()
ax.plot(y)
ax.set(xlabel="Time (ps)", ylabel="Temperature (K)", title="Temperature Equilibration")
plt.show()
