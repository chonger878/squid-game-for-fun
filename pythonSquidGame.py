import random

gamerNum = random.randint(1,457)

print("Welcome, gamer", gamerNum, ". ", "Let's play some games")

print("First game: Red Light, Green Light")

outNum = print(random.randint(1,457))

if outNum == gamerNum:
    print("Sorry, you were eliminated.")
else:
    print("Congrats, you are moving to the next round!")

print("Next game: Dalgona Honeycomb game")

outNumTwo = print(random.randint(1,457))
if outNumTwo == gamerNum:
    print("Sorry, you have failed to complete the honeycomb and are now eliminated")
else:
    print("Congrats, you are moving onto the next round")

print("Next game: Tug of War!")
outNumThree = print(random.randint(1,457))
if outNumThree == gamerNum:
    print("Sorry, your team lost to the other team and you were eliminated")
else:
    print("Congrats, you are moving on to the next round!")

print("Next game: Make up a game using marbles!")
outNumFour = print(random.randint(1,457))
if outNumFour == gamerNum:
    print("Sorry, you lost and you were eliminated")
else:
    print("Congrats, you are moving on to the next round!")

print("Second to last: Glass bridge")
outNumFive = print(random.randint(1,457))
if outNumFive == gamerNum:
    print("Sorry, but you fell through the glass and lost")
else:
    print("Congrats! You are moving on to the last round!")

print("Last game: SQUID GAME!!")
outNumLast = print(random.randint(1,457))
if outNumLast == gamerNum:
    print("Sorry, but you have lost the fight.")
else:
    print("Congrats, you are the last person standing and you have won 456 billion won!")
    