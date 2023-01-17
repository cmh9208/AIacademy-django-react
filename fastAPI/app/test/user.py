from typing import List

from sqlalchemy.orm import Session
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse
from app.cruds.user import UserCrud
from app.admin.security import get_hashed_password, generate_token
from app.admin.utils import current_time
from app.database import get_db
from app.schemas.user import UserDTO
from fastapi import APIRouter, Depends, File, UploadFile

router = APIRouter()

'''
@router.post("/files/upload")
def create_files(files: List[bytes] = File(...)):
    return {"file_sizes": [len(file) for file in files]}
@router.post("/uploadfiles/")
def create_upload_files(files: List[UploadFile] = File(...)):
    return {"filenames": [file.filename for file in files]}
@router.get("/files")
async def upload_file():
    content = """
    <body>
    <form action="/files/" enctype="multipart/form-data" method="post">
    <input name="files" type="file" multiple>
    <input type="submit">
    </form>
    <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
    <input name="files" type="file" multiple>
    <input type="submit">
    </form>
    </body>
        """
    return HTMLResponse(content=content)
'''


@router.get("/register")
async def join():
    return HTMLResponse(content="""
    <body>
    <form action="/files/" enctype="multipart/form-data" method="post">
    <input name="files" type="file" multiple>
    <input type="submit">
    </form>
    <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
    <input name="files" type="file" multiple>
    <input type="submit">
    </form>
    </body>
        """)


@router.get("/users/login")
async def login():
    return HTMLResponse(content="""
    <body>
    <form action="http://localhost:8000/users/login" method="post" style="width:300px; margin: 50 auto">

    <div class="container">
      <label for="uname"><b>Username</b></label>
      <input type="text" placeholder="Enter Username" name="email" required>
        <br/>
      <label for="psw"><b>Password</b></label>
      <input type="password" placeholder="Enter Password" name="password" required>
      <br/>
      <button type="submit">Login</button>

    </div>


  </form>
    </body>
        """)


@router.get("/test/join")
async def test():
    return HTMLResponse(content="""
    <body>
    <form action="/files/" enctype="multipart/form-data" method="post">
    <input name="files" type="file" multiple>
    <input type="submit">
    </form>
    <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
    <input name="files" type="file" multiple>
    <input type="submit">
    </form>
    </body>
        """)