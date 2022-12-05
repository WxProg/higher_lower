from os import system, name
from art import logo, vs
from game_data import data
from random import choice, randint


def start_game():
    def clear():
        """A function that clears the terminal wherever it is called"""
        # Must enable Emulate terminal output in console. click on the main.py file your working on
        # then look for modify run configuration.
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

    def format_data(a_dict):
        dict_name = a_dict['name']
        description = a_dict['description']
        country = a_dict['country']
        return f"{dict_name}, a/an {description}, from (the) {country}."

    def who_dominates(decision, follower_a, follower_b):
        """Return true, if user choice is correct with who have more followers and return false if not"""
        if follower_a > follower_b and decision == 'a':
            return True
        elif follower_b > follower_a and decision == 'b':
            return True
        else:
            return False

    score = 0
    print(logo)
    compare_b = choice(data)

    is_on = True
    while is_on:
        compare_a = compare_b
        compare_b = choice(data)

        a_follower_count = compare_a['follower_count']
        b_follower_count = compare_b['follower_count']

        print(f"Compare A: {format_data(compare_a)}")
        print(vs)
        print(f"Against B: {format_data(compare_b)}")
        who_has_more = input("Who has more followers on IG? Enter 'A' or 'B': ").lower()

        clear()
        if who_dominates(who_has_more, a_follower_count, b_follower_count):
            score += 1
            print(f"That is correct. Your current score is: {score}")
        else:
            is_on = False
            print(f"That is wrong. Your final score is: {score}")


start_game()
