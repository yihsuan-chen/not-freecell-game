import random
import math
from card import Card


class Deck:
    def __init__(self, value_start, value_end, number_of_suits):

        self.n_start = value_start
        self.n_end = value_end
        self.n_suit = number_of_suits
        # theDeck is a attribute indicate where we place the card
        self.theDeck = {}
        # theDeck[0] store the initial cards
        self.theDeck[0] = []

        # generate the initial cards and store in theDeck[0]
        # The first character of suit parameter indicate the colors of the card(B for Black; R for Red)
        # The remaining character of suit parameter are numbers representing different suits with the given color
        for j in range(1, self.n_suit + 1):
            k = math.ceil(j / 2)
            suit = ""
            if j % 2 == 1:
                suit = "B" + str(k)
            elif j % 2 == 0:
                suit = "R" + str(k)
            for i in range(self.n_start, self.n_end + 1):
                # the card face 11,12,13,1 use the character J,Q,K,A to present
                if i == 11:
                    self.theDeck[0].append(Card(suit, i, the_face="J"))
                elif i == 12:
                    self.theDeck[0].append(Card(suit, i, the_face="Q"))
                elif i == 13:
                    self.theDeck[0].append(Card(suit, i, the_face="K"))
                elif i == 1:
                    self.theDeck[0].append(Card(suit, i, the_face="A"))
                else:
                    self.theDeck[0].append(Card(suit, i))
        # randomize the cards
        random.shuffle(self.theDeck[0])

    def __str__(self):

        newstring = ""

        for card in self.theDeck[0]:
            newstring += str(card) + "\n"

        return newstring

    def is_empty(self, x):
        return len(self.theDeck[x]) == 0

    def get_card(self, x, y):

        return self.theDeck[x][y]

    def add_card(self, x, the_card):

        self.theDeck[x].append(the_card)

    def draw_card(self, x, y):

        del self.theDeck[x][y]

    def move_card(self, from_x, from_y, to_x):

        the_card = self.get_card(from_x, from_y)
        self.add_card(to_x, the_card)
        self.draw_card(from_x, from_y)


def main():
    test_deck = Deck(1, 13, 2)
    print(test_deck)


if __name__ == "__main__":
    main()
