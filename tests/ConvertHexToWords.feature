Feature: Converting Digits To Words
	
	Scenario: Convert With A small Dictionary and 2 Digit Groups
	  Given a dictionary list of "The","Quick","Brown","Fox","Jumps","Over","Lazy","Red","Dog","Bed","Monkey","Car"
		And I pass 030A as the digits
		When I convert digits
		Then the result should be a list of "Fox","Monkey"
		
	Scenario: Convert With A large dictionary and 2 Digit groups
		Given a dictionary file testwordlist.txt
		And I pass 100e2a as the digits
		When I convert digits
		Then the result should be a list of "smile", "rhythm", "round"
		