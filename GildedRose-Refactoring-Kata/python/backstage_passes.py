# -*- coding: utf-8 -*-

class Backstage_passes(object):

    def __init__(self, item):
        self.item = item

    def update(self):
        self.increase_quality()

        if self.item.sell_in < 11:
            self.increase_quality()
        if self.item.sell_in < 6:
            self.increase_quality()

        self.item.sell_in -= 1

        if self.item.sell_in < 0:
            self.item.quality = 0

    # The Quality of an item is never more than 50
    def increase_quality(self):
        if self.item.quality < 50:
            self.item.quality += 1
