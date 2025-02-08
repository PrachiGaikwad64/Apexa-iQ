# Read input and convert it to an integer
N = int(input())

# Loop from 1 to N-1
for i in range(1, N):
    # Generate and print the numerical pattern using arithmetic operations
    print((10**i - 1) // 9 * i)