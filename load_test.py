import requests
import threading
import time

URL = "http://13.51.171.98:5000/"  # заміни на адресу свого сервісу
THREADS = 20      # кількість одночасних потоків
DURATION = 60     # тривалість тесту в секундах

def worker():
    end_time = time.time() + DURATION
    while time.time() < end_time:
        try:
            response = requests.get(URL)
            print(f"Status: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")

threads = []
for _ in range(THREADS):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("Load test finished.")