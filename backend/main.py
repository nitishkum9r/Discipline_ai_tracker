from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import crud, schemas
from datetime import date
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Nitish 2026 Discipline API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/tasks", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task.title)


@app.get("/tasks", response_model=list[schemas.TaskResponse])
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)


@app.post("/log")
def log_task(log: schemas.TaskLogCreate, db: Session = Depends(get_db)):
    return crud.log_task(db, log.task_id, log.date, log.completed)


@app.get("/logs/task/{task_id}")
def get_task_logs(task_id: int, db: Session = Depends(get_db)):
    """Get all logs for a specific task"""
    return crud.get_task_logs(db, task_id)


@app.get("/stats/daily")
def get_daily_stats(log_date: date, db: Session = Depends(get_db)):
    return {"daily_completion": crud.daily_completion(db, log_date)}


@app.get("/stats/monthly")
def get_monthly_stats(year: int, month: int, db: Session = Depends(get_db)):
    return {"monthly_completion": crud.monthly_completion(db, year, month)}