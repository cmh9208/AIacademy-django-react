from fastapi import FastAPI
from starlette.responses import HTMLResponse
from datetime import datetime
import pytz

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

def current_time():
    return f"{datetime.now(pytz.timezone('Asia/Seoul')).strftime('%Y-%m-%d %H:%M:%S')}"

@app.get("/")
async def home():
    return HTMLResponse(content=f"""
    <body>
    <div>
        <h1 style="width:400px;margin:50px auto">
            {current_time()} <br/>
            현재 서버 구동 중 입니다. 
         </h1>
    </div>
    </body>
        """)

# uvicorn app.main:app -D --reload=True --host mydb.cvlrgnvb9mkf.ap-northeast-2.rds.amazonaws.com --port 8000
#
# @app.get("/schedule")
# async def root():
#     return {"날짜를 기준으로 일정을 가져옵니다."}
#
#
# @app.post("/schedule")
# async def say_hello(name: str):
#     return {"새로운 일정을 생성합니다."}
#
# @app.delete("/schedule")
# async def say_hello(name: str):
#     return {"특정 일정을 삭제합니다."}
#
# @app.post("/schedule")
# async def say_hello(name: str):
#     return {"새로운 일정을 생성합니다."}