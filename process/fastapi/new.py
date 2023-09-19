from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

import boto3
import uvicorn

# DynamoDB 연결
dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')
table = dynamodb.Table('event')
app = FastAPI()
templates = Jinja2Templates(directory='./')

class Item(BaseModel):
    title: str
    year: int
    month: int
    start_day: int
    end_day: int
    goal: str
    place: str
    content: str

@app.get('/')
async def home(request: Request): 
  return templates.TemplateResponse("real.html", {"request":request})

