from deck import Deck


class Notfreecell:

    def __init__(self):

        # the free cell game deck use the deck with 52 cards(face 1~13 and 4 suits)
        self.gameDeck = Deck(1, 13, 4)
        # a flag to check winning status
        self.win = False
        # store the maximum length of the cascade slots
        self.max_slotlen = 0

        # create cell slot and foundation slot using their index as key value in theDeck
        for i in range(2 * self.gameDeck.n_suit + 1, 4 * self.gameDeck.n_suit + 1):
            self.gameDeck.theDeck[i] = []

        # deal cards in theDeck[0] to Cascade slot
        # n_deal: the minimum number of cards divided to Cascade slot
        n_deal = len(self.gameDeck.theDeck[0]) // (2 * self.gameDeck.n_suit)
        # plus: number of surplus cards
        plus = len(self.gameDeck.theDeck[0]) % (2 * self.gameDeck.n_suit)
        for p in range(1, 2 * self.gameDeck.n_suit + 1):
            if p <= plus:
                self.gameDeck.theDeck[p] = self.gameDeck.theDeck[0]\
                    [(p - 1) * (n_deal + 1):(p - 1) * (n_deal + 1) + (n_deal + 1)]
            else:
                self.gameDeck.theDeck[p] = self.gameDeck.theDeck[0]\
                 [plus * (n_deal + 1) + (p - plus - 1) * n_deal:
                    plus * (n_deal + 1) + (p - plus - 1) * n_deal + n_deal]

    def max_len(self):

        self.max_slotlen = len(self.gameDeck.theDeck[1])
        for j in range(2, 2 * self.gameDeck.n_suit + 1):
            if len(self.gameDeck.theDeck[j]) > self.max_slotlen:
                self.max_slotlen = len(self.gameDeck.theDeck[j])
        return self.max_slotlen

    def __str__(self):

        self.max_len()
        board = ""
        board += "Cells" + "\t" * self.gameDeck.n_suit * 2 + "\t\t\t"+"Foundations" + "\n"

        for i in range(2 * self.gameDeck.n_suit + 1, 4 * self.gameDeck.n_suit + 1):
            board += str(i) + ":"
            if len(self.gameDeck.theDeck[i]) == 0:
                board += "[    ]" + "\t"
            # only output the last card in foundation slots
            elif i > 3 * self.gameDeck.n_suit:
                board += "[" + str(self.gameDeck.theDeck[i][len(self.gameDeck.theDeck[i]) - 1]) + "]" + "\t"
            # each cell slot only has one card
            else:
                board += "[" + str(self.gameDeck.theDeck[i][0]) + "]" + "\t"

        board += "\n"
        board += "------------" * self.gameDeck.n_suit * 2 + "\n"

        # create the cascade slots string for output (in straight direction)
        for j in range(0, self.max_slotlen):
            for i in range(1, 2 * self.gameDeck.n_suit + 1):
                if len(self.gameDeck.theDeck[i]) > j:
                    board += "  " + str(self.gameDeck.theDeck[i][j]) + "  " + "\t"
                else:
                    board += "        " + "\t"
            board += "\n"

        for i in range(1, 2 * self.gameDeck.n_suit + 1):
            board += "   (" + str(i) + ")\t\t"

        return board

    def get_moves(self, x, to_x):

        # if x is the index of the defined slots
        if 0 < x <= 4 * self.gameDeck.n_suit and 0 < to_x <= 4 * self.gameDeck.n_suit:

            # if source slot is not empty
            if not self.gameDeck.is_empty(x):
                # get the card of the source slot
                the_card = self.gameDeck.get_card(x, len(self.gameDeck.theDeck[x]) - 1)
                face = the_card.get_card_face()
                suit = the_card.get_card_suit()

                # if target slot is not empty
                if not self.gameDeck.is_empty(to_x):
                    # get the card of the target slot
                    place_on = self.gameDeck.get_card(to_x, len(self.gameDeck.theDeck[to_x]) - 1)
                    face_on = place_on.get_card_face()
                    suit_on = place_on.get_card_suit()

                    # move card to cascade slot (not empty)
                    if 0 < to_x <= 2 * self.gameDeck.n_suit:

                        if suit[0] != suit_on[0]:

                            if face == (face_on - 1):
                                self.gameDeck.move_card(x, len(self.gameDeck.theDeck[x]) - 1, to_x)

                    # move to foundation (not empty)
                    elif 3 * self.gameDeck.n_suit < to_x <= 4 * self.gameDeck.n_suit:

                        if suit == suit_on:

                            if face == (face_on + 1):
                                self.gameDeck.move_card(x, len(self.gameDeck.theDeck[x]) - 1, to_x)

                # if target slot is empty
                elif self.gameDeck.is_empty(to_x):

                    # empty cascade slot or cell slot
                    if 0 < to_x <= 3 * self.gameDeck.n_suit:
                        self.gameDeck.move_card(x, len(self.gameDeck.theDeck[x]) - 1, to_x)

                    # empty foundation
                    elif 3 * self.gameDeck.n_suit < to_x <= 4 * self.gameDeck.n_suit:
                        if face == self.gameDeck.n_start:
                            self.gameDeck.move_card(x, len(self.gameDeck.theDeck[x]) - 1, to_x)

    # check the winning status
    def win_the_game(self):

        # check every foundation slot whether they have been stacked to the largest card face value
        i = 3 * self.gameDeck.n_suit + 1
        while i <= 4 * self.gameDeck.n_suit:
            if not self.gameDeck.is_empty(i):
                if self.gameDeck.get_card(i, len(self.gameDeck.theDeck[i]) - 1).get_card_face() == self.gameDeck.n_end:
                    if i == 4 * self.gameDeck.n_suit:
                        self.win = True
                        return self.win
                        # if all of foundation slots match the winning condition win=True
                    else:
                        i += 1
                else:
                    break
            else:
                break

        return self.win

    def new_game(self):

        self.gameDeck = Deck(1, 13, 4)


def main():
    game = Notfreecell()
    print(game)

    choice = "0"

    while choice != "q":
        choice = input("Enter m to move, q to quit, r to restart: ")
        # move the card and check winning status
        if choice == "m":
            from_x = int(input("move from slot No: "))
            to_x = int(input("move to slot No: "))
            game.get_moves(from_x, to_x)
            print(game)
            game.win_the_game()
            if game.win:
                print(" *** You win !! *** ")
                break
        # restart the game
        elif choice == "r":
            game = Notfreecell()
            print(game)

if __name__ == "__main__":
    main()
