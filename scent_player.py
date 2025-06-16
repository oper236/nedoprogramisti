import json
import time
from datetime import timedelta

#  Заглушка вместо настоящего Smeller

class FakeSmeller:
    def send_scent(self, scent_name):
        print(f"[ЗАГЛУШКА] Эмуляция отправки аромата: {scent_name}")

def parse_time(t: str) -> int:
    """Преобразует строку 'чч:мм:сс' в секунды"""
    h, m, s = map(int, t.split(":"))
    return h * 3600 + m * 60 + s

def load_scent_track(file_path: str):
    with open(file_path, 'r') as f:
        return sorted(json.load(f), key=lambda x: parse_time(x['time']))

def play_scented_track(track, smeller, start_time=0):
    start = time.time()
    i = 0
    while i < len(track):
        elapsed = time.time() - start + start_time
        scent_time = parse_time(track[i]['time'])
        if elapsed >= scent_time:
            scent_name = track[i]['scent']
            print(f"[{timedelta(seconds=int(elapsed))}] Выпуск аромата: {scent_name}")
            smeller.send_scent(scent_name)
            i += 1
        else:
            time.sleep(0.5)

if __name__ == "__main__":
    smeller = FakeSmeller()  # 👈 Используем заглушку
    scent_track = load_scent_track("example_track.scent")
    print("Старт аромадорожки!")
    play_scented_track(scent_track, smeller)