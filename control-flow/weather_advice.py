# weather_advice.py

# prompt user for the current weather
weather = input("What's the weather like today? (sunnu/rainy/cold): ").lower()

# provide clothing recommendation based on input
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forgrt your umbreall and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else: 
    print("Sorry, I don't have recommendation for this weather.")