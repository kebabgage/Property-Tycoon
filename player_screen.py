import pygame
import GUI

def display_player_screen(game):
    board = game.get_board()
    display = board.get_display()

    # player name
    current_player = game.get_turns().current()
    player_string = "Current Player:  " + current_player.getPlayerName()
    player_text = GUI.GameText((700,15), player_string, (255,255,255), 36)
    player_text.show(display)

    # balance
    player_cash = current_player.bankBalance
    cash_string = "Total Cash:  " + "£" +str(player_cash) + " | Total Assets: " + str(current_player.calculate_assets())+ "£ "
    player_text = GUI.GameText((700,60), cash_string, (255,255,255), 36)
    player_text.show(display)

    # display properties
    # props, stations, electricity
    tiles = game.get_board().get_tile_list()
    indices = [1,3,6,8,9,11,13,14,16,18,19,21,23,24,26,27,29,31,32,34,37,39,5,15,25,35,12,28]


    for (i, index) in enumerate(indices):
        current_tile = tiles[index]
        x,y = coordinates[i]
        image = current_tile._image
        if current_tile._owner != current_player:
            image.set_alpha(35)
        else:
            image.set_alpha(255)
        display.blit(GUI.rescale(image, 0.21), (x,y))
        if current_tile._owner == current_player and current_tile._mortgaged:
            mortgage_image.set_alpha(255)
            display.blit(mortgage_image, (x-16,y))

    jail_card_image = pygame.image.load("GUI/images/card_images/card16.png")
    jail_card_image.set_alpha(35)
    if current_player.jail_card:
            jail_card_image.set_alpha(255)
    display.blit(GUI.rescale(jail_card_image,0.21), (700, 362))




mortgage_image = GUI.rescale(pygame.image.load("GUI/images/mortgage.png"), 0.12)

# player screen tile coordinates
y1 = 120
dy = 77
y2 = y1 + dy
y3 = y1 + 2*dy
y4 = y1 + 3*dy
x0 = 700
dx = 70
coordinates = [
# brown
(x0, y1),
(x0, y2),
# blue
(x0+dx, y1),
(x0+dx, y2),
(x0+dx, y3),
# purple
(x0+2*dx, y1),
(x0+2*dx, y2),
(x0+2*dx, y3),
# orange
(x0+3*dx, y1),
(x0+3*dx, y2),
(x0+3*dx, y3),
# red
(x0+4*dx, y1),
(x0+4*dx, y2),
(x0+4*dx, y3),
# yellow
(x0+5*dx, y1),
(x0+5*dx, y2),
(x0+5*dx, y3),
# green
(x0+6*dx, y1),
(x0+6*dx, y2),
(x0+6*dx, y3),
# blue
(x0+7*dx, y1),
(x0+7*dx, y2),
# station
(x0+8*dx, y1),
(x0+8*dx, y2),
(x0+8*dx, y3),
(x0+8*dx, y4),
# utilities
(x0+9*dx, y1),
(x0+9*dx, y2)
]
