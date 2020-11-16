import unittest
import testfixtures
from testfixtures import compare
import json
from tile import ActionTile, PropertyTile
from board import *

class BoardTestCases(unittest.TestCase):

    #creating and formatting sample json objects
    json_property_tile = { 'Position' : 2, 'Space/property' : 'Crapper Street', 'Group' : 'Brown', 'Action' : None, 'Can be bought?' : True, 'Cost' : 60, 'Rent (unimproved)' : 2, '1 house' : 10, '2 houses' : 30, '3 houses' : 90, '4 houses' : 150, '1 hotel' : 200, 'image' : 'GUI/images/property_cards/GO.png' }
    json_action_tile = { 'Position' : 1, 'Space/property' : 'Go', 'Group' : None, 'Action' : 'Collect £200', 'Can be bought?' : False, 'Cost' : None, 'Rent (unimproved)' : None, '1 house' : None, '2 houses' : None, '3 houses' : None, '4 houses' : None, '1 hotel' : None, 'image' : 'GUI/images/property_cards/GO.png' }
    json_action_tile_update = { 'Position' : 1, 'Space/property' : 'Go', 'Group' : None, 'Action' : 'Collect £200', 'Can be bought?' : False, 'image' : 'GUI/images/property_cards/GO.png' }

    json_dump_property_tiles = json.dumps(json_property_tile)
    json_dump_action_tiles = json.dumps(json_action_tile)
    json_dump_action_tiles_update = json.dumps(json_action_tile_update)

    json_object_property_tiles = json.loads(json_dump_property_tiles)
    json_object_action_tiles = json.loads(json_dump_action_tiles)
    json_object_action_tiles_update = json.loads(json_dump_action_tiles_update)

    #creating sample Action and Property tiles
    sample_action_tile = ActionTile(1,'Go','Collect £200',False,'GUI/images/property_cards/GO.png')
    print(sample_action_tile)
    sample_property_tile = PropertyTile(2,'Crapper Street', 'Brown', 60, 2, 10, 30, 90, 150, 200, True, 'GUI/images/property_cards/CS.png')
    print(sample_property_tile)

    #sets up board widget and sample json objects
    def setUp(self):
        self.board = Board()

    #Test: populate board and return tile at specific position
    def test_populate_board(self):
        self.board.populate_board()
        self.assertIsNotNone(self.board._tile_list)
        sample_tile = self.board._tile_list[2]
        self.assertEqual(self.board.get_tile_at(2),sample_tile)

    #Test: create tile that can not be bought
    #this will fail; was not able to find a way to compare tile objects
    def test_create_tile_not_bought(self):
        self.assertEqual(self.board.create_tile(self.json_object_action_tiles).__dict__, self.sample_action_tile.__dict__)


    #Test: create tile that can be bought
    #this will fail; was not able to find a way to compare tile objects
    def test_create_tile_bought(self):
        self.assertEqual(self.board.create_tile(self.json_object_property_tiles),self.sample_property_tile)

    #Test: return list of tiles
    def test_get_tile_list(self):
        self.assertEqual(self.board.get_tile_list(), self.board._tile_list)

if __name__ == '__main__':
    unittest.main()
