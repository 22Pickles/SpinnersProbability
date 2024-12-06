import random

#One play of the game
def test():
    #A random number: 0, 1, 2, or 3.
    spin = random.randint(0,3)

    if spin == 0:
        #The 1 indicates a win
        return 1

    #A second random number
    spin_2 = random.randint(0, 3)
    
    if spin_2 == 0:
        return 1
    else:
        #The 0 indicates a loss
        return 0

#Definitions of variables
i = 0
win_counter = 0
total = 0

#Runs the game 10 billion times
#The contents inside are repeated
while i < 10000000000:
    
    #Calling the function
    output = test()

    #Evaluating the output
    if output == 1:
        #Adds 1 to the win counter
        win_counter = win_counter + 1

    #Counts the total number of wins and losses
    total = total + 1
    
    #counts the total number of iterations
    i = i+1

#Outputs results
print(f"The amount of wins is {win_counter} out of {total} games.")
print(f"This is {100*(win_counter/total)}%")
