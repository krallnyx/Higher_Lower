from flask import Flask
import random

app = Flask(__name__)
number = random.randint(0, 9)


@app.route('/<guess>')
def guessing(guess):
    global number
    try:
        number_guessed = int(guess)
    except ValueError:
        return '<h1 style="text-align:center;">Guess a number between 0 and 9</h1>' \
           '<img style="margin: 0 auto;display: block;" src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"/>' \
           '<p style="text-align:center;">Please enter you answer in the url, for example www.hurfindia.com/5</p>'
    if number_guessed == number:
        number = random.randint(0, 9)
        return f'<h1 style="text-align:center;">Your guess was {number_guessed} and you were right!</h1>' \
           '<img style="margin: 0 auto;display: block;" src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>'
    elif number_guessed < number:
        return f'<h1 style="text-align:center;">Your guess was {number_guessed} but the correct answer is higher.</h1>' \
               '<img style="margin: 0 auto;display: block;" src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"/>'
    else:
        return f'<h1 style="text-align:center;">Your guess was {number_guessed} but the correct answer is lower.</h1>' \
               '<img style="margin: 0 auto;display: block;" src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"/>'


@app.route('/')
def main():
    return '<h1 style="text-align:center;">Guess a number between 0 and 9</h1>' \
           '<img style="margin: 0 auto;display: block;" src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"/>' \
           '<p style="text-align:center;">Please enter you answer in the url, for example www.hurfindia.com/5</p>'


if __name__ == '__main__':
    app.run(host='0.0.0.0')

