#!/Library/Frameworks/Python.framework/Versions/3.5/bin/python3.5

""" @package Cardshuffle
Documentation

More details
"""
from collections import deque
import random
from copy import copy
import sys, getopt
from multiprocessing import Pool
from types import *


# Documentation for class
# Deckofcards class. This class also performs operations on the deck of cards.
#
class DeckOfCards:
    def __init__(self, card_count=52):
        """The constructor
        :param card_count: object to specify number of cards.
        """
        # member variable to initialize a new deck of cards.
        # suites C=club, D=diamond, H=hearts, S=spade
        # rank  ace=A, 10=T, jack=J, queen=Q, king=K, numbers=2..9
        try:
            self._deck = deque(rank + suit for rank in "A23456789TJQK" for suit in "CDHS")
            self._table = deque()
            self._deck = deque(random.sample(self._deck, card_count))
        except ValueError:
            e = sys.exc_info()[0]
            print ("Error: %s. card count reset to 52" % e)
        except TypeError as e:
            print ("Error: %s" % e)
        except AttributeError as e:
            print ("Error: %s" % e)
        except:
            e = sys.exc_info()[0]
            print ("Error: %s" % e)

    def shuffle(self):
        """shuffle the deck of cards.
        """
        try:
            if self._deck:
                random.shuffle(self._deck)
            else:
                raise Exception("Empty Deck")
        except IndexError as e:
            print("ERR: Index Error")
        except AttributeError as e:
            print ("Err: %s" % e)
        except Exception as e:
            print ("Err: %s" % e)
        except:
            e = sys.exc_info()[0]
            print ("Err: %s" % e)

    def draw_card(self):
        """    draw the card on the top of the deck    """
        try:
            if self._deck:
                return self._deck.popleft()
        except IndexError:
            print("ERR: Index Error")
        except:
            e = sys.exc_info()[0]
            print ("Error: %s" % e)

    def place_card(self, TorD, card):
        """set card on the table or back of deck
        :param TorD: binary parameter to specify card placement destination.
                    Destination top of table if set to 1 and destination bottom of Deck if 0
        :param card: specifies card that is to be added to specified deque
        :return: return 1 if operation successful.
         """
        try:
            if TorD == 1:
                if sys.version_info < (3, 5):
                    self._table.reverse()
                    self._table.append(card)
                    self._table.reverse()
                else:
                    self._table.insert(0, card)
            elif TorD == 0:
                self._deck.append(card)
            else:
                raise ValueError("TorD must be 0 or 1")
            return 1
        except AttributeError as e:
            print ("Error: %s" % e)
        except:
            e = sys.exc_info()[0]
            print ("Error: %s" % e)


    def pick_deck(self):
        """    transfer deque contents from _table to _deck    """
        try:
            if len(self._deck):
                raise("Hold on. There are already cards in hand.")
            if len(self._table):
                for items in self._table:

                    self._deck.append(items)
                self._table.clear()
                pass
            else:
                 raise Exception("No Cards on table")
        except AssertionError:
            print("ERR: AssertionError (pick_deck)")
        except AttributeError as e:
            print ("Err: %s" % e)
        except Exception as e:
            print ("Error: %s" % e)
        except:
            e = sys.exc_info()[0]
            print ("Err: %s" % e)

    def shuffle_exercise(self):
        """    shuffle deck with following sequence:
            while(len(_deck))
            - pop_left _deck
            - insert(0) _table
            - pop_left _deck
            - append _table
            pick_deck"""
        try:
            cnt = 1
            if self._deck:
                while len(self._deck):
                    if cnt % 2 == 1:
                        card = self.draw_card()
                        self.place_card(1, card)
                    elif cnt % 2 == 0:
                        card = self.draw_card()
                        self.place_card(0, card)
                    cnt += 1
                self.pick_deck()
        except:
            e = sys.exc_info()[0]
            print ("Error: %s" % e)

    def compare_decks(self, deck1, deck2):
        """compare contents of deck
        :param deck1:
        :param deck2:
        :return: return 1 if decks match else 0.
        """
        try:
            for items in range(len(deck1)):
                if deck1[items] != deck2[items]:
                    return 0
            return 1
        except AssertionError:
            print("Assertion ERR")
        except:
            e = sys.exc_info()[0]
            print ("Error: %s" % e)

    def cnt_shuffle_until_original(self):
        """ method to calculate number of shuffles required to reach initial deck state 
        :rtype count: object containing total shuffle count.
        """
        try:
            assert(len(self._deck)),"Empty Deck"
            if self._deck:
                initial_deck_state = copy(self._deck)
                count = 0
                self.shuffle_exercise()
                count += 1
                while self.compare_decks(self._deck, initial_deck_state) != 1:
                    self.shuffle_exercise()
                    count += 1
                if self.compare_decks(self._deck, initial_deck_state) == 1:
                    return count
        except IndexError:
            print("ERR: Index Error!")
            return -1  # empty deque
        except AssertionError as e:
            print ("Error: %s" % e)
        except:
            e = sys.exc_info()[0]
            print ("Error: %s" % e)


def test_cases(n):
    """integer card count value test cases
    :param n: number of cards in deck.
    :return shuffle_count_until_original: returns iterations to reach original deck state
    """
    try:
        cards_list = DeckOfCards(n)
        assert isinstance(cards_list, DeckOfCards),"Object Instance not created."
        return cards_list.cnt_shuffle_until_original()
    except AssertionError:
        e = sys.exc_info()[0]
        print ("Error: %s" % e)


def main(argv):
    count = 52
    test_mode = bool(0)
    try:
        opts, args = getopt.getopt(argv, "hn:t:")
    except getopt.GetoptError:
        print('usage: Cardshuffle.py -n <count> -t <testmode>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('usage: Cardshuffle.py -n <count> -t <testmode>', \
              '\nargs:',\
              '\n\t -n: specify card count',
              '\n\t -t: use 1 to enable test mode and 0 to disable test mode',\
              '\nsamples:',\
              '\n-Cardshuffle.py -> this command will default card count to 52 and test mode to 0',\
              '\n-Cardshuffle.py -n 10 -> card count is set to 10',\
              '\n-Cardshuffle.py -t 1 -> when test mode is set to 1, card count will have no affect on program execution.')
            sys.exit()
        elif opt in ("-n"):
            count = int(arg)
        elif opt in ("-t"):
            test_mode = bool(int(arg))
    try:
        print("CardCount:", count, "TestMode:", test_mode)
        assert type(test_mode) == bool,"test mode must be bool type"
        assert type(count) == int,"card count must be int type"
    except AssertionError as e:
        print ("Error: %s" % e)
        exit()
    if test_mode == 0:
        try:
            cards_list = DeckOfCards(count)
            assert isinstance(cards_list, DeckOfCards),"Object Instance not created."
            print("New deck = %s cards" % len(cards_list._deck))
            print("Shuffle count until original deck:", cards_list.cnt_shuffle_until_original())
        except AssertionError as e:
            print ("Error: %s" % e)

    else:
        with Pool(processes=4) as p:
            print(p.map(test_cases, range(-10, 100), chunksize=10))

if __name__ == "__main__":
    main(sys.argv[1:])
