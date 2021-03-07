# -*- coding: utf-8 -*-
class Conjured_mana_cake(object):

    def __init__(self, item):
        self.item = item

    #  "Conjured" items degrade in Quality twice as fast as normal items
    def update(self):
        self.item.sell_in -= 1

        self.decrease_quality()
        self.decrease_quality()

        if self.item.sell_in < 0:
            self.decrease_quality()
            self.decrease_quality()

    def decrease_quality(self):
        if self.item.quality > 0:
            self.item.quality -= 1
