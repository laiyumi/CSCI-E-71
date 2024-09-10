import sys

n = len(sys.argv)

# loop over the input names
for i in range(1, n):
    print("Hello, " + sys.argv[i] + "!")