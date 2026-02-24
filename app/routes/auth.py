from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import User
from ..core.security import hash_password, verify_password, create_access_token
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas

router = APIRouter(prefix="/auth", tags=["Auth"])

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally: 
        db.close()

@router.post("/register", status_code=201)
def register(user: schemas.UserCreate, db : Session= Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"        
        )
    
    hashed_pw = hash_password(user.password)

    new_user = User(
        email = user.email,
        hashed_password=hashed_pw
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message" : "User registered successfully"}

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    db_user = db.query(User).filter(User.email == form_data.username).first()

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )

    if not verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    
    access_token = create_access_token({"sub" : str(db_user.id)})

    return{
        "access_token" : access_token,
        "token_type" : "bearer"
    }