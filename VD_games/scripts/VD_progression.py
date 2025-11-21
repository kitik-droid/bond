import random

def run_progression_game():
    
    print("Welcome to VD games!")
    name = input ("May I have your name?")
    print(f"Hello, {name}")
    print("What number is missing in the progression?")  

    def progression():

        wins = 0

        while wins < 3:

            start = random.randint(1, 30)
            step = random.randint(3, 7)
            num = list(range(start, start + 10 * step, step))[:10]
            blur = random.choice(num)

            display_num = num.copy()
            blur_index = num.index(blur)
            display_num[blur_index] = "?"

            print(f"Question: {display_num}")
            user_answer = input("Your answer:")

            try:
                user_answer = int(user_answer)
                if user_answer == blur:
                    print("Correct!")
                    wins += 1
                    if wins == 3:
                        print(f"Congratulations, {name}!")
                        break
                    
                else:
                    print(f"{user_answer} is wrong answer ;(. Correct answer was {blur}.")
                    print(f"Lets try again, {name}")
                    wins = 0
            

            except ValueError:
                    print("Please enter a valid number!")
        
    progression()

run_progression_game()

