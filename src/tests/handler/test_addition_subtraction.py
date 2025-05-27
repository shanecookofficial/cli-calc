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

SUBTRACTION
5-5 = 0          | Basic subtraction
-5-5 = -10       | Subtraction with a negative
-5-3.3 = -8.3    | Subtraction with a decimal
-5.7-3.3 = -9    | Subtraction with both decimals with integer output
-5.3-8.3 = -13.6 | Subtraction with both decimals with float output

OTHER
-5-6-7-8-9-10.543+2.1 = -43.443 | Other Scenario 1
| Other Scenario 2
| Other Scenario 3
| Other Scenario 4
| Other Scenario 5
"""
### ADDITION###

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

### SUBTRACTION ###

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

### OTHER ###

# Other Scenario 1
def test_other_1():
    handler = Handler()
    assert handler.solve("-5-6-7-8-9-10.543+2.1") == "-43.443"

# Other Scenario 2
def test_other_2():
    handler = Handler()
    assert handler.solve("10-3+2.5-1.5+4.3") == "12.3"

# Other Scenario 3
def test_other_3():
    handler = Handler()
    assert handler.solve("-10.5+3.7-5.2-1.5") == "-13.5"

# Other Scenario 4
def test_other_4():
    handler = Handler()
    assert handler.solve("10-5+2-7+3-1") == "2"

# Other Scenario 5
def test_other_5():
    handler = Handler()
    assert handler.solve("1.5+2.7-0.3-1.2+4.8") == "7.5"

# Other Scenario 6
def test_other_6():
    handler = Handler()
    assert handler.solve("1.5+2.7-.3-1.2+4.8") == "7.5"

# Other Scenario 7
def test_other_7():
    handler = Handler()
    assert handler.solve("1.5+2.7+.3-1.2+4.8") == "8.1"

# Other Scenario 8
def test_other_8():
    handler = Handler()
    assert handler.solve("123456.789123+987654.321987-111111.111111") == "999999.999999"