"""Given a list of song durations in minutes, use a lambda function with the map() function to convert 
all durations to seconds and print the resulting list."""
duration = [3.5,4.2,2.8,5.1]
duration_in_seconds=list(map(lambda x:x*60,duration))
print(duration_in_seconds)