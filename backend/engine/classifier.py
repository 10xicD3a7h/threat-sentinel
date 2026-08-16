class Classifier:
    def classify(self, event, signature):
        threat_dic = {
            'name': signature['name'],
            'severity': signature['severity'],
            'category': signature['category'],
            'source': f"local:PID {event['data']['pid']}",
            'confidence': 0.5,
            'timestamp': event['timestamp']
        }
        if event['data']['exe'] is not None and 'System32' not in event['data']['exe']:
            threat_dic['confidence'] = 0.8

        return threat_dic
