Threat-Sentinel: by Aditya Sahu
This project is an attempt to create a HIDS(lightweight intrusion detection system), 
though it is still missing many more functionalities such as Network Monitor etc,
it is still a fully functioning web application.

# Project Structure 
```
threat-sentinel/        ← React frontend
backend/
├── engine/
│   ├── collector.py   ← process monitoring
│   ├── detector.py    ← signature matching
│   ├── classifier.py  ← confidence scoring
│   └── logger.py      ← SQLite persistence
└── api/
    └── server.py      ← WebSocket bridge
```

# Prerequisites
- you need a chromium based browser for the frontend
- clone this repository in your system
- cd into threat-sentinal, run "npm install"
- cd into backend, run "pip install -r requirements.txt"

# version requirements
- Python 3.8 or higher
- Node.js 16 or higher

# running backend first
- cd to backend
- in terminal "uvicorn api.server:app --reload"

# running frontend
- cd to threat-sentinel 
- run "npm run dev"
- follow the link to your browser

// viol`a there you have my HIDS working on your pc