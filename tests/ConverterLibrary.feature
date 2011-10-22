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
		