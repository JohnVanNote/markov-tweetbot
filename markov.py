#!/usr/bin/env python
#
# John Van Note <johnlvannote@protonmail.com>
#
##

import random
import sys

line1 = "This is a test line"
line2 = "This is another test line";
line3 = "Look here, another test line"
line4 = "Probably should have another test line that ends differently"
line5 = "You want it to be one way"
line6 = "But it's the other way"
line7 = "I need more test lines"
line8 = "Need to increase randomness"
line9 = "Who knows how to do that"
line10 = "Maybe some way to only chooses \'starter\' words"
line11 = "Like the first word in a line"
line12 = "I could potentially get into a circular line with this implementation"

class Markov: 
  END_OF_LINE = "\0"
  DEFAULT = "\1"

  def __init__(self, lines):
    self.markovDict =  {}
    for line in lines:
      self.add(line)

  def add(self, line):
    words = self.parseLine(line)
    lastword = self.DEFAULT
    for word in words:
      if not word in self.markovDict:
        self.markovDict[word] = []
      if not lastword == "": 
        self.markovDict[lastword].append(word)
      lastword = word
    self.markovDict[lastword].append(self.END_OF_LINE)

  def parseLine(self, line):
    return line.split()

  def getDictionary(self):
    return self.markovDict

  def generateLine(self):
    line = ""
    randomKey = random.choice(self.markovDict.keys())
    isDone = False
    word = randomKey
    while not isDone:
      line += word + " "
      nextWordList = self.markovDict[word]
      nextWord = random.choice(nextWordList)
      if (not nextWord == self.END_OF_LINE) and (len(line) < 140):
        word = nextWord
      else:
        isDone = True
    return line

def main(arg=sys.argv):
  lines = []

  if len(arg) < 2:  
    lines.append(line1)
    lines.append(line2)
    lines.append(line3)
    lines.append(line4)
    lines.append(line5)
    lines.append(line6)
    lines.append(line7)
    lines.append(line8)
    lines.append(line9)
    lines.append(line10)
    lines.append(line11)
    lines.append(line12)

  else:
    file = open(arg[1], 'r')
    allLines = file.read()
    lines = allLines.strip().split('\n')

  print(lines)

  markov = Markov(lines)
  mdict = markov.getDictionary()
  print mdict
  print markov.generateLine()
  print markov.generateLine()
  print markov.generateLine()
  

if __name__ == "__main__":
  main()
