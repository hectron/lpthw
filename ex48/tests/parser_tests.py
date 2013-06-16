from nose.tools import *
from ex48 import lexicon, parser

def test_seek():
    peak = parser.peek(('test_peak', 'is the second key'))
    assert_equal(peak, 't')

def test_match():
    match = parser.match(['test', 'hunt', 'kill'], 'hunt')
    assert_equal(match, 'h')