import random

def run_calc_game():
    
    print("Welcome to VD games!")
    name = input ("May I have your name?")
    print(f"Hello, {name}")
    print("What is the result of the expression?")  

    def calculator():

        wins = 0

        while wins < 3:

            number = list(range(1, 101))
            num1 = random.choice(number)
            num2 = random.choice(number) 

            signs = ['+', '-', '*']
            sign = random.choice(signs)
            
            if sign == '+':
                correct_answer = num1 + num2
            elif sign == '-':
                correct_answer = num1 - num2
            elif sign == '*':
                correct_answer = num1 * num2

            print(f"Question: {num1} {sign} {num2}")
            user_answer = input("Your answer:")

            try:
                user_answer = int(user_answer)
                if user_answer == correct_answer:
                    print("Correct!")
                    wins += 1
                    if wins == 3:
                        print(f"Congratulations, {name}!")
                        break
                    
                else:
                    print(f"{user_answer} is wrong answer ;(. Correct answer was {correct_answer}.")
                    print(f"Lets try again, {name}")
                    wins = 0
            

            except ValueError:
                    print("Please enter a valid number!")
        
    calculator()
