from src.utils.handler import Handler
"""
ADDITION
5+5 = 10         | Addition with both positives
5+-5 = 0         | Addition with a positive & negative
-5+5 = 0         | Addition with a negative & positive
-5+-5 = -10      | Addition with both negatives
5+5.1 = 10.1     | Addition with one decimal
5.3+8.7 = 14     | Addition with both decimals with integer output
5.2+8.7 = 13.9   | Addition with both decimals with float output

ADDITION - PREV RESULT
5+5 = 10+5 = 15              | Positive int prev result - positive int output
5+5 = 10+-15 = -5            | Positive int prev result - negative int output
5+5 = 10+-10 = 0             | Positive int prev result - output of 0
5+5 = 10+5.1 = 15.1          | Positive int prev result - positive float output
5+5 = 10+-14.9 = -4.9        | Positive int prev result - negative float output
5.1+5 = 10.1+4.9 = 15        | Positive float prev result - positive int output
5.1+5 = 10.1+-11.1 = -1      | Positive float prev result - negative int output
5.1+5 = 10.1+-10.1 = 0       | Positive float prev result - output of 0
5.1+5 = 10.1+1.1 = 11.2      | Positive float prev result - positive float output
5.1+5 = 10.1+-11.2 =-1.1     | Positive float prev result - negative float output
-5+-5 = -10+12 = 2           | Negative int prev result - positive int output
-5+-5 = -10+-2 = -12         | Negative int prev result - negative int output
-5+-5 = -10+10 = 0           | Negative int prev result - output of 0
-5+-5 = -10+12.1 = 2.1       | Negative int prev result - positive float output
-5+-5 = -10+-2.1 = -12.1     | Negative int prev result - negative float output
-5.1+-5 = -10.1+11.1 = 1     | Negative float prev result - positive int output
-5.1+-5 = -10.1+-1.9 = -12   | Negative float prev result - negative int output
-5.1+-5 = -10.1+10.1 = 0     | Negative float prev result - output of 0
-5.1+-5 = -10.1+11.2 = 1.1   | Negative float prev result - positive float output
-5.1+-5 = -10.1+-1.1 = -11.2 | Negative float prev result - negative float output
"""
# Addition with both positives
def test_add_both_pos():
    handler = Handler()
    assert handler.solve("5+5") == "10"

# Addition with a positive & negative
def test_add_pos_neg():
    handler = Handler()
    assert handler.solve("5+-5") == "0"

# Addition with a negative & positive
def test_add_neg_pos():
    handler = Handler()
    assert handler.solve("-5+5") == "0"

# Addition with both negatives
def test_add_both_neg():
    handler = Handler()
    assert handler.solve("-5+-5") == "-10"

# Addition with one decimal
def test_add_dec():
    handler = Handler()
    assert handler.solve("5+5.1") == "10.1"

# Addition with both decimals with integer output
def test_add_both_dec_int():
    handler = Handler()
    assert handler.solve("5.3+8.7") == "14"

# Addition with both decimals with float output
def test_add_both_dec_float():
    handler = Handler()
    assert handler.solve("5.2+8.7") == "13.9"

# Addition with a positive int previous result with positive int output
def test_prev_pos_int_res_pos_int_output():
    handler = Handler()
    prev_equation = "5+5"
    handler.solve(prev_equation)
    equation = "+5"
    assert handler.solve(equation) == "15"

# Addition with a positive int previous result with negative int output
def test_prev_pos_int_res_neg_int_output():
    handler = Handler()
    prev_equation = "5+5"
    handler.solve(prev_equation)
    equation = "+-15"
    assert handler.solve(equation) == "-5"

# Addition with positive int previous result with output of zero
def test_prev_pos_int_res_zero_output():
    handler = Handler()
    prev_equation = "5+5"
    handler.solve(prev_equation)
    equation = "+-10"
    assert handler.solve(equation) == "0"

# Addition with positive int previous result with positive float output
def test_prev_pos_int_res_pos_float_output():
    handler = Handler()
    prev_equation = "5+5"
    handler.solve(prev_equation)
    equation = "+5.1"
    assert handler.solve(equation) == "15.1"

