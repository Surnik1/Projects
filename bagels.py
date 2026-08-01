from random import randint

print("""Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
I have thought up a number.
 You have 10 guesses to get it.""")
n = str(randint(100,999))
nl = list(n)
def check(guess):
    if n == guess:
        return 0
    res = ''
    gl = list(guess)
    for i in range(3):
        if gl[i] in nl:
            if gl[i] == nl[i]:
                res += 'Fermi '
            else:
                res += 'Pico '
    if res == '':
        res = 'Bagels'
    return res

for i in range(1,11):
    print(f"GUESS #{i}:")
    g = input('>')
    res = check(g)
    if res == 0:
        print('You got it!')
        break
    else:
        print(res)