import uvicorn
import boto3
from fastapi import FastAPI, Response, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

# DynamoDB 연결
dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-2')
table = dynamodb.Table('event')
app = FastAPI()
templates = Jinja2Templates(directory="templates")  # Create a templates directory to store HTML templates

class Item(BaseModel):
    title: str
    year: int
    month: int
    start_day: int
    end_day: int
    goal: str
    place: str
    content: str

@app.post('/save_event/', response_class=HTMLResponse)
async def save_event(request: Request, item: Item):
    # Extract the data from the Pydantic model
    title = item.title
    year = item.year
    month = item.month
    start_day = item.start_day
    end_day = item.end_day
    goal = item.goal
    place = item.place
    content = item.content

    # Save the data to DynamoDB
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
    return templates.TemplateResponse("index.html", {"request": request, "alert_message": alert_message})

# Create a route to render the form page
@app.get("/event_form/", response_class=HTMLResponse)
async def event_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/get_all_events/", response_class=HTMLResponse)
async def get_all_events(request: Request):
    # Your existing code to fetch all events from DynamoDB

    return templates.TemplateResponse("index.html", {"request": request, "events": events})

# Add other routes and functions as needed

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
