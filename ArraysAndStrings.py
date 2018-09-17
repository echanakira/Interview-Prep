import time
start_time = time.time()

# Problem #1-Implementation 1

def isUnique(string):
    s = sorted(string)
    i = 0
    j  = i+1
    while j < len(string):
        if s[i] == s[j]:
            return False
        else:
            i+=1
            j+=1
    return True

# Problem #1-Implementation 2 ***BEST***
def isUnique(string):
    dict = {}
    for s in string:
        if(dict.get(s) == None ):
            dict[s]=1
        else:
            return False
    return True

#Problem #2- Implementation 1
def check_permutation(s1, s2):
    if len(s1) == len(s2):
        sorted_s1 = sorted(s1)
        sorted_s2 = sorted(s2)
    return sorted_s1.equals(sorted_s2)

#Problem #2- Implementation 2 ***Best***
def check_permutation(s1, s2):
    arr = [0] * 128
    for s in s1:
        arr[ord(s)]+=1
    for s in s2:
        if(arr[ord(s)] == 0):
            return False
        else:
            arr[ord(s)]-=1
    return True

def urlify(string):
    string = string.strip()
    new_str = ""
    last_was_space = False
    for s in string:
        if s != ' ':
            new_str += s
            last_was_space = False
        else: #If it is a space
            if (not last_was_space):
                last_was_space = True
                new_str += '%20'
            else:
                last_was_space = True
    return new_str

print(urlify("   H E L L     O  "))

print("--- %s seconds ---" % (time.time() - start_time))
