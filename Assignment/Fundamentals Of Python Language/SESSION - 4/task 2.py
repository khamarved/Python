"""Build a Python script that asks the user for their marks (0-100) and prints their grade based on this rule: 90+ = 'A', 75-89 = 'B', 60-74 = 'C', 40-59 = 'D', below 40 = 'F'. Use if, elif, and else."""
marks = float(input("Enter your marks (0-100): "))
if marks >= 90:
    print("Your grade is 'A'.")
elif marks >= 75:
    print("Your grade is 'B'.")
elif marks >= 60:
    print("Your grade is 'C'.")
elif marks >= 40:
    print("Your grade is 'D'.")
else:
    print("Your grade is 'F'.")