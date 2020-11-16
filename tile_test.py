from tile import *
import unittest
import pygame

class TileTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.base_property = PropertyTile(1, 'Property_Name', 'Action', True, 66, 100, 101, 102, 103, 104, 300)
        self.base_property2 = PropertyTile(11, 'Property_Name2', 'Action', False, 66, 100, 101, 102, 103, 104, 300)


    @classmethod
    def tearDown(self):
        self.base_property = None
        self.base_property2 = None


    def test_property_positon(self):
        # Assert that the correct position has been assigned
        self.assertEqual(self.base_property.get_position(), 1)

    def test_property_name(self):
        # Assert that the correct name has been assigned
        self.assertEqual(self.base_property.get_name(), 'Property_Name')

    def test_can_be_bought(self):
        # Assert that a tile is correctly assigned whether it can be bought
        self.assertTrue(self.base_property.can_be_bought(), True)
        self.assertFalse(self.base_property2.can_be_bought(), False)

class PropertyTest(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.base_property = PropertyTile(1, 'Property_Name', 'Action', True, 66, 100, 101, 102, 103, 104, 300)

    @classmethod
    def tearDown(self):
        self.base_property = None

    def test_property_action(self):
        # Assert that the correct action has not been assigned in property
        self.assertIsNone(self.base_property.get_action())

    def test_property_cost(self):
        # Assert that correct cost as has been assigned
        self.assertTrue(self.base_property.get_cost(), 66)

    def test_add_house(self):
        # Assert that a house can be added
        self.assertEqual(self.base_property.add_house(), 1)
        self.assertEqual(self.base_property.get_house_count(), 1)

        # Assert that a second house can be added
        self.assertEqual(self.base_property.add_house(), 1)
        self.assertEqual(self.base_property.get_house_count(), 2)

    def test_add_hotel(self):

        # Assert that a hotel cannot be added without 4 initial houses
        self.assertEqual(self.base_property.add_hotel(), 0)

        # Assert that a hotel can be added if 4 houses are already purchased
        self.base_property.add_house()
        self.base_property.add_house()
        self.base_property.add_house()
        self.base_property.add_house()
        self.assertEqual(self.base_property.add_hotel(), 1)

        # Assert that the houses are removed from the property
        self.assertEqual(self.base_property.get_house_count(), 0)

        # Assert that a second hotel cannot be added
        self.assertEqual(self.base_property.add_hotel(), 0)


    def test_rent_initial(self):

        # Assert that the correct base rent has been assigned with no hotels and houses
        self.assertEqual(self.base_property.get_house_count(), 0)
        self.assertEqual(self.base_property.get_hotel_count(), 0)
        self.assertEqual(self.base_property.get_rent(), 100)

    def test_rent_house1(self):

        self.base_property.add_house()

        # Assert that a house can be added to a property and the rent changes
        self.assertEqual(self.base_property.get_house_count(), 1)
        self.assertEqual(self.base_property.get_hotel_count(), 0)

        # Assert that the rent increases with an increase of houses on the property
        # (The property already has one house)
        self.assertEqual(self.base_property.get_rent(), 101)

    def test_rent_house2(self):

        self.base_property.add_house()
        self.base_property.add_house()                   # Two houses are added

        self.assertEqual(self.base_property.get_house_count(), 2)
        self.assertEqual(self.base_property.get_hotel_count(), 0)
        self.assertEqual(self.base_property.get_rent(), 102)

    def test_rent_house3(self):

        self.base_property.add_house()
        self.base_property.add_house()
        self.base_property.add_house()                   # Three houses are added

        self.assertEqual(self.base_property.get_house_count(), 3)
        self.assertEqual(self.base_property.get_hotel_count(), 0)
        self.assertEqual(self.base_property.get_rent(), 103)

    def test_rent_house4(self):

        self.base_property.add_house()
        self.base_property.add_house()
        self.base_property.add_house()
        self.base_property.add_house()                   # Four houses are added

        self.assertEqual(self.base_property.get_house_count(), 4)
        self.assertEqual(self.base_property.get_hotel_count(), 0)
        self.assertEqual(self.base_property.get_rent(), 104)

    def test_rent_hotel(self):

        self.base_property.add_house()
        self.base_property.add_house()
        self.base_property.add_house()
        self.base_property.add_house()
        self.base_property.add_hotel()                   # A hotel is added

        self.assertEqual(self.base_property.get_house_count(), 0)
        self.assertEqual(self.base_property.get_hotel_count(), 1)
        self.assertEqual(self.base_property.get_rent(), 300)


if __name__ == '__main__':
    unittest.main()
