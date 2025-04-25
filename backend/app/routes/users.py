from fastapi import APIRouter, HTTPException, Depends, UploadFile, File
from fastapi.responses import JSONResponse
import shutil
import os
from sqlalchemy.orm import Session
from core.db import get_db
from models.model import UserDB
from schemas.users import UserCreate, User
from routes.auth import is_admin, get_current_user
from fastapi import UploadFile, File

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.get("/get")
def get_users(admin_check: bool = Depends(is_admin), db : Session = Depends(get_db)):
    users = db.query(UserDB).order_by(UserDB.id).all()

    if not users:
        raise HTTPException(status_code=404, detail="Error, users not found")
    
    return users



@router.post("/upload-pfp")
def upload_profile_picture(db : Session = Depends(get_db), file: UploadFile = File(...), user : dict = Depends(get_current_user)):
    user = db.query(UserDB).filter(UserDB.id == user.id).first()

    user.picture = f"{user.id}_pfp.png"
    filepath = f"static/pfps/{user.picture}"


    with open(filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    db.commit()
    db.refresh(user)

    return {"Success" : "Saved successfully"}


@router.delete("/delete")
def delete_user(user_id : int, admin_check: bool = Depends(is_admin), db : Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="Error, user not found")
    
    db.delete(user)
    db.commit()

    return {"Success" : f"User {user.username} deleted successfully"}

@router.delete("/delete-currentuser")
async def delete_currentuser(user : dict = Depends(get_current_user), db : Session = Depends(get_db)):
    user = db.query(UserDB).filter(UserDB.id == user.id).first()
    
    db.delete(user)
    db.commit()

    return user
