import random
lives = 8
action = ''
words = ['python', 'java', 'kotlin', 'javascript']
random.seed()
typed = set()

print(*'HANGMAN')
while action != 'exit':
    secret_word = random.choice(words)
    hidden_word = '-' * len(secret_word)
    action = input('Type "play" to play the game, "exit" to quit: ')
    if action != 'play':
        continue
    while lives:
        if '-' not in hidden_word:
            print(f'You guessed the word {hidden_word}!\nYou survived!\n')
            break
        print('\n' + hidden_word)
        lett = input('Input a letter: ')
        if len(lett) != 1:
            print('You should input a single letter')
            continue
        if not lett.isalpha() or not lett.islower():
            print('It is not an ASCII lowercase letter')
            continue
        if lett in typed:
            print('You already typed this letter')
            continue
        typed.add(lett)
        if lett in secret_word:
            hidden_word = ''.join([lett if char == lett else hidden_word[i] for i, char in enumerate(secret_word)])
        else:
            print('No such letter in the word')
            lives -= 1
    else:
        print('You are hanged!\n')
