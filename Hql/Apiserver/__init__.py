from fastapi import FastAPI, HTTPException
import uvicorn
from typing import TYPE_CHECKING, Optional, Union
import threading
from Hql.Helpers import can_thread
from Hql.Exceptions import HqlExceptions as hqle
import json

if TYPE_CHECKING:
    from Hql.Hac.Engine import HacEngine

class Apiserver():
    def __init__(self, hacengine:'HacEngine', host='127.0.0.1', port=8080):
        if not can_thread():
            raise hqle.CompilerException('Cannot start the api server as free threading is not supported, use the container?')

        self.hacengine = hacengine
        self.app = FastAPI()
        self.host = host
        self.port = port
        self.thread = None

        @self.app.get("/")
        def read_root():
            return {"I'm serving a": "youthful porpoise 🐬"}

        @self.app.get('/detection/{detection_id}/history')
        def get_detection_history(detection_id:str):
            if detection_id not in self.hacengine.detections:
                raise HTTPException(status_code=404, detail=f'Detection {detection_id} not found')
            return self.hacengine.detections[detection_id].run_history

        @self.app.get('/detection')
        def get_detections():
            detections = []
            for i in self.hacengine.detections:
                det = self.hacengine.detections[i]
                if not det.hac:
                    continue
                detections.append(det.hac.asm)
            return detections

        @self.app.get('/runs/{tid}')
        def get_run_by_id(tid:str):
            run = self.hacengine.get_by_id(tid)
            if run == None:
                raise HTTPException(status_code=404, detail=f'Run {tid} not found')
            return run.to_dict()

        @self.app.get('/runs')
        def get_runs():
            return self.hacengine.get_runs()

    def start(self):
        self.thread = threading.Thread(target=self.run, daemon=True)
        self.thread.start()

    def run(self):
        uvicorn.run(self.app, host=self.host, port=self.port, log_level="info")

    def join(self):
        if self.thread:
            self.thread.join()
