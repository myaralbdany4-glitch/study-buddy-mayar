
def add_task(tasks, name):
    """Add a valid study task to the list."""
if name.strip() == "" or len(name) > 30:
    print("Invalid task name")
        return tasks
    tasks.append(name)
    return tasks
