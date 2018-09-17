'''
    A child is running up a staircase with n steps and can hop either 1 step, 2 steps,
    or 3 steps at a time. Implement a method to count how many possible ways the
    child can run up the stairs.
'''
def triple_step(steps):
    return triple_helper(steps, {})

#Base Case: 0 -> 0
def triple_helper(steps, memo):
    if(steps == 0):
        return 1
    elif(steps in memo):
        return memo[steps]
    elif(steps < 0 ):
        return 0
    else:
        memo[steps] = triple_helper(steps - 1, memo) + triple_helper(steps - 2, memo) + triple_helper(steps - 3, memo)
        return memo[steps]
