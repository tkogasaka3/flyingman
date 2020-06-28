

hobbies = {"ski":"Fischer", "golf":"Ping", "Climbing":"La Sportiva"}

n = input("please input your fav hobby:")

if n in hobbies:
    hobby = hobbies[n]
    print(hobby)
else:
    print("not founded")
    

