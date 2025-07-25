#Find the greatest number



def greatest_number(number_list):
    greatest_number = number_list[0]
    for number in number_list:
        if number > greatest_number:
            greatest_number = number
    
    return (f"greatest_number is {greatest_number}")




def greatest_nextnumber(number_list):
    greatest_number = number_list[0]
    next_greatest_number = float("inf")
    for number in number_list:
        if number >= greatest_number:
            greatest_number,next_greatest_number = number, next_greatest_number
     
    
    return f"greatest_number is {greatest_number} and next_greatest_number  is {next_greatest_number}"

number_list = [111,20,53,24,15,67,9,23,11,84,56]

print(greatest_nextnumber(number_list))
