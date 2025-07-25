def split_string(string):
    string_length = len(string)
    splited_string = string.split()
    return splited_string 

def string_char(string):
    char = list(string)
    return f"Characters in the string are: {char} and it has {len(char)} characters"

def string_char_loop(string):
    char=[]
    for char in string:
        print(char, end='')

string = "Ade Ada is a girl"

#print(split_string(string))
#print(string_char(string))


def string_char_loop1(string):
    char_list=[]
    for char in string:
        # Using list to store characters
        # This is not necessary but shows how to use a list
        char_list.append(char)
        # Using a simple print to display characters       
        # This is more efficient than using a list if you just want to print
        #char.append(char)
        print(char, end='')

string_char_loop1(string)


#using lambda to split string
def split_string_lambda(string):
    return list(map(lambda x: x, string.split()))

print(split_string_lambda(string))