
temperature = int(input("Enter the current temperature in Celsius: "))
if temperature >= 30 :
    print("It's a hot day. Stay hydrated!")
elif 20 <= temperature <= 29:# and temperature <= 29 :
    print("It's a warm day. Enjoy the weather!")
elif temperature >= 10 and temperature <= 19 :
    print("It's a cool day. Wear a jacket!")
else :
    print("It's a cold day. Stay warm!")