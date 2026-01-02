# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
# animal_crackers('Levelheaded Llama') --> True
# animal_crackers('Crazy Kangaroo') --> False

def animal_crackers(text):
    words = text.split(" ")
    if words[0][0] == words[1][0]:
        return True
    else :
        return False

def main():
    check01 = animal_crackers("Levelheaded Llama")
    if check01 != True:
        print("check01 failed should return True but got ",check01)
        return
    
    check02 = animal_crackers("Crazy Kangaroo")
    if check02 == True:
        print("check02 failed should return False but got ",check02)
        return

    print("All tests are success!")

main()