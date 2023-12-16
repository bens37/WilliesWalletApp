''' Adds money to the current budget '''
def add_to_budget(moneyToAdd, currentBudget):
    newBudget = currentBudget + moneyToAdd
    return newBudget
    
currentBudget = 15
newMoney = 8
newBudget = add_to_budget(newMoney, currentBudget)
print(f"You added ${newMoney} to your previous budget of ${currentBudget}. Your new budget is: ${newBudget}")