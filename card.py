class Card:
    
    def __init__(self, card_suit, card_face, **kwargs):
        self.face = card_face
        self.suit = card_suit

        # if the card has been given special character for the_face
        if "the_face" in kwargs:
            self.the_face = kwargs["the_face"]
        else:
            self.the_face = self.face
        # if the card has been given special character for the_suit
        if "the_suit" in kwargs:
            self.the_suit = kwargs["the_suit"]
        else:
            self.the_suit = self.suit

    def __str__(self):
        return str(self.the_suit)+"#"+str(self.the_face)

    def get_card_face(self):
        return self.face

    def get_card_suit(self):
        return self.suit


def main():
    testcard = Card("B1", 12, the_face="Q", the_suit="S")
    print(testcard)
   
if __name__ == "__main__":
    main()
