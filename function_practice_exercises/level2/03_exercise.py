# BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11) --> 19

def blackjack(a,b,c):
    sum = a + b + c
    if 11 in [a,b,c]:
        sum -= 10

    if sum > 21:
        return 'BUST'
    else :
        return sum

testCheck = True
check01 = blackjack(5,6,7)
if check01 != 18:
    print("check01 failed should return 18, but got ", check01)
    testCheck = False

check02 = blackjack(9,9,9)
if check02 != 'BUST':
    print("check02 failed should return 'BUST', but got ", check02)
    testCheck = False

check03 = blackjack(9,9,11)
if check03 != 19:
    print("check03 failed should return 19, but got ", check03)
    testCheck = False

if testCheck:
    print("All tests are success!")