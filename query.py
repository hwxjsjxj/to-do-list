import database
from sqlalchemy import func

def add_task(user_id: int, task_text: str) -> str:
    if database.session.query(database.Task).filter_by(user_id = user_id,text = task_text).first():
        return 'такая задача уже есть'
    else:
        all_task = database.session.query(func.max(database.Task.task_id)).filter(database.Task.user_id==user_id).scalar() or 0
        new_task = database.Task(text=task_text, user_id=user_id, task_id=all_task+1)
        database.session.add(new_task)
        database.session.commit()
        return 'задача успешно добавлена'
    

def view_task(user_id: int) -> str:
    all_task = database.session.query(database.Task).filter_by(user_id=user_id).all()
    
    result = ""
    
    for tasks in all_task:
        result += f"{tasks.task_id} {tasks.text}" + "\n"
    
    return result

def remove_task(user_id: int, task_id: int) -> str:
    task_to_remove = database.session.query(database.Task).filter_by(user_id=user_id, task_id=task_id).first()
    if task_to_remove:
        database.session.delete(task_to_remove)
        database.session.commit()
        return 'задача успешно удалена'
    else:
        return 'такой задачи нет'
    
def change_task(user_id: int, task_id: int, new_text: str) -> str:
    task_to_change = database.session.query(database.Task).filter_by(user_id=user_id, task_id=task_id).first()
    if task_to_change:
        task_to_change.text = new_text
        database.session.commit()
        return 'задача успешно изменена'
    else:
        return 'такой задачи нет'