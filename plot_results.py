import matplotlib.pyplot as plt
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

def read_file(filename):
    x = []
    y = []
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('#') or line.startswith('n'):
                continue  # Skip comment lines
            data = line.strip().split(' ')
            x.append(int(data[0]))
            y.append(int(data[1]))
    return x, y

# Read data from results1.txt and results2.txt
x1, y1 = read_file(file1)
x2, y2 = read_file(file2)

# Plot the lines
plt.plot(x1, y1, label='standard LLL attack')
plt.plot(x2, y2, label='improved LLL attack')

# Add labels and title
plt.xlabel('n')
plt.ylabel('Breaks out of 100 tries')
plt.title('Comparison of Results')

# Add legend
plt.legend()

plt.grid(axis='y')

# Display the plot
plt.show()
