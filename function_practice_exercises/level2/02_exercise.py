# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
# paper_doll('Hello') --> 'HHHeeellllllooo'
# paper_doll('Mississippi') --> 'MMMiiissssssiiissssssiiippppppiii'

def paper_doll(text):
    word = ""
    for t in text:
        word += t * 3
    return word

testCheck = True
check01 = paper_doll('Hello')
if check01 != 'HHHeeellllllooo':
    print("check01 failed should return 'HHHeeellllllooo', but got ", check01)
    testCheck = False

check02 = paper_doll('Mississippi')
if check02 != 'MMMiiissssssiiissssssiiippppppiii':
    print("check02 failed should return 'MMMiiissssssiiippppppiii', but got ", check02)
    testCheck = False

if testCheck:
    print("All tests are success!")