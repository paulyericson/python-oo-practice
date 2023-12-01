"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    
    def __init__(self, path):
        '''reads dictionary and reporst the amount of words'''
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        '''parses words in dict_file'''
        return [w.strip() for w in dict_file]
    
    def random(self):
        '''returns a random word'''
        return random.choice(self.words)
    
