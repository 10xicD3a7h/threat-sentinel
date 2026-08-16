import psutil
import time


class Collector:
    def __init__(self):
        self.seen_pids = set()

    def get_processes(self):
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'username', 'exe', 'cmdline']):
            processes.append({
                                'pid':proc.pid,
                                'name':proc.info['name'],
                                'username':proc.info['username'],
                                'exe': proc.info['exe'],
                                'cmdline': proc.info['cmdline']
                                })
        return processes

    def get_process_events(self):
        events = []
        for proc in self.get_processes():
            pid = proc['pid']
            if pid not in self.seen_pids:
                self.seen_pids.add(pid)
                event = {
                    'type' : 'process',
                    'timestamp': time.time(),
                    'data': proc
                }
                events.append(event)
        print(f"New events this cycle: {len(events)}")
        return events