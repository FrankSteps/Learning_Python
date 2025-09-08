#too hot or too could
import random
import sys

int_num = random.randint(1, 20)
#print(int_num)

dificult_str = input("Chanse your dificult level (1, 2 or 3): ")
dificult_int = int(dificult_str)

if dificult_int == 1:
    count = 7
elif dificult_int == 2:
    count = 5
elif dificult_int == 3:
    count = 3
else:
    print("Are you retarded, bro!?!?!?!?")
    sys.exit(1)

while count > 0:
    guess_str = input("What's your guess? ")
    guess_int = int(guess_str)
    print("your chances: ", count)
    count -= 1

    if guess_int >= int_num + 5:
        print("smaller")

    elif int_num < guess_int < int_num + 5:
        print("slightly smaller")

    elif guess_int <= int_num - 5:
        print("greater")

    elif int_num - 5 < guess_int < int_num:
        print("slightly greater")

    elif guess_int == int_num:
        print("You win!!!!!! congratulations for doing the minimum <3!")
        sys.exit(0)


if count == 0:
    print("Game Over: you lose... you are a dumb, man!?")
    print("the answer was: ", int_num)
    sys.exit(0)

