#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26
"""

# 1. Library imports
import uvicorn
import gunicorn
import os
from fastapi import FastAPI

# Create app and model objects
application = FastAPI()

# Run the API with gunicorn
if __name__ == '__main__':
    #uvicorn.run('main:app', host='127.0.0.1', port=8000)
    #gunicorn('main:app', uvicorn.workers.UvicornWorker, workers=4)
    os.system('gunicorn -w 1 -k uvicorn.workers.UvicornWorker main:app')