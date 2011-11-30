Feature: Converter Library API
	#Since i need to be able to use arbitrarily long dictionaries
	#And the code should be lossless and reversible - ie no bits lost
	#Then simple lookup is not enough
	#This needs to be an offset lookup that loops back around
	
	#Need to work out later how to further avoid collisions
	
	Scenario: Convert With A small Dictionary
	  Given a dictionary list of "The","Quick","Brown","Fox","Jumps","Over","Lazy","Red","Dog","Bed","Monkey","Car"
		And I pass 0305 as the digits
		When I convert digits
		Then the result should be a list of "Fox","Dog"
		
	Scenario: Convert With A large dictionary 
		Given a dictionary file testwordlist.txt
		And I pass 100e2a as the digits
		When I convert digits
		Then the result should be a list of "smile", "feeble", "degree"
		
	Scenario: Convert With high values
		Given a dictionary file testwordlist.txt
		And I pass ffafbe34 as the digits
		When I convert digits
		Then the result should be a list of "operation", "burst", "kettle", "fork"
		
	Scenario: Convert a long set
		Given a dictionary file testwordlist.txt
		And I pass d49a20bd425c as the digits
		When I convert digits
		Then there should be no errors
		
	Scenario: Handle Colons between digit pairs
		Given a dictionary file testwordlist.txt
		And I pass d4:9a:20:bd:42:5c as the digits
		When I convert digits
		Then there should be no errors
		
	Scenario: Reduce long list to shorter hash
		Given I pass d4:9a:20:bd:42:5c as the digits
		And I set desired length to 8 digits
		When I get the shortened hash
		Then the result length should be 8 digits.
		
	Scenario: Very different digits lists should have different hashes
		Given two sets of very different digits 
		And I set desired length to 8 digits
		When I get both shortened hashes
		Then the two results should be different
	
	Scenario: Reduce a string to a salted hashed set of digits
		Given I pass ff:00:ff:00:ff:00 as the salt
		And I pass "orionrobots.com" as the string
		And I set desired length to 8 digits
		When I get the short string hash
		Then the result length should be 8 digits.
	
	Scenario: Reduce a string + salt to 4 words
		Given I pass ff:00:ff:00:ff:00 as the salt
		And a dictionary file testwordlist.txt
		And I pass "orionrobots.com" as the string
		And I set desired length to 4 words
		When I get the text hashed to words
		Then the result should be a list of "sort", "stitch", "medical", "pocket"
		
	Scenario: A reduced string with different end character shouldn't have the same result
		Given I pass ff:00:ff:00:ff:00 as the salt
		And a dictionary file testwordlist.txt
		And I pass "orionrobots.co." as the string
		And I set desired length to 4 words
		When I get the text hashed to words
		Then the result should not be a list of "sort", "stitch", "medical", "pocket"
