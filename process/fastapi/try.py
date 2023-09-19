import uvicorn
import boto3
from fastapi import FastAPI, Response
from pydantic import BaseModel #BaseModel 상속없이 구현시, Item 클래스가 pydnatic field type이 아니라는 오류를 내뱉음

# DynamoDB 연결
dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')
table = dynamodb.Table('event')
app = FastAPI()

class Item(BaseModel):
    title: str
    year: int
    month: int
    start_day: int
    end_day: int
    goal: str
    place: str
    content: str

@app.post('/save_event/')
async def save_event(item: Item):
    # Convert item object to a dictionary
    item_data = item.dict()
    
    # Save data to DynamoDB table
    table.put_item(Item=item_data)
    
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



# # Put: 모든 내용을 바꾸느냐 / Patch: 일부의 내용을 바꾸냐
# @app.patch("/update/{event_id}")
# async def update_event(event_id: str, item: Item):
#     # 생성한 event 가져옴 From DynamoDB
#     existing_event = table.get_item(Key={'eventId': event_id}).get('Item')
#     if not existing_event:
#         return Response(content="<script>alert('수정할 내역이 존재하지 않습니다.');</script>", media_type="text/html")

#     # 선택적으로 변경할 데이터가 있는 경우에만 수정
#     updated_event = {**existing_event}
#     if item.title is not None:
#         updated_event['title'] = item.title
#     if item.year is not None:
#         updated_event['year'] = item.year
#     if item.month is not None:
#         updated_event['month'] = item.month
#     if item.start_day is not None:
#         updated_event['start_day'] = item.start_day
#     if item.end_day is not None:
#         updated_event['end_day'] = item.end_day
#     if item.goal is not None:
#         updated_event['goal'] = item.goal
#     if item.place is not None:
#         updated_event['place'] = item.place
#     if item.content is not None:
#         updated_event['content'] = item.content

#     # 수정한 Event 수정
#     table.put_item(Item=updated_event)

#     alert_message = "이벤트가 수정되었습니다."
#     return Response(content=f"<script>alert('{alert_message}');/</script>", media_type="text/html")

 