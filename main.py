import pygame as pg
from image import Images
from player import Player
from monster import Monster

pg.init()
combat_surf = pg.display.set_mode((1920, 1080))
pg.display.set_caption('Combat')

# Initialize Images #

# Start screen and character select #
start_screen = Images('title.png', 1920, 1080)
start_screen = start_screen.load_image()
play_screen = Images('start.png', 1920, 1080)
play_screen = play_screen.load_image()
quit_screen = Images('quit.png', 1920, 1080)
quit_screen = quit_screen.load_image()
select_character = Images('select_character.png', 1920, 1080)
select_character = select_character.load_image()

ironclad = Images('Ironclad.png', 1920, 1080)
ironclad = ironclad.load_image()
silent = Images('Silent.png', 1920, 1080)
silent = silent.load_image()
defect = Images('Defect.png', 1920, 1080)
defect = defect.load_image()
watcher = Images('Watcher.png', 1920, 1080)
watcher = watcher.load_image()

# Character images #
ironclad_char = Images('TheIronclad.png', 240, 255)
ironclad_char = ironclad_char.load_image()
ironclad_char.set_colorkey((0, 0, 0))
silent_char = Images('TheSilent.png', 240, 255)
silent_char = silent_char.load_image()
silent_char.set_colorkey((0, 0, 0))
defect_char = Images('TheDefect.png', 240, 255)
defect_char = defect_char.load_image()
defect_char.set_colorkey((0, 0, 0))
watcher_char = Images('TheWatcher.png', 240, 255)
watcher_char = watcher_char.load_image()
watcher_char.set_colorkey((0, 0, 0))

# Energy #
i_energy = Images('i_energy.jpg', 100, 100)
i_energy = i_energy.load_image()
i_energy.set_colorkey((0, 0, 0))

# Monster images #
cultist = Images('cultist.png', 240, 255)
cultist = cultist.load_image()
cultist.set_colorkey((0, 0, 0))

# Main combat surfaces #
level_1 = Images('Level_1.png', 1920, 1080)
level_1 = level_1.load_image()
level_2 = Images('Level_2.png', 1920, 1080)
level_2 = level_2.load_image()
level_3 = Images('Level_3.png', 1920, 1080)
level_3 = level_3.load_image()
top_bar = Images('top_bar.png', 1920, 76)
top_bar = top_bar.load_image()

# Cards #

# Ironclad cards #
bash = Images('Bash.png', 240, 255)
bash = bash.load_image()
bash.set_colorkey((0, 0, 0))
i_strike = Images('i_strike.png', 240, 255)
i_strike = i_strike.load_image()
i_strike.set_colorkey((71, 112, 76))
i_defend = Images('i_defend.png', 240, 255)
i_defend = i_defend.load_image()
i_defend.set_colorkey((71, 112, 76))

# Silent cards #
survivor = Images('Survivor.png', 240, 255)
survivor = survivor.load_image()
survivor.set_colorkey((0, 0, 0))
neutralize = Images('Neutralize.png', 240, 255)
neutralize = neutralize.load_image()
neutralize.set_colorkey((0, 0, 0))
s_strike = Images('s_strike.png', 240, 255)
s_strike = s_strike.load_image()
s_strike.set_colorkey((71, 112, 76))
s_defend = Images('s_defend.png', 240, 255)
s_defend = s_defend.load_image()
s_defend.set_colorkey((71, 112, 76))

# Defect cards #
zap = Images('Zap.png', 240, 255)
zap = zap.load_image()
zap.set_colorkey((0, 0, 0))
dualcast = Images('Dualcast.png', 240, 255)
dualcast = dualcast.load_image()
dualcast.set_colorkey((0, 0, 0))
d_strike = Images('d_strike.png', 240, 255)
d_strike = d_strike.load_image()
d_strike.set_colorkey((71, 112, 76))
d_defend = Images('d_defend.png', 240, 255)
d_defend = d_defend.load_image()
d_defend.set_colorkey((71, 112, 76))

# Watcher cards #
vigilance = Images('Vigilance.png', 240, 255)
vigilance = vigilance.load_image()
vigilance.set_colorkey((0, 0, 0))
eruption = Images('Eruption.png', 240, 255)
eruption = eruption.load_image()
eruption.set_colorkey((0, 0, 0))
w_strike = Images('w_strike.png', 240, 255)
w_strike = w_strike.load_image()
w_strike.set_colorkey((71, 112, 76))
w_defend = Images('w_defend.png', 240, 255)
w_defend = w_defend.load_image()
w_defend.set_colorkey((71, 112, 76))


current_screen = start_screen
combat_surf.blit(current_screen, (0, 0))

