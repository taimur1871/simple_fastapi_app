#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# 2. Create app and model objects
app = FastAPI()

# 2. Create app and model objects
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates/")

#3. Welcome page
@app.get("/", response_class=HTMLResponse)
async def read_root(request:Request):
    return templates.TemplateResponse("welcome.html", {"request": request, "message":"message"})

@app.post("/uploads")
async def create_upload_file(request:Request):
    
    return templates.TemplateResponse("upload_page.html", {"request": request})

# 1. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload = True)