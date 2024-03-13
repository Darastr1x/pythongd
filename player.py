import random


class Player:
    def __init__(self, char):
        self.char = char
        self.gold = 99
        self.block = 0
        self.keep_block = False
        self.max_energy = 3
        self.current_energy = None
        self.cost = None

        self.deck = []
        self.hand = []
        self.draw_pile = []
        self.discard_pile = []
        i_deck = ['i_strike', 'i_strike', 'i_strike', 'i_strike', 'i_strike', 'i_defend', 'i_defend', 'i_defend', 'i_defend', 'bash']
        s_deck = ['s_strike', 's_strike', 's_strike', 's_strike', 's_strike', 's_defend', 's_defend', 's_defend', 's_defend', 's_defend', 'survivor', 'neutralize']
        d_deck = ['d_strike', 'd_strike', 'd_strike', 'd_strike', 'd_defend', 'd_defend', 'd_defend', 'd_defend', 'zap', 'dualcast']
        w_deck = ['w_strike', 'w_strike', 'w_strike', 'w_strike', 'w_defend', 'w_defend', 'w_defend', 'w_defend', 'eruption', 'vigilance']
        self.blit_cards = []

        self.max_health = None
        self.current_health = self.max_health
        self.relics = []

        if char == 'ironclad':
            self.max_health = 80
            self.current_health = self.max_health
            self.relics.append('burning_blood')
            self.deck.extend(i_deck)
        elif char == 'silent':
            self.max_health = 70
            self.current_health = self.max_health
            self.relics.append('ring_of_the_snake')
            self.deck.extend(s_deck)
        elif char == 'defect':
            self.max_health = 75
            self.current_health = self.max_health
            self.relics.append('cracked_core')
            self.deck.extend(d_deck)
        elif char == 'watcher':
            self.max_health = 72
            self.current_health = self.max_health
            self.relics.append('pure_water')
            self.deck.extend(w_deck)

        self.draw_pile.extend(self.deck)
        random.shuffle(self.draw_pile)

    def take_turn(self):
        print('TAKING TURN')
        self.current_energy = self.max_energy
        if not self.keep_block:
            self.block = 0
        self.blit_cards = []
        self.draw(5, 10)
        self.blit_cards = self.hand.copy()
        print('CARDS TO BLIT', self.blit_cards)
        print('TAKING TURN 2')

        # Alternatively, if you want to keep the cards in hand for some reason, you can use:
        # self.discard_pile.extend(self.hand[:])
        # self.hand.clear()

    def end_turn(self):
        # Move each card in hand to discard_pile
        self.discard_pile.extend(self.hand)
        self.hand.clear()

    def draw(self, times, max_hand):
        for x in range(0, times):

            print('DRAWING CARD')

            if len(self.hand) <= max_hand:
                if len(self.draw_pile) != 0:
                    self.hand.append(self.draw_pile[0])
                    del self.draw_pile[0]

                    print('CARD ADDED TO HAND')

                else:
                    self.draw_pile.extend(self.discard_pile)
                    self.discard_pile.clear()
                    random.shuffle(self.draw_pile)
                    self.hand.append(self.draw_pile[0])
                    del self.draw_pile[0]

                    print('DRAW PILE RAN OUT')

    def discard(self, num):
        # temp #
        return num

    def play_card(self, card):

        print('PLAYING CARD')

        # IRONCLAD CARDS #

        if card == 'i_defend.png':
            self.cost = 1
            if self.cost >= self.current_energy:
                self.current_energy -= self.cost
                self.block += 5

        if card == 'i_attack.png':
            self.cost = 1
            if self.cost >= self.current_energy:
                self.current_energy -= self.cost
                # NEED MONSTER CLASS (6 damage) #
                return

        if card == 'bash.png':
            self.cost = 2
            if self.cost >= self.current_energy:
                self.current_energy -= self.cost
                # NEED MONSTER CLASS (8 damage, 2 vulnerable) #

        # SILENT CARDS #

        if card == 's_defend.png':
            self.cost = 1
            if self.cost >= self.current_energy:
                self.current_energy -= self.cost
                self.block += 5

        if card == 's_attack.png':
            self.cost = 1
            if self.cost >= self.current_energy:
                self.current_energy -= self.cost
                # NEED MONSTER CLASS (6 damage) #
                return

        if card == 'neutralize.png':
            self.cost = 0
            if self.cost >= self.current_energy:
                self.current_energy -= self.cost
                # NEED MONSTER CLASS (3 damage, 1 weak) #

        if card == 'survivor.png':
            self.cost = 1
            if self.cost >= self.current_energy:
                self.current_energy -= self.cost
                self.block += 8
                self.discard(1)

        # DEFECT CARDS #

        if card == 'd_defend.png':
            self.cost = 1
            if self.cost >= self.current_energy:
                self.current_energy -= self.cost
                self.block += 5

        if card == 'd_attack.png':
            self.cost = 1
            if self.cost >= self.current_energy:
                self.current_energy -= self.cost
                # NEED MONSTER CLASS (6 damage) #
                return

        if card == 'dualcast.png':
            self.cost = 1
            if self.cost >= self.current_energy:
                self.current_energy -= self.cost
                # EVOKE 1 #
                return

        if card == 'zap.png':
            self.cost = 1
            if self.cost >= self.current_energy:
                self.current_energy -= self.cost
                # CHANNEL 1 LIGHTNING #
                return

        # WATCHER CARDS #

        if card == 'w_defend.png':
            self.cost = 1
            if self.cost >= self.current_energy:
                self.current_energy -= self.cost
                self.block += 5

        if card == 'w_attack.png':
            self.cost = 1
            if self.cost >= self.current_energy:
                self.current_energy -= self.cost
                # NEED MONSTER CLASS (6 damage) #
                return

        if card == 'eruption.png':
            self.cost = 2
            if self.cost >= self.current_energy:
                self.current_energy -= self.cost
                # NEED MONSTER CLASS (9 damage, enter wraith) #

        if card == 'vigilance.png':
            self.cost = 2
            if self.cost >= self.current_energy:
                self.current_energy -= self.cost
                # ENTER CALM #
                self.block += 5
