# -*- coding: utf-8 -*-
from aged_brie import Aged_brie
from backstage_passes import Backstage_passes
from conjured_mana_cake import Conjured_mana_cake
from normal import Normal
from sulfuras_hand_of_ragnaros import Sulfuras_hand_of_ragnaros


class GildedRose(object):

    def __init__(self, items):
        self.items = []
        for item in items:
            if item.name == "Aged Brie":
                self.items.append(Aged_brie(item))
                continue

            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.items.append(Backstage_passes(item))
                continue

            if item.name == "Sulfuras, Hand of Ragnaros":
                self.items.append(Sulfuras_hand_of_ragnaros(item))
                continue

            if item.name == "Conjured Mana Cake":
                self.items.append(Conjured_mana_cake(item))
                continue

            self.items.append(Normal(item))

    def update_quality(self):
        for item in self.items:
            item.update()