p1 = None
char = None
mon = Monster('cultist')
card_print = (580, 800)
font_32 = pg.font.Font('Kreon.ttf', 32)
font_25 = pg.font.Font('Kreon.ttf', 25)

running = True
lock = False
start = True
combat = False
action_lock = True
card_select = False


# Set cards #
def set_cards(card):
    if card == 'i_strike':
        return i_strike
    if card == 'i_defend':
        return i_defend
    if card == 'bash':
        return bash

    if card == 's_strike':
        return s_strike
    if card == 's_defend':
        return s_defend
    if card == 'neutralize':
        return neutralize
    if card == 'survivor':
        return survivor

    if card == 'd_strike':
        return d_strike
    if card == 'd_defend':
        return d_defend
    if card == 'zap':
        return zap
    if card == 'dualcast':
        return dualcast

    if card == 'vigilance':
        return vigilance
    if card == 'eruption':
        return eruption
    if card == 'w_strike':
        return w_strike
    if card == 'w_defend':
        return w_defend


# Main game loop #
while running:
    pg.display.flip()
    for event in pg.event.get():

        # Start Screen #
        if start:
            mouse_pos_x, mouse_pos_y = pg.mouse.get_pos()
            print(mouse_pos_x, mouse_pos_y)
            combat_surf.blit(current_screen, (0, 0))
            print('start')

            if not lock:
                if 117 < mouse_pos_x < 371 and 687 < mouse_pos_y < 729:
                    current_screen = play_screen
                    if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                        current_screen = select_character
                        lock = True
                elif 117 < mouse_pos_x < 371 and 969 < mouse_pos_y < 1008:
                    current_screen = quit_screen
                    if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                        pg.quit()
                else:
                    current_screen = start_screen

            if lock:
                if 0 < mouse_pos_x < 267 and 845 < mouse_pos_y < 931 and event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    current_screen = start_screen
                    lock = False
                if 544 < mouse_pos_x < 695 and 806 < mouse_pos_y < 953 and event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    current_screen = ironclad
                if 765 < mouse_pos_x < 915 and 806 < mouse_pos_y < 953 and event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    current_screen = silent
                if 985 < mouse_pos_x < 1135 and 806 < mouse_pos_y < 953 and event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    current_screen = defect
                if 1205 < mouse_pos_x < 1355 and 806 < mouse_pos_y < 953 and event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    current_screen = watcher
                if 1645 < mouse_pos_x < 1920 and 855 < mouse_pos_y < 935 and event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    if current_screen == ironclad:
                        p1 = Player('ironclad')
                        char = ironclad_char
                        combat = True
                    elif current_screen == silent:
                        p1 = Player('silent')
                        char = silent_char
                        combat = True
                    elif current_screen == defect:
                        p1 = Player('defect')
                        char = defect_char
                        combat = True
                    elif current_screen == watcher:
                        p1 = Player('watcher')
                        char = watcher_char
                        combat = True
                    # start = False

            if combat:

                # BG #
                current_screen = level_1

                # Top UI #
                combat_surf.blit(top_bar, (0, 0))

                # Character #
                combat_surf.blit(char, (355, 525))

                # Enemy #
                combat_surf.blit(cultist, (1325, 525))

                # Health Text #
                health_text = font_32.render(str(p1.current_health) + '/' + str(p1.max_health), True, 'red')
                combat_surf.blit(health_text, (300, 10))

                # Gold Text #
                gold_text = font_32.render(str(p1.gold), True, 'yellow')
                combat_surf.blit(gold_text, (475, 10))

                # Deck Size #
                deck_number_text = font_25.render(str(len(p1.deck)), True, 'white')
                combat_surf.blit(deck_number_text, (1810, 40))

                print('hand', len(p1.hand))
                print('deck', p1.draw_pile)
                print('discard', p1.discard_pile)

                # Blit Hand #
                x = 300
                for c in p1.blit_cards:
                    c = set_cards(c)
                    combat_surf.blit(c, (x, 825))
                    x += 120

                if action_lock:
                    if not card_select:
                        p1.take_turn()
                        card_select = True
                    else:
                        p1.end_turn()
                        card_select = False
                        break

                    print('CARDS TO BLIT MAIN', p1.blit_cards)
                    print('hand', len(p1.hand))
                    print('deck', p1.draw_pile)
                    print('discard', p1.discard_pile)

                    action_lock = False
                action_lock = True

            #     print(mon.take_turn())
            # print('end')

            # Update Screen #
            pg.display.flip()

        else:

            pg.quit()

        if event.type == pg.QUIT:
            pg.quit()
