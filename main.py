from fastapi import FastAPI,Request,Form,Depends,HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List
from sqlalchemy.orm import Session
from models import Lists
from sqlalchemy.future import select
from database import get_db,Base,engine



Base.metadata.create_all(bind = engine)


app = FastAPI()
#app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def get_users_html(request: Request,db:Session = Depends(get_db)):
    items = db.query(Lists).all()
   
    return templates.TemplateResponse("index.html", {"request": request, "items":items})




@app.post("/delete/{item_id}", response_class=HTMLResponse)
async def  del_task(item_id:int, request:Request, db:Session = Depends(get_db)):
    task = db.query(Lists).filter(Lists.id == item_id).first()

    if task:
        db.delete(task)
        db.commit()

    items = db.query(Lists).all()
   
    return templates.TemplateResponse("index.html", {"request": request, "items":items})


@app.post("/post", response_class = HTMLResponse)
async def add_task(task_name:str = Form(...), request = Request, db:Session = Depends(get_db)):

    new_task = Lists(name = task_name)

    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    
    items = db.query(Lists).all()
    return templates.TemplateResponse("index.html", {"request": request, "items":items})
   




