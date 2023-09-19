import uvicorn
import boto3
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

# DynamoDB 연결
dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')
table = dynamodb.Table('event')
KeySchema=[
    {
        'AttributeName': 'title',
        'KeyType': 'HASH'  # Partition Key로 설정 (단일 속성 키)
    }
    ],
AttributeDefinitions=[
    {
        'AttributeName': 'title',
        'AttributeType': 'S'  # 'title' 속성의 데이터 타입 (S: 문자열, N: 숫자 등)
    }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
# 테이블이 생성되기를 기다립니다.
table.meta.client.get_waiter('table_exists').wait(TableName='event')

app = FastAPI()
templates = Jinja2Templates(directory="./")

class Item(BaseModel):
    title: str
    year: int
    month: int
    start_day: int
    end_day: int
    goal: str
    place: str
    content: str

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})
 

@app.post("/event_add", response_model=Item)
async def create_event(item: Item):
    # Extract data from the item
    title = item.title
    year = item.year
    month = item.month
    start_day = item.start_day
    end_day = item.end_day
    goal = item.goal
    place = item.place
    content = item.content
    
    # Save data to DynamoDB table
    table.put_item(
        Item={
            'title': title,
            'year': year,
            'month': month,
            'start_day': start_day,
            'end_day': end_day,
            'goal': goal,
            'place': place,
            'content': content
        }
    )
    alert_message = "저장되었습니다"
    return Response(content=f"<script>alert('{alert_message}');</script>", media_type="text/html")

@app.get("/get_all_events/")
async def get_all_events():
  # 테이블의 모든 이벤트 조회
  response = table.scan() #DB데이터를 조회해서 response에 담음

  #검색 결과에서 이벤트 목록 가져오기
  events = response.get('Items', []) #Items키에 해당하는 값을 전부 가져옴, 키가 존재하지 않으면 []반환.

  if not events:
    return Response(content="<script>alert('이벤트가 존재하지 않습니다.');</script>", media_type="text/html")
  
  # 조회한 모든 이벤트를 반환
  return events #조회된 Events를 Client에 반환

@app.get("/get_one_event/")
async def get_one_event(title: str):
    # Query the DynamoDB table to get the event with the specified title
    response = table.get_item(Key={'title': title})

    # Extract the event data from the response
    event = response.get('Item')

    if not event:
        return Response(content="<script>alert('이벤트가 존재하지 않습니다.');</script>", media_type="text/html")

    return event