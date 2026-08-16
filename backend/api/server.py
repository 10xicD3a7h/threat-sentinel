from fastapi import FastAPI, WebSocket
import asyncio
import json
import time
from fastapi.middleware.cors import CORSMiddleware
from engine.collector import Collector
from engine.detector import Detector
from engine.classifier import Classifier

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.websocket("/ws")
async def websocket_endpoiint(ws: WebSocket):
    await ws.accept()
    collector = Collector()
    detector = Detector()
    classifier = Classifier()
    while(True):
        events = collector.get_process_events()
        await ws.send_text(json.dumps({
            'type': 'log',
            'message': f'Scan complete - {len(events)} new processes checked',
            'timestamp': time.time()
        }))
        for event in events:
            check = detector.check_process(event)

            if check is not None:
                threat = classifier.classify(event, check)
                await ws.send_text(json.dumps({
                    'type': 'threat',
                    'data': threat
                }))
        await asyncio.sleep(5)



