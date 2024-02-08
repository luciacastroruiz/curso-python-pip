import random

options = ('piedra', 'papel', 'tijera')
rounds = 1
user1_wins = 0
user2_wins = 0

while True:

    print('*'*10)
    print('ROUND', rounds)
    print('*'*10)

    print('puntaje user1= ', user1_wins)
    print('puntaje user2= ', user2_wins)
    
    user1_option = input('Elige Piedra, papel o tijera= ')
    user2_option = random.choice(options)

    user1_option = user1_option.lower()
    user2_option = user2_option.lower()

    print(user1_option)
    print(user2_option)

    if not user1_option in options:
        print('Esta opción no es válida')

    if user1_option == user2_option:
        print('Empate!')
    elif user1_option == 'piedra':
        if user2_option == 'tijera':
            print('piedra le gana a tijera')
            print('user1 ganó')
            user1_wins += 1
        else:
            print('papel le gana a piedra')
            print('user2 ganó')
            user2_wins += 1

    elif user1_option == 'tijera':
        if user2_option == 'piedra':
            print('piedra le gana a tijera')
            print('user2 ganó')
            user2_wins += 1
        else:
            print('tijera le gana a papel')
            print('user1 ganó')
            user1_wins += 1

    elif user1_option == 'papel':
        if user2_option == 'piedra':
            print('papel le gana a piedra')
            print('user1 ganó')
            user1_wins += 1
        else:
            print('tijera le gana a papel')
            print('user2 ganó')
            user2_wins += 1

    rounds += 1
    
    if user1_wins == 5:
        print('***El rotundo ganador es= user1***')
        break
    if user2_wins == 5:
        print('***El rotundo ganador es= user2***')
        break
    