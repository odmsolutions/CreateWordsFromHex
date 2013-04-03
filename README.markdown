'''
Convert Words From Hex
======================

AKA "operation burst kettle fork"

What is it?
-----------

This is a utility, and Python Library that will take a string of hex digits, and convert them to a list of words.

The hex digits need to be pairs - that is a string that is divisible by two. 

Live version for password generation
------------------------------------
http://dannystaple.github.com/CreateWordsFromHex - This is a JS page that generates a password string in a local JS 
page of four or more words. Read http://xkcd.com/936/ for why this is a good password system.

How does it do it?
------------------

The words are generated from the dictionary, with offset positions from the last offset so more of the dictionary can be used, and there are no wasted bits in the hex string.

In theory, with a dictionary larger than 256 words, I do not think that different hex strings can result in the same set of words, so this should make a unique, lossless and reversible name.

Why?
----

The initial example was the source control system git, which uses SHA1 codes for identifying revisions. Another case could be MAC addresses and IPV6 addresses. All of these produce streams of hex digits.

No person can remember a stream of hex digits, but a few words can be quite memorable.

Example Usage As A Library
--------------------------

	>>> from CreateWordsFromHex import Converter

	>>> converter = Converter()
	>>> converter.set_dictionary_from_file("wordlist.txt")
	>>> converter.convert("fafbe34")
	['receipt', 'present', 'journey', 'building']
	
Example usage as an App
-----------------------

	python CreateWordsFromHex.py <some string>

You will get four unique (currently non-reversible) words for that string code. This can also be used for password generation. Note that subsequent runs will generate different numbers.

http://xkcd.com/936/

To Do
-----

* Increase the number of digits per word
	Currently one word is created for every pair of digits.
	In the case of an IPV6 address, this will be 16 words - which is still too long. I could group by 3 or 4 digits, however, 
these cover significantly larger spaces than the dictionary size, and it would be harder to avoid collisions.

* Add --salt option so salting is not mandatory.
* Add --length option to override length
* Tests probably need a refactor

Notes for testing
-----------------

CreateWordsFromHex uses the Freshen tool 

		pip install freshen

To run them:

		nosetests --with-freshen

To validate the python lib example

		python -m doctest -v README.markdown

License
-------
<a rel="license" href="http://creativecommons.org/licenses/by/3.0/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by/3.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Dataset" property="dct:title" rel="dct:type">ConvertWordsFromHex</span> by <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Danny Staple</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/3.0/">Creative Commons Attribution 3.0 Unported License</a>.
This program is free software. It comes without any warranty, to the extent permitted by applicable law.
'''
