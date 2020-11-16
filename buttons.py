from GUI import Button
import actions

button_roll = Button((350,520), "GUI/images/buttons/button_roll_1.png", "GUI/images/buttons/button_roll_2.png", "GUI/images/buttons/button_roll_1.png")
def button_roll_function(game):
    actions.roll_dice(game)

button_buy = Button((250,520), "GUI/images/buttons/button_buy_1.png", "GUI/images/buttons/button_buy_2.png", "GUI/images/buttons/button_buy_1.png")
def button_buy_function(game):
    actions.buy_property(game)


button_pay_rent = Button((250,520), "GUI/images/buttons/button_pay_rent_1.png", "GUI/images/buttons/button_pay_rent_2.png", "GUI/images/buttons/button_pay_rent_1.png")
def button_pay_rent_function(game):
    actions.pay_rent(game)

button_end_turn = Button((450,520), "GUI/images/buttons/button_end_turn_1.png", "GUI/images/buttons/button_end_turn_2.png", "GUI/images/buttons/button_end_turn_1.png")
def button_end_turn_function(game, bought_something):
    return actions.end_turn(game, bought_something)

button_bail = Button((250,520), "GUI/images/buttons/button_bail_1.png", "GUI/images/buttons/button_bail_2.png", "GUI/images/buttons/button_bail_1.png")
def button_bail_function(game):
    actions.pay_bail(game)

button_concede = Button((250,720), "GUI/images/buttons/button_concede_2.png", "GUI/images/buttons/button_concede_1.png", "GUI/images/buttons/button_concede_1.png")
def button_concede_function(game):
    actions.concede(game)
