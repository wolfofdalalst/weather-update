# Run this in command line to check whether your setup is right or not
# the code below is temporary

from open_weather.current import CurrentCity

kolkata = CurrentCity("Kolkata", test=True)

print(str(kolkata))