
from rle import encode
from rle import decode

from hypothesis import given, settings
from hypothesis.strategies import text
from hypothesis.strategies import integers

def test_rle():
    assert encode('kkk') == '3k'

def test_rle2():
    assert encode('kkkkkkoooo') == '6k4o'

def test_empty():
    assert encode('') == "error, empty input"

def test_symbol():
    assert encode('virker ikke') == '1v1i1r1k1e1r1 1i2k1e'
    
def test_number():
    assert encode('3777') == '1337'

def test_decode_empty():
    assert decode('') == ""
    
    
def test_decode():
    assert decode('2k') == 'kk'
    
@given(text()) 
@settings(max_examples=30)
def test_hypo(x):
    print(x)
    decode(encode(x)) == x
    
#@given(integers()) 
@settings(max_examples=30)
def test_hypo(x):
    print(x)
    decode(encode(x)) == x