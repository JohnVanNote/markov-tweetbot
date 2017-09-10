#!/usr/bin/env python
#
# MarkovChain.py
#
# John Van Note
#
#

"""Markov Chain Data Structure"""

import random

class MarkovChain(object):
    """Markov Chain Data Structure"""

    END_OF_LINE = "\0"
    DEFAULT = "\1"

    def __init__(self, lines):
        """Initializes Data Structure"""
        self.dictionary = {}
        for line in lines:
            self.add(line)

    def add(self, line):
        """Adds Line to the Dictionary"""
        words = line.split()
        last_word = self.DEFAULT
        for word in words:
            if not word in self.dictionary:
                self.dictionary[word] = []
            if last_word != "":
                self.dictionary[last_word].append(word)
            last_word = word
        self.dictionary[last_word].append(self.END_OF_LINE)

    def get_dictionary(self):
        """Gets Dictionary"""
        return self.dictionary

    def generate_line(self):
        """Generates a new line based on the dictionary"""
        line = ""
        random_key = random.choice(self.dictionary.keys())
        is_not_done = True
        word = random_key
        while is_not_done:
            line += word + " "
            next_word_list = self.dictionary[word]
            next_word = random.choice(next_word_list)
            if next_word != self.END_OF_LINE:
                word = next_word
            else:
                is_not_done = False
        return line
