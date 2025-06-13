from typing import List

from models import Task


async def completed_tasks(tasks_db : List[Task]):
    done = 0
    in_progress = 0
    for task in tasks_db:
        if task.completed == True:
            done = done + 1
        else:
            in_progress = in_progress + 1
    return {"message" : f"Tâches terminées : {done} / Tâches en cours : {in_progress}"}

async def get_next_id(tasks_db : List[Task]):
    if not tasks_db:
        return 0
    return max(task.id for task in tasks_db) + 1

async def get_percentage_tasks(tasks_db : List[Task]):
    done = 0
    for task in tasks_db:
        if task.completed == True:
            done+=1
    return {"message" : f"{(done/len(tasks_db))*100}% des tâches terminées"}
