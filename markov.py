#!/usr/bin/env python
#
# John Van Note <johnlvannote@protonmail.com>
#
# markov.py
#

"""Test Main For MarkovChain'ing"""

import sys
from MarkovChain import MarkovChain

def get_default_lines():
    """Default Lines for testing"""

    default_lines = []
    default_lines.append("This is a test line")
    default_lines.append("This is another test line")
    default_lines.append("Look here, another test line")
    default_lines.append("Probably should have another test line that ends differently")
    default_lines.append("You want it to be one way")
    default_lines.append("But it's the other way")
    default_lines.append("I need more test lines")
    default_lines.append("Need to increase randomness")
    default_lines.append("Who knows how to do that")
    default_lines.append("Maybe some way to only chooses \'starter\' words")
    default_lines.append("Like the first word in a line")
    default_lines.append("I could potentially get into a circular line with this implementation")

    return default_lines

def main(arg=None):
    """Main Function"""

    lines = []
    arg = sys.argv

    if len(arg) < 2:
        lines = get_default_lines()
    else:
        input_file = open(arg[1], 'r')
        raw_lines = input_file.read()
        lines = raw_lines.strip().split('\n')

    print lines

    markov_chain = MarkovChain(lines)
    markov_dict = markov_chain.get_dictionary()
    print markov_dict
    print markov_chain.generate_line()
    print markov_chain.generate_line()
    print markov_chain.generate_line()

if __name__ == "__main__":
    main()
