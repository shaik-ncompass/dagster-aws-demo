import dagster as dg

@dg.asset 
def addition():
    a = 10
    b = 5
    return a + b

@dg.asset
def subtraction(addition):
    return addition - 3