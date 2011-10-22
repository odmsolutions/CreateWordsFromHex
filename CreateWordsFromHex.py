"""A script/library that will take a block of hex bytes-
a mac address, sha1 or similar, along with a dictionary,
and convert it into a phrase.
The intent is to then have unique generated memorable phrases."""

def split_into_chunks_of_2(string):
    """Split A String pairs of 2 Characters"""
    items = []
    while len(string) > 0:
        items.append(string[:2])
        string = string[2:]
    return items

def digit_pairs_to_numbers(digitpairs):
    """Convert a list of digit pairs to number values"""
    numbers = []
    for pair in digitpairs:
        numbers.append(int(pair,16))
    return numbers

class Converter:
    """Object for converting digits to a list of words from a dictionary"""
    
    def set_dictionary_from_file(self, filename):
        """Set the dictionary to use from a file"""
        fd = open(filename)
        self._dictionary = fd.read().splitlines()
        
    def set_dictionary_from_list(self, dictionary):
        """Set the dictionary to use from a list"""
        self._dictionary = dictionary
        
    def get_dictionary(self):
        """Get the dictionary list"""
        return self._dictionary
        
    def words_from_numbers(self, numbers):
        """Create a list of words from a list of numbers and a dictionary"""
        words = []
        for number in numbers:
            words.append(self._dictionary[number])
        return words
    
    def convert(self, digits):
        """Convert the string of hex digits to a list of words from the dictionary.
        For now assume pairs of 2 digits."""
        digitpairs = split_into_chunks_of_2(digits)
        numbers = digit_pairs_to_numbers(digitpairs)
        wordlist = self.words_from_numbers(numbers)
        return wordlist

