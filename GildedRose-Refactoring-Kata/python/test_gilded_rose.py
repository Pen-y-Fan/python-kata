# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from item import Item


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("fixme", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("fixme", items[0].name)

    def test_dexterity_vest(self):
        items = [Item("+5 Dexterity Vest", 10, 20)]
        gilded_rose = GildedRose(items)

        expected_data = [
            ["+5 Dexterity Vest", 9, 19],
            ["+5 Dexterity Vest", 8, 18],
            ["+5 Dexterity Vest", 7, 17],
            ["+5 Dexterity Vest", 6, 16],
            ["+5 Dexterity Vest", 5, 15],
            ["+5 Dexterity Vest", 4, 14],
            ["+5 Dexterity Vest", 3, 13],
            ["+5 Dexterity Vest", 2, 12],
            ["+5 Dexterity Vest", 1, 11],
            ["+5 Dexterity Vest", 0, 10],
            ["+5 Dexterity Vest", -1, 8],
            ["+5 Dexterity Vest", -2, 6],
            ["+5 Dexterity Vest", -3, 4],
            ["+5 Dexterity Vest", -4, 2],
            ["+5 Dexterity Vest", -5, 0],
            ["+5 Dexterity Vest", -6, 0],
            ["+5 Dexterity Vest", -7, 0],
            ["+5 Dexterity Vest", -8, 0],
            ["+5 Dexterity Vest", -9, 0],
        ]

        for expected in expected_data:
            gilded_rose.update_quality()
            self.assertEqual(expected[0], items[0].name)
            self.assertEqual(expected[1], items[0].sell_in)
            self.assertEqual(expected[2], items[0].quality)

    def test_aged_brie(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)

        expected_data = [
            # "name"
            # "sell_in"
            # "quality"
            {"name": "Aged Brie", "sell_in": 1, "quality": 1},
            {"name": "Aged Brie", "sell_in": 0, "quality": 2},
            {"name": "Aged Brie", "sell_in": -1, "quality": 4},
            {"name": "Aged Brie", "sell_in": -2, "quality": 6},
            {"name": "Aged Brie", "sell_in": -3, "quality": 8},
            {"name": "Aged Brie", "sell_in": -4, "quality": 10},
            {"name": "Aged Brie", "sell_in": -5, "quality": 12},
            {"name": "Aged Brie", "sell_in": -6, "quality": 14},
            {"name": "Aged Brie", "sell_in": -7, "quality": 16},
            {"name": "Aged Brie", "sell_in": -8, "quality": 18},
            {"name": "Aged Brie", "sell_in": -9, "quality": 20},
            {"name": "Aged Brie", "sell_in": -10, "quality": 22},
            {"name": "Aged Brie", "sell_in": -11, "quality": 24},
            {"name": "Aged Brie", "sell_in": -12, "quality": 26},
            {"name": "Aged Brie", "sell_in": -13, "quality": 28},
            {"name": "Aged Brie", "sell_in": -14, "quality": 30},
            {"name": "Aged Brie", "sell_in": -15, "quality": 32},
            {"name": "Aged Brie", "sell_in": -16, "quality": 34},
            {"name": "Aged Brie", "sell_in": -17, "quality": 36},
        ]

        for expected in expected_data:
            gilded_rose.update_quality()
            self.assertEqual(expected["name"], items[0].name)
            self.assertEqual(expected["sell_in"], items[0].sell_in)
            self.assertEqual(expected["quality"], items[0].quality)

    def test_elixir_of_the_mongoose(self):
        items = [Item("Elixir of the Mongoose", 5, 7)]
        gilded_rose = GildedRose(items)

        expected_data = [
            ["Elixir of the Mongoose", 4, 6],
            ["Elixir of the Mongoose", 3, 5],
            ["Elixir of the Mongoose", 2, 4],
            ["Elixir of the Mongoose", 1, 3],
            ["Elixir of the Mongoose", 0, 2],
            ["Elixir of the Mongoose", -1, 0],
            ["Elixir of the Mongoose", -2, 0],
            ["Elixir of the Mongoose", -3, 0],
            ["Elixir of the Mongoose", -4, 0],
            ["Elixir of the Mongoose", -5, 0],
            ["Elixir of the Mongoose", -6, 0],
            ["Elixir of the Mongoose", -7, 0],
            ["Elixir of the Mongoose", -8, 0],
            ["Elixir of the Mongoose", -9, 0],
            ["Elixir of the Mongoose", -10, 0],
            ["Elixir of the Mongoose", -11, 0],
            ["Elixir of the Mongoose", -12, 0],
            ["Elixir of the Mongoose", -13, 0],
            ["Elixir of the Mongoose", -14, 0],
        ]

        for expected in expected_data:
            gilded_rose.update_quality()
            self.assertEqual(expected[0], items[0].name)
            self.assertEqual(expected[1], items[0].sell_in)
            self.assertEqual(expected[2], items[0].quality)

    def test_sulfuras_hand_of_ragnaros(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        gilded_rose = GildedRose(items)

        expected_data = [
            ["Sulfuras, Hand of Ragnaros", 0, 80],
            ["Sulfuras, Hand of Ragnaros", 0, 80],

        ]

        for expected in expected_data:
            gilded_rose.update_quality()
            self.assertEqual(expected[0], items[0].name)
            self.assertEqual(expected[1], items[0].sell_in)
            self.assertEqual(expected[2], items[0].quality)

    def test_backstage_passes_to_a_tafkal80etc_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gilded_rose = GildedRose(items)

        expected_data = [
            ["Backstage passes to a TAFKAL80ETC concert", 14, 21],
            ["Backstage passes to a TAFKAL80ETC concert", 13, 22],
            ["Backstage passes to a TAFKAL80ETC concert", 12, 23],
            ["Backstage passes to a TAFKAL80ETC concert", 11, 24],
            ["Backstage passes to a TAFKAL80ETC concert", 10, 25],
            ["Backstage passes to a TAFKAL80ETC concert", 9, 27],
            ["Backstage passes to a TAFKAL80ETC concert", 8, 29],
            ["Backstage passes to a TAFKAL80ETC concert", 7, 31],
            ["Backstage passes to a TAFKAL80ETC concert", 6, 33],
            ["Backstage passes to a TAFKAL80ETC concert", 5, 35],
            ["Backstage passes to a TAFKAL80ETC concert", 4, 38],
            ["Backstage passes to a TAFKAL80ETC concert", 3, 41],
            ["Backstage passes to a TAFKAL80ETC concert", 2, 44],
            ["Backstage passes to a TAFKAL80ETC concert", 1, 47],
            ["Backstage passes to a TAFKAL80ETC concert", 0, 50],
            ["Backstage passes to a TAFKAL80ETC concert", -1, 0],
            ["Backstage passes to a TAFKAL80ETC concert", -2, 0],
            ["Backstage passes to a TAFKAL80ETC concert", -3, 0],
            ["Backstage passes to a TAFKAL80ETC concert", -4, 0],

        ]

        for expected in expected_data:
            gilded_rose.update_quality()
            self.assertEqual(expected[0], items[0].name)
            self.assertEqual(expected[1], items[0].sell_in)
            self.assertEqual(expected[2], items[0].quality)

    def test_conjured_mana_cake(self):
        items = [Item("Conjured Mana Cake", 3, 11)]
        gilded_rose = GildedRose(items)

        expected_data = [
            ["Conjured Mana Cake", 2, 9],
            ["Conjured Mana Cake", 1, 7],
            ["Conjured Mana Cake", 0, 5],
            ["Conjured Mana Cake", -1, 1],
            ["Conjured Mana Cake", -2, 0],
            ["Conjured Mana Cake", -3, 0],
        ]

        for expected in expected_data:
            gilded_rose.update_quality()
            self.assertEqual(expected[0], items[0].name)
            self.assertEqual(expected[1], items[0].sell_in)
            self.assertEqual(expected[2], items[0].quality)


if __name__ == '__main__':
    unittest.main()
