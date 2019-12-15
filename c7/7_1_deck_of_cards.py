import pytest
import random


class Card:
    DIAMONDS = 20
    HEARTS = 21
    CLUBS = 22
    SPADES = 23
    SUITS = list(range(20, 24))
    ACE = 1
    JACK = 11
    QUEEN = 12
    KING = 13

    SHORT = {
        DIAMONDS: '♦',
        HEARTS: '♥',
        CLUBS: '♣',
        SPADES: '♠',
        ACE: 'A',
        JACK: 'J',
        QUEEN: 'Q',
        KING: 'K'
    }

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return '{}{}'.format(
            Card.SHORT[self.value] if self.value in Card.SHORT else self.value,
            Card.SHORT[self.suit]
        )

    def get_value(self):
        return self.value

    def get_max_value(self):
        return self.get_value()


class Deck:
    """
    Standard deck of 52 cards
    """
    def __init__(self, card_cls=Card):
        self.cards = []
        for suit in Card.SUITS:
            for value in range(Card.ACE, Card.KING+1):
                self.cards.append(card_cls(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def take(self):
        """
        Take a card
        :return: A card
        """
        if not self.cards:
            return None

        return self.cards.pop()


class Hand:
    def __init__(self, deck, size):
        self.deck = deck
        self.cards = []
        for _ in range(size):
            self.take_card()

    def __repr__(self):
        return str(self.cards)

    def __gt__(self, other):
        return self.get_score() > other.get_score()

    def take_card(self):
        self.cards.append(self.deck.take())

    def get_score(self):
        return sum(map(lambda c: c.value, self.cards))


class BlackJackCard(Card):
    def get_value(self):
        if self.value >= Card.JACK:
            return 10
        else:
            return self.value

    def get_max_value(self):
        if self.value == Card.ACE:
            return 11
        else:
            return self.value


class BlackJackHand(Hand):
    def __init__(self, deck, size=2):
        super().__init__(deck, size)

    def __gt__(self, other):
        if self.get_score() > 21:
            return False
        if other.get_score() > 21:
            return True
        return super().__gt__(other)

    def get_score(self):
        score = sum(map(lambda c: c.get_value(), self.cards))
        for card in self.cards:
            if card.get_value() == Card.ACE and score + 10 <= 21:
                score += 10
        return score


def test_standard_hand():
    deck = Deck()
    hand1 = Hand(deck, 5)
    assert hand1.get_score() == 55
    hand2 = Hand(deck, 5)
    assert hand2.get_score() == 30
    assert hand1 > hand2


def test_blackjack_hand():
    deck = Deck(card_cls=BlackJackCard)
    hand1 = BlackJackHand(deck)
    assert hand1.get_score() == 20

    hand2 = BlackJackHand(deck)
    assert hand2.get_score() == 20
    hand2.take_card()
    assert hand2.get_score() == 29

    assert hand1 > hand2

    BlackJackHand(deck, 7)  # remove cards up to the ace
    hand3 = BlackJackHand(deck)
    assert hand3.get_score() == 21

    assert hand3 > hand1
    assert hand3 > hand2


if __name__ == '__main__':
    pytest.main(args=[__file__])
