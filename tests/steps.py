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

@Given("I pass (\w+) as the digits")
def setDigitParam(digits):
    scc.digits = digits
  
@Given("a dictionary (list of .*)")
def setDictionary(dictionary):
    scc.converter.set_dictionary_from_list(dictionary)

@Given("a dictionary file (\w+\.txt)")
def setDictionaryFilename(filename):
    scc.converter.set_dictionary_from_file(os.path.join("tests", filename))

@When("I convert digits")
def runConvertDigits():
    scc.result = scc.converter.convert(scc.digits)
  
@When("I get the dictionary")
def runReadWordList():
    scc.result = scc.converter.get_dictionary()

@Then("the result should be a (list of .*)")
def check_result(expected_list):
    assert_equal(scc.result, expected_list)

    
@Then("the result should start with (list of .*)")
def check_read_word_list_result(list_start):
    assert_equals(scc.result[:len(list_start)], list_start)
    
@Then("there should be no errors")
def check_no_errors():
    pass