#write a python3 program to test your typing speed

import random
import time
import os

# Clearing the screen
os.system('cls' if os.name == 'nt' else 'clear')



print("Welcome to the typing speed test")
print("Rules: ")
print("1. You will be given a list of random words")
print("2. You have to type the words as fast as you can")
print("3. You will be given your speed and accuracy after the test")
print("4. You have to type all the words in whatever time you may take.Under no circumstances you can leave the words or add extra words")
print("5. After typing all the words, press enter to get your results")



#read a file containing words
#the file is in same directory as the program

file=open("data.csv","r")
data=file.read()
all_words=data.split("\n")






#define a function for the test

def typing_speed_test():

    
    #print the words one after another
    global all_words

    #take 500 random words from the list

    words=random.sample(all_words,500)

    #shuffle the words
    random.shuffle(words)


    #take random unique words from the list

    print("The words are: \n")
    for i in words:
        print(i,end=" ")
    init_time=time.time()
    #take the input from the user
    user_input=input("\n Please type the above words: \n \n \n")
    final_time=time.time()
    user_input=user_input.split()
    #calculate the time taken by the user
    time_taken=final_time-init_time
    correct_words=0
    if len(user_input)==0:
        print("You did not type anything")
        return
    #calculate the number of words typed by the user
    for i in range(len(user_input)):
        if user_input[i]==words[i]:
            correct_words+=1
    #calculate the accuracy of the user
    accuracy=(correct_words/len(user_input))*100

    #calculate the speed of the user
    speed=(correct_words/time_taken)*60
    print("Your speed is: ",speed," words per minute")
    print("Your accuracy is: ",accuracy," %")
    print("You took ",time_taken," seconds to complete the test")
    
            
#make the front end for user interaction

while True:
    print("Enter 1 to start the test")
    print("Enter 2 to exit")
    user_choice=int(input())
    if user_choice==1:
        typing_speed_test()
        break
    elif user_choice==2:
        print("Thanks for playing")
        break
    else:
        print("Please enter a valid input")
        continue
