to_do_list = []  # Initialize an empty list to store tasks

while True:  # Infinite loop until 'done' is entered
    task = input("Enter a task (or 'done' to stop): ")  # Get user input
    
    if task.lower() == 'done':  # If user types 'done', break the loop
        break
    else:
        to_do_list.append(task)  # Add the task to the list

# Display the stored tasks
print("Your tasks are:")
for task in to_do_list:  # Loop runs len(to_do_list) times -> O(n)
    print(task)

# TC: O(n) -> Loop runs for each task entered
# SC: O(n) -> Storing all tasks in a list
