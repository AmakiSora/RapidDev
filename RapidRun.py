"""
    程序入口
"""
import uvicorn
from fastapi import FastAPI
from quotations import app_quotation

app = FastAPI()

app.include_router(app_quotation, prefix='/quotation', tags=['语录集'])

if __name__ == '__main__':
    uvicorn.run(app='RapidRun:app', host='127.0.0.1', port=2233, reload=True, debug=True, workers=1)