secret_word = 'Password'
guess = ""
guess_count = 0
guess_limit = 6
out_of_guesses = False
Secret_word = True

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter a password: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, You lose!")
else:
    print("You win!")

secret_word = 'Kyle'
guess = ""
guess_count = 0
guess_limit = 6
out_of_guesses = False
Secret_word = True

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter a password: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, You lose!")
else:
    print("You win!")