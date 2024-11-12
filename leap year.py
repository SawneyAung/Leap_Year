# chain logic
def isLeapYear_LogicChain(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return "a leap year"
    else:
        return "not a leap year"
    ...

# nested function
def isLeapYear_NestedIfConditional(year):
    # use nested contional Ifs
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "a leap year"
            else:
                return "not a leap year"
        else:
            return "a leap year"
    else:
        return "not a leap year"
    ...

# Test Cases
print(isLeapYear_LogicChain(2100))  # Expected: not a leap year
print(isLeapYear_NestedIfConditional(2100))  # Expected: not a leap year

print(isLeapYear_LogicChain(2000))  # Expected: a leap year
print(isLeapYear_NestedIfConditional(2000))  # Expected: a leap year

print(isLeapYear_LogicChain(2024))  # Expected: a leap year
print(isLeapYear_NestedIfConditional(2024))  # Expected: a leap year