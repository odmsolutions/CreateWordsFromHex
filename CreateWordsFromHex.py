"""A script/library that will take a block of hex bytes-
a mac address, sha1 or similar, along with a dictionary,
and convert it into a phrase.
The intent is to then have unique generated memorable phrases."""

def _split_into_chunks_of_2(string):
    """Generate string pairs of 2 Characters from a string of digits"""
    if ":" in string:
        string = string.replace(':','')
    while len(string) > 0:
        yield string[:2]
        string = string[2:]

def digit_pairs_to_numbers(digitpairs):
    """Generate digit pairs from iterable of number values"""
    for pair in digitpairs:
        yield int(pair,16)

def _hash_numbers(numbers, length):
    '''Return a hash of the desired length for the given numbers. 0 padded'''
    max_hash_size = 16 ** length
    hash = 0
    for number in numbers:
        hash *= 17
        hash += number
    hash %= max_hash_size
    digits = hex(hash).split('x')[1]
    digits = digits.rjust(length, '0')
    if digits.endswith('L'):
        digits = digits[:-1]
    return digits

def get_shortened_hash(digits, length):
    '''Given a list of digits, get a shorter hashed set'''
    digit_list = _split_into_chunks_of_2(digits)
    return _hash_numbers(
                         digit_pairs_to_numbers(digit_list),
                         length
                         )

def _numbers_from_digits(digits_string):
    '''Generate numbers from a digits string'''
    return digit_pairs_to_numbers(_split_into_chunks_of_2(digits_string))
    
def _numbers_from_text(text):
    '''Generates a list of numbers from a text parameter'''
    for char in text:
        yield ord(char)

def _salt_numbers(numbers, salt):
    '''Generate a list of salted numbers. Salt is a list of numbers'''
    salt_list = list(salt)
    current_salt = 0
    for number in numbers:
        yield salt_list[current_salt] + number
        current_salt += 1
        current_salt %= len(salt_list)

def get_short_salted_string_hash(text, salt, desired_length):
    return _hash_numbers(
                         _salt_numbers(
                                       _numbers_from_text(text), 
                                       _numbers_from_digits(salt)), 
                         desired_length)

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
        """Generate words from a list of numbers and a dictionary"""
        words = []
        offset = 0
        for number in numbers:
            offset += number
            offset %= len(self._dictionary)
            words.append(self._dictionary[offset])
        return words
    
    def convert(self, digits):
        """Convert the string of hex digits to a list of words from the dictionary.
        For now assume pairs of 2 digits."""
        digitpairs = _split_into_chunks_of_2(digits)
        numbers = digit_pairs_to_numbers(digitpairs)
        wordlist = self.words_from_numbers(numbers)
        return wordlist

    def getHashedWordsFromText(self, text, salt, desired_length):
        '''Hash the text, using the salt, into a list of words at the desired length'''
        hash = get_short_salted_string_hash(text, salt, desired_length * 2)
        print hash
        return self.convert(hash)