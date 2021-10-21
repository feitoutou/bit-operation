# During the client registration for ASIC, there are 8 questions for them to answer
# Suppose we use 8 digit bits for the results of 8 answers
# bit 0 for question 1 answer pass(1) or not(0)
# bit 1 for question 2 answer pass(1) or not(0) ... to bit 7
# This 8 digit bits are stored as decimal in database (0 - 255)
# Given a list of users' answer results, return the error answer times of every question

# Then write a test for this function

from data import data, errors

def findErrorAnswerTimes():
    #implement this
    return []

def test_error_times():
    result = findErrorAnswerTimes()
    assert result == errors