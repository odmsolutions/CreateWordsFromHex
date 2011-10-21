"""Small script to prepare data for a word list"""
import sys

#Converting comma seperated bunches of words into a single wordlist.

def make_word_list(input_filename, output_filename):
    """Given an input filename to read from, and an output filename to write to,
    this will read in comma and newline seperated values, strip out extra spaces.
    It will strip out words with less than 3 characters.
    It will then write the output, a word per line, to an output filename"""
    word_list = open(input_filename).read().replace(" ",'').split(",")
    filtered_list = filter(lambda word: len(word) > 3, word_list)
    unique_set = set(filtered_list)
    open(output_filename,"w").write("\n".join(unique_set))

if __name__ == '__main__':
    make_word_list(sys.argv[1], sys.argv[2])