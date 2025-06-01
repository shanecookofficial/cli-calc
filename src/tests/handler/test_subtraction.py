from src.utils.handler import Handler
"""
SUBTRACTION
5-5 = 0          | Basic subtraction
-5-5 = -10       | Subtraction with a negative
-5-3.3 = -8.3    | Subtraction with a decimal
-5.7-3.3 = -9    | Subtraction with both decimals with integer output
-5.3-8.3 = -13.6 | Subtraction with both decimals with float output

SUBTRACTION - PREV RESULT
10-5 = 5-2 = 3                         | Positive int prev result - positive int output
10-5 = 5-6 = -1                        | Positive int prev result - negative int output
10-5 = 5-5 = 0                         | Positive int prev result - output of 0
10-5 = 5-3.9 = 1.1                     | Positive int prev result - positive float output
10-5 = 5-6.1 = -1.1                    | Positive int prev result - negative float output
10.1-5 = 5.1-4.1 = 1                   | Positive float prev result - positive int output
10.1-5 = 5.1-6.1 = -1                  | Positive float prev result - negative int output
10.1-5 = 5.1-5.1 = 0                   | Positive float prev result - output of 0
10.1-5 = 5.1-2.3 = 2.8                 | Positive float prev result - positive float output
10.1-5 = 5.1-8.3 = -3.2                | Positive float prev result - negative float output
-5-5 = -10--11 = 1                     | Negative int prev result - positive int output
-5-5 = -10-5 = -15                     | Negative int prev result - negative int output
-5-5 = -10--10 = 0                     | Negative int prev result - output of 0
-5-5 = -10--11.1 = 1.1                 | Negative int prev result - positive float output
-5-5 = -10-2.3 = -12.3                 | Negative int prev result - negative float output
-5.1-5 = -10.1--11.1 = 1               | Negative float prev result - positive int output
-5.1-5 = -10.1-1.9 = -12               | Negative float prev result - negative int output
-5.1-5 = -10.1--10.1 = 0               | Negative float prev result - output of 0
-5.1-5 = -10.1--11.2 = 1.1             | Negative float prev result - positive float output
-5.1-5 = -10.1-1.1 = -11.2             | Negative float prev result - negative float output
"""
# Basic subtraction
def test_basic_sub():
    handler = Handler()
    assert handler.solve("5-5") == "0"

# Subtraction with a negative
def test_sub_neg():
    handler = Handler()
    assert handler.solve("-5-5") == "-10"

# Subtraction with a decimal
def test_sub_dec():
    handler = Handler()
    assert handler.solve("-5-3.3") == "-8.3"

# Subtraction with both decimals with integer output
def test_sub_both_dec_int():
    handler = Handler()
    assert handler.solve("-5.7-3.3") == "-9"

# Subtraction with both decimals with float output
def test_sub_both_dec_float():
    handler = Handler()
    assert handler.solve("-5.3-8.3") == "-13.6"

# Subtraction with positive int previous result with positive int output
def test_sub_prev_pos_int_res_pos_int_output():
    handler = Handler()
    handler.solve("10-5")
    equation = "-2"
    assert handler.solve(equation) == "3"

# Subtraction with positive int previous result with negative int output
def test_sub_prev_pos_int_res_neg_int_output():
    handler = Handler()
    handler.solve("10-5")
    equation = "-6"
    assert handler.solve(equation) == "-1"

# Subtraction with positive int previous result with output of zero
def test_sub_prev_pos_int_res_zero_output():
    handler = Handler()
    handler.solve("10-5")
    equation = "-5"
    assert handler.solve(equation) == "0"

# Subtraction with positive int previous result with positive float output
def test_sub_prev_pos_int_res_pos_float_output():
    handler = Handler()
    handler.solve("10-5")
    equation = "-3.9"
    assert handler.solve(equation) == "1.1"

# Subtraction with positive int previous result with negative float output
def test_sub_prev_pos_int_res_neg_float_output():
    handler = Handler()
    handler.solve("10-5")
    equation = "-6.1"
    assert handler.solve(equation) == "-1.1"

# Subtraction with positive float previous result with positive int output
def test_sub_prev_pos_float_res_pos_int_output():
    handler = Handler()
    handler.solve("10.1-5")
    equation = "-4.1"
    assert handler.solve(equation) == "1"

# Subtraction with positive float previous result with negative int output
def test_sub_prev_pos_float_res_neg_int_output():
    handler = Handler()
    handler.solve("10.1-5")
    equation = "-6.1"
    assert handler.solve(equation) == "-1"

# Subtraction with positive float previous result with output of zero
def test_sub_prev_pos_float_res_zero_output():
    handler = Handler()
    handler.solve("10.1-5")
    equation = "-5.1"
    assert handler.solve(equation) == "0"

# Subtraction with positive float previous result with positive float output
def test_sub_prev_pos_float_res_pos_float_output():
    handler = Handler()
    handler.solve("10.1-5")
    equation = "-2.3"
    assert handler.solve(equation) == "2.8"

# Subtraction with positive float previous result with negative float output
def test_sub_prev_pos_float_res_neg_float_output():
    handler = Handler()
    handler.solve("10.1-5")
    equation = "-8.3"
    assert handler.solve(equation) == "-3.2"

# Subtraction with negative int previous result with positive int output
def test_sub_prev_neg_int_res_pos_int_output():
    handler = Handler()
    handler.solve("-5-5")
    equation = "--11"
    assert handler.solve(equation) == "1"

# Subtraction with negative int previous result with negative int output
def test_sub_prev_neg_int_res_neg_int_output():
    handler = Handler()
    handler.solve("-5-5")
    equation = "-5"
    assert handler.solve(equation) == "-15"

# Subtraction with negative int previous result with output of zero
def test_sub_prev_neg_int_res_zero_output():
    handler = Handler()
    handler.solve("-5-5")
    equation = "--10"
    assert handler.solve(equation) == "0"

# Subtraction with negative int previous result with positive float output
def test_sub_prev_neg_int_res_pos_float_output():
    handler = Handler()
    handler.solve("-5-5")
    equation = "--11.1"
    assert handler.solve(equation) == "1.1"

# Subtraction with negative int previous result with negative float output
def test_sub_prev_neg_int_res_neg_float_output():
    handler = Handler()
    handler.solve("-5-5")
    equation = "-2.3"
    assert handler.solve(equation) == "-12.3"

# Subtraction with negative float previous result with positive int output
def test_sub_prev_neg_float_res_pos_int_output():
    handler = Handler()
    handler.solve("-5.1-5")
    equation = "--11.1"
    assert handler.solve(equation) == "1"

# Subtraction with negative float previous result with negative int output
def test_sub_prev_neg_float_res_neg_int_output():
    handler = Handler()
    handler.solve("-5.1-5")
    equation = "-1.9"
    assert handler.solve(equation) == "-12"

# Subtraction with negative float previous result with output of zero
def test_sub_prev_neg_float_res_zero_output():
    handler = Handler()
    handler.solve("-5.1-5")
    equation = "--10.1"
    assert handler.solve(equation) == "0"

# Subtraction with negative float previous result with positive float output
def test_sub_prev_neg_float_res_pos_float_output():
    handler = Handler()
    handler.solve("-5.1-5")
    equation = "--11.2"
    assert handler.solve(equation) == "1.1"

# Subtraction with negative float previous result with negative float output
def test_sub_prev_neg_float_res_neg_float_output():
    handler = Handler()
    handler.solve("-5.1-5")
    equation = "-1.1"
    assert handler.solve(equation) == "-11.2"