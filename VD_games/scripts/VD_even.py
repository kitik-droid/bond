import random

def run_NOD_game():

    print("Welcome to the VD Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the greatest common divisor of given numbers.")

    def gcd_game():
        wins = 0

        while wins < 3:
            number = list(range(1, 101))
            num1 = random.choice(number)
            num2 = random.choice(number)

            # Вычисляем НОД
            a, b = num1, num2
            while b:
                a, b = b, a % b
            correct_answer = a

            print(f"Question: {num1} {num2}")
            user_answer = input("Your answer: ")

            try:
                user_answer = int(user_answer)
                if user_answer == correct_answer:
                    print("Correct!")
                    wins += 1
                    if wins == 3:
                        print(f"Congratulations, {name}!")
                        break
                else:
                    print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
                    print(f"Let's try again, {name}!")
                    wins = 0

            except ValueError:
                print("Please enter a valid number!")

    gcd_game()



