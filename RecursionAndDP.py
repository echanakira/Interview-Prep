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

'''
Find the index in an Arr[0...n-1] where Arr[i]=i
'''
def magic_index(arr, left, right):
    left = 0
    right  = len(arr)-1
    mid = int((left + right)/2)
    while(left < right):
        if(arr[mid] > mid): #Search left
            right = mid
            mid = int((left + right)/2)
        elif(arr[mid] < mid):
            left = mid+1
            mid = int((left + right)/2)
        else:
            return mid
    return -1

print(magic_index([-5,-3,1,4,6], 0, 5))


'''
    Implement multiply without multiplyinh
'''
def recursive_multiply(num1, num2):
    if(num1 == 0):
        return 0
    elif(num2 == 0):
        return 0
    return num1 + recursive_multiply(num1, num2-1)
