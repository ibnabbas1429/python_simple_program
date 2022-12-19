# This is a simple program to find the occurence of a string in a list
cars= ["audi","bmw","audi","ferrari","porsh","mercedez","audi"]
car_count ={}
for car in cars:
    if car not in car_count:
        car_count.update({car:1})
    else:
        car_count.update({car:car_count[car]+1})

print(car_count)