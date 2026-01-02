# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# almost_there(90) --> True
# almost_there(104) --> True
# almost_there(150) --> False
# almost_there(209) --> True
# NOTE: abs(num) returns the absolute value of a number

def almost_there(n):
    if abs(n - 100) < 10 or abs(n - 200) < 10:
        return True
    else :
        return False


testCheck = True
check01 = almost_there(104)
if check01 != True:
    print("check01 failed should return True, but got ", check01)
    testCheck = False

check02 = almost_there(150)
if check02 != False:
    print("check02 failed should return False, but got ", check02)
    testCheck = False

check03 = almost_there(209)
if check03 != True:
    print("check03 failed should return True, but got ", check03)
    testCheck = False

if testCheck:
    print("All tests are success!")