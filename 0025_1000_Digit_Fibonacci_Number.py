"""
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
a = 1
b = 1
index = 1
while True:
    index += 1
    # print("{}: {}".format(index, b))
    if len(str(b)) == 1000:
        break

    a = a + b
    a, b = b, a

print("Answer:", index)
