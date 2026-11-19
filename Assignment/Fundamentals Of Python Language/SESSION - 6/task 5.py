"""Create a program that uses a while loop to print a pyramid star pattern with 4 rows, so the output looks like BookMyShow's seat rows:
*
***
*****
*******<br><br><em><strong>Hint:</strong> Use two nested while loops: one for spaces, one for stars.</em>"""

for i in range(1,9):
    if i%2!=0:
     print("*"*i)



   