class Card:
    def __init__(self, card_face, card_suit):
        self.face = card_face
        self.suit = card_suit

    def return_card(self):
        return self.face + ' ' + self.suit