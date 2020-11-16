import unittest
from player import Player

class BoardTestCases(unittest.TestCase):

    def setUp(self):
        self.player = Player("Tom", "Boot")

    def test_get_player_name(self):
        curr_name = "Tom"
        self.assertEqual(self.player.getPlayerName(), curr_name)

    def test_set_player_name(self):
        new_name = "Jim"
        self.player.setPlayerName(new_name)
        self.assertEqual(self.player.getPlayerName(), new_name)

    def test_get_token_name(self):
        curr_token = "Boot"
        self.assertEqual(self.player.getTokenName(), curr_token)

    def test_set_token_name(self):
        new_token = "Thimble"
        self.player.setTokenName(new_token)
        self.assertEqual(self.player.getTokenName(), new_token)

    def test_get_bank_balance(self):
        self.assertEqual(self.player.getBankBalance(),1500)

    def test_set_bank_balance(self):
        new_balance = 2000
        self.player.setBankBalance(new_balance)
        self.assertEqual(self.player.getBankBalance(), new_balance)

    def test_add_bank_balance(self):
        added_amount = 500
        balance = self.player.getBankBalance() + added_amount
        self.player.addBankBalance(added_amount)
        self.assertEqual(self.player.getBankBalance(), balance)

    def test_remove_bank_balance(self):
        removed_amount = 200
        balance = self.player.getBankBalance() - removed_amount
        self.player.removeBankBalance(removed_amount)
        self.assertEqual(self.player.getBankBalance(), balance)

    def test_get_position(self):
        self.assertEqual(self.player.getPosition(), 0)

    def test_set_position(self):
        new_position = 2
        self.player.setPosition(new_position)
        self.assertEqual(self.player.getPosition(), new_position)

    def test_get_jailtime_count(self):
        self.assertEqual(self.player.getJailTimeCount(), 0)

    def test_set_jailtime_count(self):
        new_jailtime = 2
        self.player.setJailTimeCount(new_jailtime)
        self.assertEqual(self.player.getJailTimeCount(), new_jailtime)

    def test_get_has_won(self):
        self.assertEqual(self.player.getHasWon(), False)

    def test_set_has_won(self):
        self.player.setHasWon()
        self.assertEqual(self.player.getHasWon(), True)

    def test_get_in_jail(self):
        self.assertEqual(self.player.getInJail(), False)

    def test_set_in_jail(self):
        new_injail = True
        self.player.setInJail(new_injail)
        self.assertEqual(self.player.getInJail(), new_injail)

    def has_no_cash_true(self):
        bank_balance = 0
        self.player.setBankBalance(bank_balance)
        self.assertEqual(self.player.has_no_cash(), True)

    def has_no_cash_false(self):
        bank_balance = 100
        self.player.setBankBalance(bank_balance)
        self.assertEqual(self.player.has_no_cash(), False)

    def test_calculate_assets(self):
        self.player.addPropertyOwned("Property 1")
        self.player.addPropertyOwned("Property 2")
        self.player.addPropertyOwned("Property 3")
        self.player.addPropertyOwned("Property 1")

if __name__ == '__main__':
    unittest.main()
