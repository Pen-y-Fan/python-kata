# -*- coding: utf-8 -*-
class Normal(object):

    def __init__(self, item):
        self.item = item

    def update(self):
        self.item.sell_in -= 1

        self.decrease_quality()

        # Once the sell by date has passed, quality degrades twice as fast
        if self.item.sell_in < 0:
            self.decrease_quality()

    # The quality of an item is never negative
    def decrease_quality(self):
        if self.item.quality > 0:
            self.item.quality -= 1
