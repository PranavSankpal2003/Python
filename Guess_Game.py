#It is used to guess the random number between 1 to 100.
import random 

player = int(input("Please enter how many player are playing: "))


#Function to guess the number give output your number is correct or not 
#If your number is correct then it show the count and congratulate you
#If your number is not correct then it show the hint that your number is higher or lower
def guess_number(ran_num, count=0):
    guess_num = int(input("Please enter any number between 1 to 100:"))
    count += 1
    if(guess_num == ran_num) :
        print("Congratulations! You guessed the number correctly.")
        return count + 1
    elif(guess_num < ran_num):
        print("Please try again! The number is higher then you guessed.")
        return guess_number(ran_num, count)
    elif(guess_num > ran_num):
        print("Please try again! The number is lower than you guessed.")
        return guess_number(ran_num, count)
    

# Generate a random number between 1 and 200
for i in range(player):
    print(f"player{i+1} turn:")
    ran_num = random.randint(1,100)
    count = (guess_number(ran_num) - 1)
    print(f"Your count is {count}.")
    print("--------------------------------------------------") 
