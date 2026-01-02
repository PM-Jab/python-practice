# WARMUP SECTION:
# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd
# lesser_of_two_evens(2,4) --> 2
# lesser_of_two_evens(2,5) --> 5
def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            return a
        else :
            return b
    else :
        if a < b:
            return b
        else :
            return a

def main():
    check01 = lesser_of_two_evens(2,4)
    if check01 != 2 :
        print("check01 failed should return 2 but got ", check01)
        return
    
    check02 = lesser_of_two_evens(2,5)
    if check02 != 5:
        print("check02 failed should return 5 but got ", check02)
        return
    
    print("All tests are success!")


main()