"""Try to change the first element of your fav_apps tuple to 'YouTube' and 
observe the error message. Write a comment explaining why this happens based on tuple immutability."""

my_fav_apps = ('Instagram', 'Zomato', 'Spotify', 'WhatsApp', 'Flipkart')
my_fav_apps[0]='youtube'

#Error occur because tuples are immutable
#once a tuple is created , its element cannot be changed. 