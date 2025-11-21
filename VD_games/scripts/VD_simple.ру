import random

def run_simple_game():

    print("Welcome to the VD Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Answer 'yes' if the given number is prime. Otherwise, answer 'no'.")

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def simple_game():
        wins = 0

        while wins < 3:
            random_num = random.randint(1, 100)
            correct_answer = "yes" if is_prime(random_num) else "no"
                          
            print(f"Question: {random_num}")
            user_answer = input("Your answer: ")

            if user_answer not in ["yes", "no"]:
                print("Please enter 'yes' or 'no'")
                continue

            if user_answer == correct_answer:
                print("Correct!")
                wins += 1
                if wins == 3:
                    print(f"Congratulations, {name}!")
                    break
            else:
                print("Incorrect:(")
                print(f"Let's try again, {name}!")               
                wins = 0

    simple_game()

run_simple_game()

