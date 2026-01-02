# FIND 33:
# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False

def has_33(nums):
    return "".join(map(str, nums)).find("33") >= 0
    

testCheck = True
check01 = has_33([1,3,3])
if check01 != True:
    print("check01 failed should return True, but got ", check01)
    testCheck = False

check02 = has_33([1,3,1,3])
if check02 != False:
    print("check02 failed should return False, but got ", check02)
    testCheck = False

check03 = has_33([3,1,3])
if check03 != False:
    print("check03 failed should return False, but got ", check03)
    testCheck = False

if testCheck :
    print("All tests are success!")