print("Threat Sentinel backend starting")

from engine.collector import Collector
from engine.detector import Detector
from engine.classifier import Classifier
from engine.logger import Logger

collector = Collector()
detector = Detector()
classifier = Classifier()
logger = Logger()

events  = collector.get_process_events()

for event in events:
    match = detector.check_process(event)
    if match:
        threat = classifier.classify(event, match)
        logger.log_threat(threat)

#rows = logger.cursor.execute('SELECT * FROM threats LIMIT 5').fetchall()
#for row in rows:
#    print(row)