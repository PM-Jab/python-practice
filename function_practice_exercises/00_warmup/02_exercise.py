# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# makes_twenty(20,10) --> True
# makes_twenty(12,8) --> True
# makes_twenty(2,3) --> False

def makes_twenty(n1, n2):
    if n1 + n2 == 20 or n1 == 20 or n2 == 20:
        return True
    else :
        return False

def main():
    check01 = makes_twenty(20,10)
    if check01 != True:
        print("check01 failed should return True, but got ", check01)
        return
    
    check02 = makes_twenty(2,3)
    if check02 != False:
        print("check02 failed should return False, but got ", check02)
        return
    
    print("All tests are success!")

main()