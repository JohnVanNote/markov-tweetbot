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

    SOL = '\0'
    EOL = '\1'


    def get_sol_str(self):
        return self.SOL


    def get_eol_str(self):
        return self.EOL


    def __init__(self, lines):
        """Initializes Data Structure"""
        self.dictionary = {}
        for line in lines:
            self.add(line)


    def add(self, line):
        """Adds Line to the Dictionary"""
        
        self.add_words(line.split())


    def add_words(self, words):
        """Adds a list of words to the chain"""

        if not isinstance(words, list):
            raise TypeError("Word List must be and instance of a list")

        start = self.get_sol_str()
        end = self.get_eol_str()

        # Start of line
        prev_word = start

        for word in words:
            self.add_word(prev_word, word)
            prev_word = word

        # End of line
        self.add_word(prev_word, end)


    def add_word(self, prev_word, word):
        """Adds/Updates word in dictionary"""

        if not isinstance(word, str):
            raise TypeError("Word must be and instance of a String")

        if not prev_word in self.dictionary:
            self.dictionary[prev_word] = []
        self.dictionary[prev_word].append(word)


    def get_dictionary(self):
        """Gets Dictionary"""
        return self.dictionary


    def generate_line(self):
        """Generates a new line based on the dictionary"""

        start = self.get_sol_str()
        end = self.get_eol_str()

        line = ""
        is_not_done = True
        word = random.choice(self.dictionary[start])

        while is_not_done:
            line += word + " "
            next_word_list = self.dictionary[word]
            next_word = random.choice(next_word_list)
            if next_word != self.get_eol_str():
                word = next_word
            else:
                is_not_done = False
        return line
