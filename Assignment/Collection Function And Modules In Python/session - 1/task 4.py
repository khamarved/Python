
"""Create a new list called weekend_plan with at least 5 items representing things you want to 
do this weekend (mix of strings and numbers). Remove the last item using the pop() method and 
display the removed item and the updated list."""

weekend_plan = ["Shopping", "Watching movies", 2, "Listening to music", 500]

removed_item = weekend_plan.pop()

print("Removed item:", removed_item)
print("Updated list:", weekend_plan)