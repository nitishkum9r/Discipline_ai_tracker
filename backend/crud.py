from sqlalchemy.orm import Session
from models import Task, TaskLog
from datetime import date
from sqlalchemy import func

def create_task(db: Session, title: str):
    task = Task(title=title)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_tasks(db: Session):
    return db.query(Task).all()

def get_task_logs(db: Session, task_id: int):
    """Get all logs for a specific task"""
    return db.query(TaskLog).filter(TaskLog.task_id == task_id).all()


def log_task(db: Session, task_id: int, log_date: date, completed: bool):
    log = db.query(TaskLog).filter(
        TaskLog.task_id == task_id,
        TaskLog.date == log_date
    ).first()

    if log:
        log.completed = completed
    else:
        log = TaskLog(task_id=task_id, date=log_date, completed=completed)
        db.add(log)

    db.commit()
    return log

def daily_completion(db: Session, log_date: date):
    total = db.query(Task).count()
    completed = db.query(TaskLog).filter(
        TaskLog.date == log_date,
        TaskLog.completed == True
    ).count()

    if total == 0:
        return 0

    return round((completed / total) * 100, 2)

def monthly_completion(db: Session, year: int, month: int):
    total_tasks = db.query(Task).count()
    total_days = 30  # simplified for now

    completed_logs = db.query(TaskLog).filter(
        func.strftime('%Y', TaskLog.date) == str(year),
        func.strftime('%m', TaskLog.date) == f"{month:02}",
        TaskLog.completed == True
    ).count()

    if total_tasks == 0:
        return 0

    return round((completed_logs / (total_tasks * total_days)) * 100, 2)