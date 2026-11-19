#Write a function display_friends() that takes a dictionary of Instagram usernames as keys
#and their follower counts as values, and prints each username with their followers in the format:
#'username: 2.3K followers'.

def display_friends(friends_dict):
    for username, followers in friends_dict.items():
        if followers >= 1000:
            print(f"{username}: {followers/1000:.1f}k followers")
        else:
            print(f"{username}:{followers} followers")

friends = {
    "kashish": 2300,
    "ved": 1500,
    "om": 850
}
display_friends(friends)