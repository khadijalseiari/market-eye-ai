import os
import sqlite3
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel
from passlib.context import CryptContext

# ——— Config & DB helpers ———
DB_PATH = os.path.join(os.path.dirname(__file__), "market_eye.db")
pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

# ——— Request schemas ———
class UserIn(BaseModel):
    username: str
    password: str

app = FastAPI(title="Market Eye Auth")

# ——— Signup endpoint ———
@app.post("/signup", status_code=status.HTTP_201_CREATED)
def signup(user: UserIn, db: sqlite3.Connection = Depends(get_db)):
    hashed = pwd_ctx.hash(user.password)
    try:
        db.execute(
            "INSERT INTO users (username, password_hashed) VALUES (?, ?)",
            (user.username, hashed),
        )
        db.commit()
        user_id = db.execute(
            "SELECT user_id FROM users WHERE username = ?", (user.username,)
        ).fetchone()["user_id"]
        db.execute(
            "INSERT INTO activity_logs (user_id, action) VALUES (?, ?)",
            (user_id, "signup"),
        )
        db.commit()
        return {"message": "User created"}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=409, detail="Username already exists")

# ——— Login endpoint ———
@app.post("/login")
def login(user: UserIn, db: sqlite3.Connection = Depends(get_db)):
    row = db.execute(
        "SELECT * FROM users WHERE username = ?", (user.username,)
    ).fetchone()
    if not row or not pwd_ctx.verify(user.password, row["password_hashed"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    db.execute(
        "INSERT INTO activity_logs (user_id, action) VALUES (?, ?)",
        (row["user_id"], "login"),
    )
    db.commit()
    return {"message": "Login successful"}