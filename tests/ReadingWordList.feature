Feature: Read a wordlist from a file
	Scenario: passing the testwordlist
		Given a dictionary file testwordlist.txt
		When I get the dictionary
		Then the result should start with list of "chain", "yellow", "month", "manager"