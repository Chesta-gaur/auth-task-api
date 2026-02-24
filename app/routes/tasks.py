from fastapi import Query, APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import SessionLocal
from ..models import Task, User
from ..schemas import TaskCreate, TaskResponse, TaskUpdate
from ..core.security import get_current_user
from typing import Optional

router = APIRouter(prefix="/tasks", tags=["Tasks"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# create tasks
@router.post("", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_task = Task(
        title=task.title,
        owner_id=current_user.id
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

# get all tasks together
@router.get("", response_model=list[TaskResponse])
def get_my_tasks(
    completed : Optional[bool] = Query(None),
    limit : int = Query(10, ge=1, le=100),
    offset : int = Query(0,ge=0),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = db.query(Task).filter(
        Task.owner_id == current_user.id
        )
    
    if completed is not None:
        query = query.filter(Task.completed == completed)
        
    tasks = query.offset(offset).limit(limit).all()
    return tasks

# get single task
@router.get("/{task_id}", response_model=TaskResponse)
def get_single_task(
    task_id : int,
    db : Session = Depends(get_db),
    current_user : User = Depends(get_current_user)
):
    task = db.query(Task).filter(Task.id == task_id, Task.owner_id == current_user.id).first()

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    return task

# update tasks
@router.patch("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id : int,
    updates : TaskUpdate,
    db : Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    task = db.query(Task).filter(
        Task.id == task_id,
        Task.owner_id == current_user.id
    ).first()

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    if updates.title is not None:
        task.title = updates.title

    if updates.completed is not None:
        task.completed = updates.completed

    db.commit()
    db.refresh(task)

    return task

# delete task
@router.delete("/{task_id}", status_code=204)
def delete_task(
    task_id : int,
    db : Session = Depends(get_db),
    current_user : User = Depends(get_current_user)
):
    task = db.query(Task).filter(
        Task.id == task_id,
        Task.owner_id == current_user.id
    ).first()

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    
    db.delete(task)
    db.commit()

    return