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
s_energy = Images('s_energy.jpg', 100, 100)
s_energy = s_energy.load_image()
s_energy.set_colorkey((0, 0, 0))
d_energy = Images('d_energy.jpg', 100, 100)
d_energy = d_energy.load_image()
d_energy.set_colorkey((0, 0, 0))
w_energy = Images('w_energy.jpg', 100, 100)
w_energy = w_energy.load_image()
w_energy.set_colorkey((0, 0, 0))

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
end_turn = Images('end_turn.png', 190, 80)
end_turn = end_turn.load_image()

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
energy = None
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
clicked_card_index = None
second = False
selected_card = None
not_str_selected_card = None
is_card_selected = False
click_count = 0  # Variable to count left clicks


# Set cards #
def set_cards(card):
    if card == 'i_strike':
        return i_strike
    if card == i_strike:
        return 'i_strike'
    if card == 'i_defend':
        return i_defend
    if card == i_defend:
        return 'i_defend'
    if card == 'bash':
        return bash
    if card == bash:
        return 'bash'

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
                        energy = i_energy
                        combat = True
                    elif current_screen == silent:
                        p1 = Player('silent')
                        char = silent_char
                        energy = s_energy
                        combat = True
                    elif current_screen == defect:
                        p1 = Player('defect')
                        char = defect_char
                        energy = d_energy
                        combat = True
                    elif current_screen == watcher:
                        p1 = Player('watcher')
                        char = watcher_char
                        energy = w_energy
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

                # Health #
                monster_health_text = font_25.render(str(mon.health) + '/' + str(mon.max_health), True, 'white')
                combat_surf.blit(monster_health_text, (1395, 780))
                player_health_text = font_25.render(str(p1.current_health) + '/' + str(p1.max_health), True, 'white')
                combat_surf.blit(player_health_text, (430, 785))

                # Block #
                player_block = font_25.render(str(p1.block), True, 'white')
                combat_surf.blit(player_block, (370, 785))
                monster_block = font_25.render(str(mon.block), True, 'white')
                combat_surf.blit(monster_block, (1320, 780))

                # Gold Text #
                gold_text = font_32.render(str(p1.gold), True, 'yellow')
                combat_surf.blit(gold_text, (475, 10))

                # Deck Size #
                deck_number_text = font_25.render(str(len(p1.deck)), True, 'white')
                combat_surf.blit(deck_number_text, (1810, 40))

                # Energy #
                combat_surf.blit(energy, (113, 793))
                energy_text = font_25.render(str(p1.current_energy) + '/' + str(p1.max_energy), True, 'black')
                combat_surf.blit(energy_text, (145, 830))

                # End turn #
                combat_surf.blit(end_turn, (1630, 820))

                print('hand', len(p1.hand))
                print('deck', p1.draw_pile)
                print('discard', p1.discard_pile)

                # Blit Hand #
                x = 300
                for c in p1.blit_cards:
                    c = set_cards(c)
                    combat_surf.blit(c, (x, 825))
                    x += 120

                # Player taking turn #
                if action_lock:
                    if not card_select:
                        print('not card_select')
                        p1.take_turn()
                        card_select = True
                    else:
                        if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                            mouse_x, mouse_y = pg.mouse.get_pos()

                            # Check if the click is on a card in the player's hand
                            for i, card_position in enumerate(zip(range(300, 900, 120), [825] * len(p1.hand))):
                                x, y = card_position

                                # Check if the mouse click is within the bounding box of the card
                                if x < mouse_pos_x < x + 120 and y < mouse_pos_y < y + 255:
                                    clicked_card_index = i
                                    print(p1.hand[clicked_card_index], 'THIS CARD')
                                    not_str_selected_card = p1.hand[clicked_card_index]
                                    selected_card = set_cards(p1.hand[clicked_card_index])
                                    is_card_selected = True
                                    click_count += 1

                        if click_count == 1:
                            # Check if the second click occurs anywhere on the screen
                            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                                click_count += 1
                            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 3:
                                click_count = 0
                                is_card_selected = False
                                selected_card = None
                                not_str_selected_card = None

                        if click_count == 2:
                            print(click_count, 'click')
                            mouse_x, mouse_y = pg.mouse.get_pos()

                            if is_card_selected:
                                tmp_card_var = p1.play_card(not_str_selected_card)
                                print('DAMAGE?', tmp_card_var)
                                if tmp_card_var >= 0:
                                    print('HAPPENING')
                                    print(tmp_card_var, 'ERROR?')
                                    mon.take_damage(tmp_card_var)
                                click_count = 0  # Reset the click count
                                is_card_selected = False  # Reset the card selection

                        if is_card_selected:
                            mouse_x, mouse_y = pg.mouse.get_pos()
                            combat_surf.blit(selected_card, (mouse_x, mouse_y))

                        if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                            mouse_x, mouse_y = pg.mouse.get_pos()
                            if 1630 <= mouse_x <= 1820 and 820 <= mouse_y <= 900:
                                p1.end_turn()
                                mon.take_turn()

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
