from youtube_transcript_api import YouTubeTranscriptApi

video_id = input("Введите ID видео: ")

try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['ru', 'en'])
    print(f"[INFO] Субтитры загружены: {len(transcript)} строк.")
except Exception as e:
    print(f"[ERROR] Не удалось получить субтитры: {e}")
    exit(1)  # нормальный выход с ошибкой, не -1
