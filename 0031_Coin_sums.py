"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
import time
start_time = time.time()

counter = 0

for a in range(3):
    for b in range(5):
        if a*100 + b*50 > 200:
            break
        for c in range(11):
            if a * 100 + b * 50 + c*20 > 200:
                break
            for d in range(21):
                if a * 100 + b * 50 + c * 20 + d*10 > 200:
                    break
                for e in range(41):
                    if a * 100 + b * 50 + c * 20 + d * 10 + e*5 > 200:
                        break
                    for f in range(101):
                        if a * 100 + b * 50 + c * 20 + d * 10 + e * 5 + f*2 > 200:
                            break
                        if a*100 + b*50 + c*20 + d*10 + e*5 + f*2 <= 200:
                            counter += 1
                            print(counter)



print(counter + 1)

print("--- {} seconds ---".format(time.time() - start_time) )
