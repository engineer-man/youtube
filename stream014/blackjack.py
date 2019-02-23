import os
import random

player_points = 0
dealer_points = 0

def calc_hand(hand):
    non_aces = [c for c in hand if c != 'A']
    aces = [c for c in hand if c == 'A']

    sum = 0

    for card in non_aces:
        if card in 'JQK':
            sum += 10
        else:
            sum += int(card)

    for card in aces:
        if sum <= 10:
            sum += 11
        else:
            sum += 1

    return sum

while True:
    cards = [
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
        '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
    ]

    random.shuffle(cards)

    dealer = []
    player = []

    player.append(cards.pop())
    dealer.append(cards.pop())
    player.append(cards.pop())
    dealer.append(cards.pop())

    first_hand = True
    standing = False

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        player_score = calc_hand(player)
        dealer_score = calc_hand(dealer)

        if standing:
            print(f"Dealer Cards: [{']['.join(dealer)}] ({dealer_score})")
        else:
            print(f'Dealer Cards: [{dealer[0]}][?]')

        print(f"Your Cards:   [{']['.join(player)}] ({player_score})\n==")
        print('')

        if standing:
            if dealer_score > 21:
                print('Dealer busted, you win!')
                player_points+=1
            elif player_score == dealer_score:
                print('Push, nobody wins')
            elif player_score > dealer_score:
                print('You beat the dealer, you win!')
                player_points+=1
                if choice == '3': #(For double down)
                    print('Extra point for doubling down')
                    player_points+=1
            else:
                print('You lose :(')
                dealer_points+=1

            print('')
            print("-=Current score=-")
            print(f" | Dealer: {dealer_points} |")
            print(f" | Player: {player_points} |")
            print('-' * 17)

            print('')
            input('Play again? (Hit enter to continue) ')
            break

        if first_hand and player_score == 21:
            print('Blackjack! Nice!\n')
            input('Play again? (Hit enter to continue) ')
            break

        if player_score > 21:
            print('You busted!')
            print('')
            input('Play again? (Hit enter to continue) ')
            break

        print('What would you like to do?')
        print(' [1] Hit')
        print(' [2] Stand')
        print(' [3] Double Down')

        print('')
        choice = input('Your choice: ')
        print('')

        first_hand = False

        if choice == '1':
            player.append(cards.pop())
        elif choice == '2':
            standing = True
            while calc_hand(dealer) <= 16:
                dealer.append(cards.pop())
        elif choice == '3':
            player.append(cards.pop())
            standing = True
