"""Step definitions for the feature"""
from freshen import *

import CreateWordsFromHex
import os

@Before
def before(sc):
    scc.result = None
    scc.digits = None
    scc.converter = CreateWordsFromHex.Converter()
  
@Transform(r"^list of (.*)$")
def transform_list(list_string):
    return list(eval(list_string))

@Given("I pass (.*) as the digits")
def setDigitParam(digits):
    scc.digits = digits
  
@Given("I pass (.*) as the salt")
def setSaltParam(digits):
    scc.salt = digits
    
@Given("I pass \"(.*)\" as the string")
def setStringParam(string):
    scc.string = string

@Given("a dictionary (list of .*)")
def setDictionary(dictionary):
    scc.converter.set_dictionary_from_list(dictionary)

@Given("I set desired length to (.*) (digits|words)")
def setDesiredLength(length_str, discarded):
    scc.desired_length = int(length_str)

@Given("a dictionary file (\w+\.txt)")
def setDictionaryFilename(filename):
    scc.converter.set_dictionary_from_file(os.path.join("tests", filename))

@Given("two sets of very different digits")
def prepareTwoSetsOfDifferentDigits():
    scc.first_set = "12b88e6912b88e69"
    scc.second_set = "369e1567369e1567"

@When("I convert digits")
def runConvertDigits():
    scc.result = scc.converter.convert(scc.digits)
  
@When("I get the dictionary")
def runReadWordList():
    scc.result = scc.converter.get_dictionary()

@When("I get the shortened hash")
def runGetShortenedHash():
    scc.result = CreateWordsFromHex.get_shortened_hash(scc.digits, scc.desired_length)

@When("I get both shortened hashes")
def runGetBothShortenedHashes():
    scc.result1 = CreateWordsFromHex.get_shortened_hash(scc.first_set, scc.desired_length)
    scc.result2 = CreateWordsFromHex.get_shortened_hash(scc.second_set, scc.desired_length)

@When("I get the short string hash")
def runGetShortStringHash():
    scc.result = CreateWordsFromHex.get_short_salted_string_hash(scc.string, scc.salt, scc.desired_length)

@When("I get the text hashed to words")
def runGetTextHashedToWords():
    scc.result = scc.converter.getHashedWordsFromText(scc.string, scc.salt, scc.desired_length)

@Then("the two results should be different")
def checkResultsAreDifferent():
    assert_not_equal(scc.result1, scc.result2)

@Then("the result should be a (list of .*)")
def checkResultIsListOf(expected_list):
    assert_equal(scc.result, expected_list)
    
@Then("the result should not be a (list of .*)")
def checkResultIsNotListOf(expected_not_list):
    assert_not_equal(scc.result, expected_not_list)
    
@Then("the result should start with (list of .*)")
def check_read_word_list_result(list_start):
    assert_equals(scc.result[:len(list_start)], list_start)

@Then("the result length should be (.*) digits")
def check_result_list_length(list_length_str):
    required_list_len = int(list_length_str)
    assert_equals(len(scc.result), required_list_len)
    print scc.result
    
@Then("there should be no errors")
def check_no_errors():
    pass