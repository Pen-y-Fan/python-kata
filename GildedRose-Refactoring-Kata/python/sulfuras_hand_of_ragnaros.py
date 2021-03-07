# -*- coding: utf-8 -*-

class Sulfuras_hand_of_ragnaros(object):

    def __init__(self, item):
        self.item = item

    # "Sulfuras", being a legendary item, never has to be sold or decreases in Quality
    def update(self):
        pass
