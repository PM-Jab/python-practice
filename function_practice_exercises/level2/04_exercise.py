# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14

def summer_69(arr):
    sum = 0
    lock = False
    for i in arr:
        if i == 6:
            lock = True
        elif i == 9:
            lock = False
            continue
        
        if not lock:
            sum+= i

    return sum


testCheck = True
check01 = summer_69([1,3,5])
if check01 != 9:
    print("check01 failed should return 9, but got ", check01)
    testCheck = False

check02 = summer_69([4, 5, 6, 7, 8, 9])
if check02 != 9:
    print("check02 failed should return 9, but got ", check02)
    testCheck = False

check03 = summer_69([2, 1, 6, 9, 11])
if check03 != 14:
    print("check03 failed should return 14, but got ", check03)
    testCheck = False

if testCheck:
    print("All tests are success!")