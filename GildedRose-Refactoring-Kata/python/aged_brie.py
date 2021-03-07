# -*- coding: utf-8 -*-
class Aged_brie(object):

    def __init__(self, item):
        self.item = item

    def update(self):
        self.item.sell_in -= 1

        self.increase_quality()

        if self.item.sell_in < 0:
            self.increase_quality()

    # The Quality of an item is never more than 50
    def increase_quality(self):
        if self.item.quality < 50:
            self.item.quality += 1
