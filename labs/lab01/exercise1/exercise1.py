# Lab 01 Exercise 1: Road Trip Budgeter
def is_budget_sufficient(one_way_km,budget):
    possible_trip = budget / 2 * 10
    whole_trip = one_way_km * 2
    if possible_trip >= whole_trip:
        return True
    else:
        return False

budget1 = is_budget_sufficient(100,40)
budget2 = is_budget_sufficient(100,39)

print(budget1)
print(budget2)
