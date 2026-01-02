# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
 
# old_macdonald('macdonald') --> MacDonald
# Note: 'macdonald'.capitalize() returns 'Macdonald'

def old_macdonald(name):
    first = name[0:3].capitalize()
    last = name[3:].capitalize()
    return first + last

def main():
    check = old_macdonald("macdonald")
    if check != "MacDonald":
        print("check failed should return MacDonald, but got ",check)
        return
    
    print("All test success!")

main()