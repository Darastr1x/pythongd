import random


class Monster:

    def __init__(self, name):
        self.name = name
        self.health = 0
        self.max_health = 0
        self.turn = 0
        self.strength = 0
        self.block = 0
        self.split = False
        self.ritual = False
        if self.name == 'cultist':
            self.health = random.randint(48, 54)
            self.max_health = self.health
        if self.name == 'jaw_worm':
            self.health = random.randint(40, 44)
            self.max_health = self.health
        if self.name == 'red_louse':
            self.health = random.randint(10, 15)
            self.max_health = self.health
        if self.name == 'green_louse':
            self.health = random.randint(11, 17)
            self.max_health = self.health
        if self.name == 'acid_slime_m':
            self.health = random.randint(28, 32)
            self.max_health = self.health
            self.split = True
        if self.name == 'acid_slime_s':
            self.health = random.randint(8, 12)
            self.max_health = self.health
        if self.name == 'spike_slime_m':
            self.health = random.randint(28, 32)
            self.max_health = self.health
            self.split = True
        if self.name == 'spike_slime_s':
            self.health = random.randint(10, 14)
            self.max_health = self.health

    def take_turn(self):
        if self.name == 'cultist':
            if self.ritual:
                self.strength += 3
            if self.turn == 0:
                self.ritual = True
                self.turn += 1
                print('turn 0')
                return 'effect',  0
            else:
                return 'attack', 6 + self.strength

    def take_damage(self, num):
        self.health -= num
