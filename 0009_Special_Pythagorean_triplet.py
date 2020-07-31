"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

def triplet_1000():
    for i in range(1,334):
        for j in range(1,667-i):
            if ((i**2 + j**2)**(1/2) == int((i**2 + j**2)**(1/2))):
                c = int((i**2 + j**2)**(1/2))
                if (i + j + c == 1000):
                    print(i,j,c,sep="\t")
                    return (int(i * j * c))

print(triplet_1000())