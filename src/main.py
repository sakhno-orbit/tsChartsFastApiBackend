from fastapi import FastAPI

from src.middleware import CustomMW, CustomCorsMiddleware
from src.mongoose import default_collection

app = FastAPI()

app.add_middleware(CustomMW)
app.add_middleware(CustomCorsMiddleware)


@app.get('/')
async def get_chart_data_by_page():
    result = default_collection.find(
        {}, {'_id': 0, "header": 1, "page": 1, "datasets": 1, 'labels': 1})\
        .limit(10)
    return list(result)
