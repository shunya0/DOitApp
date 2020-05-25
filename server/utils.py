
def findIndexById(id, tasks):
    for index, task in enumerate(tasks):
        if task.get('id') == id:
            return index
    return -1