# Addition with positive int previous result with negative float output
def test_prev_pos_int_res_neg_float_output():
    handler = Handler()
    prev_equation = "5+5"
    handler.solve(prev_equation)
    equation = "+-14.9"
    assert handler.solve(equation) == "-4.9"

# Addition with positive float previous result with positive int output
def test_prev_pos_float_res_pos_int_output():
    handler = Handler()
    prev_equation = "5+5.1"
    handler.solve(prev_equation)
    equation = "+4.9"
    assert handler.solve(equation) == "15"

# Addition with positive float previous result with negative int output
def test_prev_pos_float_res_neg_int_output():
    handler = Handler()
    prev_equation = "5+5.1"
    handler.solve(prev_equation)
    equation = "+-11.1"
    assert handler.solve(equation) == "-1"

# Addition with positive float previous result with output of zero
def test_prev_pos_float_res_zero_output():
    handler = Handler()
    prev_equation = "5.1+5"
    handler.solve(prev_equation)
    equation = "+-10.1"
    assert handler.solve(equation) == "0"

# Addition with positive float previous result with positive float output
def test_prev_pos_float_res_pos_float_output():
    handler = Handler()
    prev_equation = "5.1+5"
    handler.solve(prev_equation)
    equation = "+1.1"
    assert handler.solve(equation) == "11.2"

# Addition with positive float previous result with negative float output
def test_prev_pos_float_res_neg_float_output():
    handler = Handler()
    prev_equation = "5.1+5"
    handler.solve(prev_equation)
    equation = "+-11.2"
    assert handler.solve(equation) == "-1.1"

# Addition with negative int previous result with positive int output
def test_prev_neg_int_res_pos_int_output():
    handler = Handler()
    prev_equation = "-5+-5"
    handler.solve(prev_equation)
    equation = "+12"
    assert handler.solve(equation) == "2"

# Addition with negative int previous result with negative int output
def test_prev_neg_int_res_neg_int_output():
    handler = Handler()
    prev_equation = "-5+-5"
    handler.solve(prev_equation)
    equation = "+-2"
    assert handler.solve(equation) == "-12"

# Addition with negative int previous result with output of zero
def test_prev_neg_int_res_zero_output():
    handler = Handler()
    prev_equation = "-5+-5"
    handler.solve(prev_equation)
    equation = "+10"
    assert handler.solve(equation) == "0"

# Addition with negative int previous result with positive float output
def test_prev_neg_int_res_pos_float_output():
    handler = Handler()
    prev_equation = "-5+-5"
    handler.solve(prev_equation)
    equation = "+12.1"
    assert handler.solve(equation) == "2.1"

# Addition with negative int previous result with negative float output
def test_prev_neg_int_res_neg_float_output():
    handler = Handler()
    prev_equation = "-5+-5"
    handler.solve(prev_equation)
    equation = "+-2.1"
    assert handler.solve(equation) == "-12.1"

# Addition with negative float previous result with positive int output
def test_prev_neg_float_res_pos_int_output():
    handler = Handler()
    prev_equation = "-5.1+-5"
    handler.solve(prev_equation)
    equation = "+11.1"
    assert handler.solve(equation) == "1"

# Addition with negative float previous result with negative int output
def test_prev_neg_float_res_neg_int_output():
    handler = Handler()
    prev_equation = "-5.1+-5"
    handler.solve(prev_equation)
    equation = "+-1.9"
    assert handler.solve(equation) == "-12"

# Addition with negative float previous result with output of zero
def test_prev_neg_float_res_zero_output():
    handler = Handler()
    prev_equation = "-5.1+-5"
    handler.solve(prev_equation)
    equation = "+10.1"
    assert handler.solve(equation) == "0"

# Addition with negative float previous result with positive float output
def test_prev_neg_float_res_pos_float_output():
    handler = Handler()
    prev_equation = "-5.1+-5"
    handler.solve(prev_equation)
    equation = "+11.2"
    assert handler.solve(equation) == "1.1"

# Addition with negative float previous result with negative float output
def test_prev_neg_float_res_neg_float_output():
    handler = Handler()
    prev_equation = "-5.1+-5"
    handler.solve(prev_equation)
    equation = "+-1.1"
    assert handler.solve(equation) == "-11.2"