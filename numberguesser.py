import random 
# randNum = random.randrange(1,101)
randNum =  11
print(randNum)
#this gives the first hint, whether its above/below 50
if randNum >= 50:
    print('Clue: The random number is 50 or above')
elif randNum <= 50:
    print('Clue: The random number is 50 or below')
#input for first guess
for x in range(1):
    inputNum = input("Guess a number. You have 3 tries: ")
    inputInt = int(inputNum)
    if inputInt == randNum:
        print('You guessed right in one try!')
        break 
    else: #if first guess is wrong
        print('You guessed wrong! 2 more tries.')
        for i in range(10,1,-1): #checks if number is prime. hard code numbers below 10
            if randNum in [1,2,3,5,7]:
                print('Clue: The random number is prime')
                break
            if (randNum % i == 0) == True:
                print('Clue: The random number is divisible by ' + str(i))
                break
        else: #accounts for prime numbers above 10
            print('Clue: the random number is prime')

    if inputInt != randNum: 
        inputNum = input("Guess again: ")
        inputInt = int(inputNum)
    if inputInt == randNum:
        print('You guessed right!')
        break
    else:
        print('You guessed wrong! One try left: ')
        for n in range(100, 9, -10):
            if randNum < 10:
                print("Clue: The random number is below 10")
                break
            if randNum >= n:
                print("Clue: The random number is in the " + str(n) + "'s")
                break

        if inputInt != randNum:
            inputNum = input("Guess again: ")
            inputInt = int(inputNum)
        if inputInt == randNum:
            print('You guessed right!')
            break
        else:
            print('You guessed wrong! The number was ' + str(randNum))