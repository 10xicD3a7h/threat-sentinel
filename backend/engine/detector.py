
class Detector:
    def __init__(self):
        self.signatures = [
            # Credential theft
            {'name': 'Mimikatz credential dumper', 'pattern': 'mimikatz', 'severity': 'critical', 'category': 'Intrusion'},
            {'name': 'PWDump password extractor', 'pattern': 'pwdump', 'severity': 'critical', 'category': 'Intrusion'},
            {'name': 'LaZagne credential stealer', 'pattern': 'lazagne', 'severity': 'critical', 'category': 'Intrusion'},

            # Remote access
            {'name': 'Metasploit Meterpreter', 'pattern': 'meterpreter', 'severity': 'critical', 'category': 'Intrusion'},
            {'name': 'Netcat reverse shell', 'pattern': 'netcat', 'severity': 'high', 'category': 'Intrusion'},
            {'name': 'DarkComet RAT', 'pattern': 'darkcomet', 'severity': 'critical', 'category': 'Malware'},

            # Ransomware
            {'name': 'WannaCry ransomware', 'pattern': 'wannacry', 'severity': 'critical', 'category': 'Malware'},
            {'name': 'REvil ransomware', 'pattern': 'revil', 'severity': 'critical', 'category': 'Malware'},

            # Cryptominers
            {'name': 'XMRig cryptominer', 'pattern': 'xmrig', 'severity': 'high', 'category': 'Malware'},
            {'name': 'Cryptomining malware', 'pattern': 'cryptominer', 'severity': 'high', 'category': 'Malware'},

            # Reconnaissance
            {'name': 'Nmap network scanner', 'pattern': 'nmap', 'severity': 'medium', 'category': 'Recon'},
            {'name': 'Masscan port scanner', 'pattern': 'masscan', 'severity': 'medium', 'category': 'Recon'},
        ]

    def check_process(self, event):
        name = event['data']['name']
        for sig in self.signatures:
            if sig['pattern'] in name:
                return sig
        return None


