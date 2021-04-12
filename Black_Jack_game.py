import random
from turtledemo.clock import hand


def create_deck():
    """ This function is going to create a deck."""

    deck = []
    playing_cards = ["Ace", "King", "Queen", "Jack", 10, 9, 8, 7, 6, 5, 4, 3, 2]  # all types of cards

    for i in range(4):  # 4 different playing card suits
        for card in playing_cards:
            deck.append(str(card))

    random.shuffle(deck)
    return deck




class Player:

    def __init__(self, hand=[],money=1000):  # hand, money are standard's values, defaults. Hand is empty list for storing elements
        """ The __init__ method of Player class initializes the atributes of clas.  """

        self.hand = hand
        self.score = self.set_score()
        self.money = money
        self.bet = 0

    def __str__(self) -> str:
        """ the __str__ method is defined to see updated player hand and score every round. Print player. """

        current_hand = ""  # we return all lements in the hand in the string format (e.g. self.hand = ["Ace",4] to "Ace, 4"
        for card in self.hand:
            current_hand += str(card) + " "
        final_status = (f'Cards in your hand: {current_hand} | score: {str(self.score)}')  # "A 10 score: 21"
        return final_status

    def set_score(self):
        """ The set_score method of Player class recalculates the score over current_hand."""
        self.score = 0
        card_dictionary = {"Ace": 11, "King": 10, "Queen": 10, "Jack": 10, "10": 10, "9": 9, "8": 8,
                           "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
        ace_counter = 0
        for card in self.hand:
            self.score += card_dictionary[card]
            if card == "Ace":
                ace_counter += 1
            if self.score > 21 and ace_counter != 0:
                self.score -= 10
                ace_counter -= 1
        return self.score

    def hit(self, card):
        """ This method aims to pick a new card from the pack of cards."""
        self.hand.append(card)
        self.score = self.set_score() #recalculating of score

    def play(self, new_hand):
        """ This method aims to restart the game."""
        self.hand = new_hand
        self.score = self.set_score() #recalculating of score

    def bet_money(self, amount):
        """ This method enables to bet the particular amount of money."""
        self.money -= amount # money 100->80,
        self.bet += amount  # bet 0-> 20

    def win(self, result) -> object:
        """ This method enables to sum the money if you win."""
        if result == True:
            if self.score == 21 and len(self.hand) == 2:
                self.money += 2.5*self.bet
                print("Congrats BlackJack!")
            else:
                self.money += 2*self.bet
                print("Congrats you won!")
            self.bet = 0
        else:
            self.bet = 0
            print("Sorry, you lost!")

    def draw(self):
        """ This method return money back to the players if the game ends with draw."""
        self.money += self.bet
        self.bet = 0

    def has_black_Jack(self):
        """ This method checks if starting cards are equal to BlackJack value."""

        if self.score == 21 and len(self.hand) == 2:
            return True
        else:
            return False

def print_house(House):
    for card in range(len(House.hand)):
        if card == 0:
            print("X", end = " ")
        elif card == len(House.hand) -1:
            print(House.hand[card])
        else:
            print(House.hand[card], end = " ")



card_deck = create_deck()

first_hand = [card_deck.pop(), card_deck.pop()]
second_hand = [card_deck.pop(), card_deck.pop()]
Player1 = Player(first_hand)
House = Player(second_hand)
Bet = int(input("How many would you like to bet: "))
Player1.bet_money(Bet)
print(f'Pavel: {Player1}')
print_house(House)
if Player1.has_black_Jack():
    if House.has_black_Jack():
        Player1.draw()
    else:
        Player1.win(True)
else:
    while True:
        action = input("Do you want another car? (y/n): ")
        if action == "y":
            Player1.hit(card_deck.pop())
            print(f'Pavel: {Player1}')
            print_house(House)
        else:
            break
    while (House.score <16):
        print(House)
        House.hit(card_deck.pop())

    if Player1.score > 21:
        if House.score > 21:
            Player1.draw()
        else:
            Player1.win(False)

    elif Player1.score > House.score:
        Player1.win(True)

    elif Player1.score == House.score:
        Player1.draw()
    else:
        if House.score > 21:
            Player1.win(True)
        else:
            Player1.win(False)

print(f' Your money {Player1.money}')
print(House)



