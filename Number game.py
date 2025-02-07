def game():
    '''Game that makes computer guess the number you choose under 10 moves

    :param str input: player input
    :rtype: str + int
    :return: String with a number choosen algorytm
    '''
    print("Pomyśl liczbę od 0 do 1000 a ja ją zgadnę w max. 10 próbach")
    minimum , maximum = 0, 1000
    while True:
        guess = int((maximum - minimum) / 2) + minimum
        print(f"Zgaduje {guess}")
        answer = input('Komendy: za dużo, za mało, zgadłeś: ')

        if answer == str("zgadłeś"):
            print('Wygrałem!')
            break
        elif answer == str('za dużo'):
            maximum = guess
            continue
        elif answer == str('za mało'):
            minimum = guess
            continue
        else:
            print('Nie oszukuj')
            continue

if __name__ == '__main__':
    game()