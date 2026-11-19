"""Write a function called format_follower_count that takes a number and returns it 
in Instagram-style format (e.g., 1500 as '1.5K', 1200000 as '1.2M').
<br><br><em><strong>Hint:</strong>
Use if-elif-else to check the number range and format accordingly.</em>"""

def format_follower_count(n):
    if(n<0):
      print("Invalid")

    elif(n>=1000):
        print("Followers",n,"k")
    elif(n>=1000000):
        print("Followers",n,"k")

n=int(input("Enter instagram follower"))
format_follower_count(n)