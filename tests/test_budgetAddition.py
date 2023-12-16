import pytest
from budgetAddition import add_to_budget

def test_add_to_budget():
    # Test case 1
    current_budget = 15
    money_to_add = 8
    new_budget = add_to_budget(money_to_add, current_budget)
    assert new_budget == 23

    # Test case 2
    current_budget = 0
    money_to_add = 10
    new_budget = add_to_budget(money_to_add, current_budget)
    assert new_budget == 10

    # Test case 3 (negative money)
    current_budget = 30
    money_to_add = -5
    new_budget = add_to_budget(money_to_add, current_budget)
    assert new_budget == 25
