India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]
USA = ["New York", "Chicago", "Las Vegas", "San Francisco"]
UK = ["London", "Manchester", "Liverpool", "Nottingham"]

guess = input("Enter a city name: ")

if guess in India:
    print(f"{guess} is an Indian city")
elif guess in USA:
    print(f"{guess} is a US city")
elif guess in UK:
    print(f"{guess} is a UK city")
else:
    print("This city in not known")


city1 = input("Enter city: ")
city2 = input("Enter another city: ")

if city1 in India and city2 in India:
    print("Both city belongs to India.")

elif city1 in USA and city2 in USA:
    print("Both city belongs to USA.")

elif city1 in UK and city2 in UK:
    print("Both city belongs to UK.")

else:
    print("Both city belongs to different countries")
