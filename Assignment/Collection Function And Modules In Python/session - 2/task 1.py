"""Create a Python list called playlist containing five of your favorite song names, 
then use a for loop to print each song with its position in the playlist (starting from 1)."""

playlist=["apna bana le", "aaj ki raat", "Kesariya","love you zindagi ", "o mahi ve" ]
for i in range(len(playlist)):
    print(i+1,playlist[i])
    