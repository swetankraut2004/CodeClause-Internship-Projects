"""
Project ID - #CC9877
Project Title - Simple To-Do List App
Internship Domain - Python Development Intern
Project Level - Entry Level
Assigned By- CodeClause Internship
Assigned To - Swetank Kalyan Raut
Technology used - Python Development
Project Aim - Create a typing speed calculator that measures the user's typing speed in words per minute (WPM).
"""

import random as rn
from time import time

def calculate_errors(paratest, usertest):
    error_count = 0
    for i in range(len(paratest)):
        try:
            if paratest[i] != usertest[i]:
                error_count += 1
        except:
            error_count += 1
    return error_count

def calculate_speed(time_start, time_end, userinput):
    time_diff = time_end - time_start
    time_rounded = round(time_diff, 2)
    words = len(userinput.split())
    wpm = (words / time_rounded) * 60
    return round(wpm), time_rounded

def calculate_accuracy(paratest, usertest):
    error_count = calculate_errors(paratest, usertest)
    total_chars = len(paratest)
    correct_chars = total_chars - error_count
    accuracy = (correct_chars / total_chars) * 100
    return round(accuracy, 2)

if __name__ == '__main__':
    while True:
        check = input("Ready for test : Yes/No : ").strip().lower()
        if check == "yes":
            test_sentences = [
                "This is a typing speed calculator and we are using Python 3 here.",
                "My name is Swetank Raut and I am an Intern at CodeClause.",
                "This is a Python project and it is full of fun."
            ]

            selected_test = rn.choice(test_sentences)

            print("\n****************** Typing Speed Calculator ******************\n")
            print(selected_test)
            print("\n")

            time_start = time()
            user_input = input("Enter: ")
            time_end = time()

            speed, time_taken = calculate_speed(time_start, time_end, user_input)
            accuracy = calculate_accuracy(selected_test, user_input)

            print(f"\nTime taken: {time_taken} seconds")
            print(f"Speed: {speed} WPM")
            print(f"Accuracy: {accuracy}%")

        elif check == "no":
            print("Thank you!")
            break
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")
