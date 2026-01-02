# MASTER YODA: Given a sentence, return a sentence with the words reversed
# master_yoda('I am home') --> 'home am I'
# master_yoda('We are ready') --> 'ready are We'
# Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:

# >>> "--".join(['a','b','c'])
# >>> 'a--b--c'
# This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:

# >>> " ".join(['Hello','world'])
# >>> "Hello world"

def master_yoda(text):
    words = text.split(" ")
    return " ".join(words[::-1])
    pass

def main():
    check01 = master_yoda('I am home')
    if check01 != 'home am I':
        print("check01 failed should return 'home am I', but got ", check01)
        return
    
    check02 = master_yoda('We are ready')
    if check02 != 'ready are We':
        print("check02 failed should retrun 'ready are We', but got ", check02)
        return
    
    print("All tests are success!")

main()