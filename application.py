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
application = FastAPI()
#application.mount("/static", StaticFiles(directory="static"), name="static")
#templates = Jinja2Templates(directory="templates/")

# 1. Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000)