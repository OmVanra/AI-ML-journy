# Q10. Letʼs create a “Number Guessing Game”. Given a secret number (already 
# decided by you), write a program that asks the user to guess it and prints: 
# "Too high" 
# "Too low" 
# if the guess is above the number 
# if the guess is below 
# "Correct!" 
# if the guess matches

def number_guessing_game():
    secret_number = 42
    while True:
        guess = int(input("Guess the secret number: "))
        if guess > secret_number:
            print("Too high")
        elif guess < secret_number:
            print("Too low")
        else:
            print("Correct!")
            break 