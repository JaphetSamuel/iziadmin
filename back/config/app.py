from fastapi import FastAPI
from config.db import init_db
from fastapi_events.handlers.local import local_handler
from fastapi_events.middleware import EventHandlerASGIMiddleware
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    on_startup=[init_db],
    debug=True
)

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"])

app.add_middleware(EventHandlerASGIMiddleware,handlers=[local_handler])



