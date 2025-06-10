from typing import List
from venv import logger

from fastapi import APIRouter, HTTPException
from DoYourTasks.Enum.priorite import PrioriteEnum
from DoYourTasks.models import Task, TaskCreate, TaskUpdate

router = APIRouter(prefix="/tasks")

tasks_db: List[Task] = []


async def get_next_id():
    if not tasks_db:
        return 0
    return max(task.id for task in tasks_db) + 1

@router.post("/create")
async def create_task(task :TaskCreate):
    task = Task(id=await get_next_id(), **task.model_dump())
    tasks_db.append(task)
    return {"message" : "Tache ajoutée avec succès"}

@router.get("/list")
async def show_tasks():
    return tasks_db

@router.get("/completer")
async def completed_tasks_route():
    return await completed_tasks()


async def completed_tasks():
    done = 0
    in_progress = 0
    for task in tasks_db:
        if task.completed == True:
            done = done + 1
        else:
            in_progress = in_progress + 1
    return {"message" : f"Tâches terminées : {done} / Tâches en cours : {in_progress}"}

@router.get("/recherche")
async def find_by_word(word : str):
    tasks : List[Task] = []
    for task in tasks_db:
        if word in task.description:
            tasks.append(task)
    if len(tasks) > 0:
        return tasks
    return {"message" : "La tâche n'existe pas"}

@router.get("/trier")
async def sort_by_priority():
    priority_order = {
        PrioriteEnum.HAUTE: 0,
        PrioriteEnum.MOYENNE: 1,
        PrioriteEnum.BASSE: 2,
    }
    sorted_tasks = sorted(
        tasks_db,
        key=lambda t: priority_order.get(t.priorite, 3)
    )
    return sorted_tasks

@router.get("/{id}")
async def get_task(id :int):
    for task in tasks_db:
        if task.id == id:
            return task
    raise HTTPException(status_code=404, detail="Tâche non trouvée")


@router.delete("/{id}")
async def delete_task(id :int):
    tasks_db.remove(await get_task(id))
    return {"message" : "Tâche supprimée avec succès"}


@router.patch("/terminer/{id}", name="Marquer comme terminé")
async def update_task(id : int):
    task = await get_task(id)
    task.completed = True
    return {"message" : f"Tâche {await get_task(id).description} terminée"}

@router.patch("/modifier/{id}", name="Modifier une tâche")
async def update_task(id : int, task : TaskUpdate):
    task_update = await get_task(id)
    updates = task.model_dump(exclude_unset=True)
    for field, value in updates.items():
        setattr(task_update, field, value)
    return {"message" : f"Tâche {await get_task(id).description} modifiée"}

