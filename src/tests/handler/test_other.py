from src.utils.handler import Handler
"""
OTHER
| Other Scenario 1
| Other Scenario 2
| Other Scenario 3
| Other Scenario 4
| Other Scenario 5
"""
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