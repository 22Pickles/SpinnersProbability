import random
def test():
    spin = random.randint(0,3)

    if spin == 0:
        return 1
    spin_2 = random.randint(0, 3)
    if spin_2 == 0:
        return 1
    else:
        return 0

i = 0
win_counter = 0
total = 0
while i < 10000000000:
    output = test()
    if output == 1:
        win_counter = win_counter + 1
    total = total + 1
    i = i+1
print(f"The amount of wins is {win_counter} out of {total} games.")
print(f"This is {100*(win_counter/total)}%")
