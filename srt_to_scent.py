
from youtube_transcript_api import YouTubeTranscriptApi
import json
import re

# Ключевые слова и соответствующие ароматы
KEYWORDS_TO_SCENTS = {
    "кофе": "coffee",
    "лес": "pine",
    "море": "ocean",
    "любовь": "rose",
    "смерть": "smoke",
    "огонь": "fire",
    "еда": "vanilla",
    "сон": "lavender"
}
video_id = str(input())

def find_scent_for_text(text):
    for keyword, scent in KEYWORDS_TO_SCENTS.items():
        if re.search(rf"\\b{keyword}\\b", text, re.IGNORECASE):
            return scent
    return None

def seconds_to_hms(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = int(seconds % 60)
    return f"{h:02}:{m:02}:{s:02}"

def generate_scent_track(video_id, output_file="output.scent"):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['ru', 'en'])
        print(f"[INFO] Загружено {len(transcript)} строк из субтитров")
    except Exception as e:
        print(f"[ERROR] Не удалось получить субтитры: {e}")
        return

    scent_events = []
    for entry in transcript:
        scent = find_scent_for_text(entry['text'])
        print(f"[DEBUG] {entry['start']} | {entry['text']} -> {scent}")
        if scent:
            scent_events.append({
                "time": seconds_to_hms(int(entry['start'])),
                "scent": scent
            })

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(scent_events, f, indent=2, ensure_ascii=False)

    print(f"[OK] Сохранено {len(scent_events)} событий в файл {output_file}")

# Пример использования:
# generate_scent_track("dQw4w9WgXcQ")
