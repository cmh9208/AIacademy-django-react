FROM python:3.9

WORKDIR /app
ADD requirements.txt .
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "app.main:app","-D", "--reload=True", "--host", "mydb.cvlrgnvb9mkf.ap-northeast-2.rds.amazonaws.com", "--port", "8000"]
