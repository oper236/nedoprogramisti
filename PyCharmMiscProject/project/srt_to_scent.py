import json
import re
import os
from kinopoisk_dev import KinopoiskDev

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

def find_scent_for_text(text):
    for kw, scent in KEYWORDS_TO_SCENTS.items():
        if re.search(rf"\b{kw}\b", text, re.IGNORECASE):
            return scent
    return None

def generate_scent_track_by_id(kp_id, output_file='output.scent'):
    try:
        # токен кинопоиск.дев
        kp = KinopoiskDev(token='BY6ZPZQ-FB4MHTZ-HEYZ2AW-HKFT1BV')

        print(f"[INFO] Получаю данные о фильме с ID {kp_id}...")
        movie = kp.find_one_movie(kp_id)

        if not movie:
            print("[ОШИБКА] Фильм не найден.")
            return

        # Инициализация списка для ароматов
        scent_events = []

        # Проверяем поля, где могут быть ключевые слова
        texts = [
            ("описание", getattr(movie, 'description', None)),
            ("слоган", getattr(movie, 'slogan', None)),
        ]

        for поле, текст in texts:
            if текст:
                аромат = find_scent_for_text(текст)
                print(f"[DEBUG] {поле}: {текст} -> {аромат}")
                if аромат:
                    scent_events.append({
                        "поле": поле,
                        "аромат": аромат,
                        "время": None  # нет таймингов
                    })

        # Если ароматов нет, выводим информацию
        if not scent_events:
            print("[INFO] Не найдено ароматов по ключевым словам.")

        # Сохраняем результат в файл
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(scent_events, f, ensure_ascii=False, indent=2)

        путь = os.path.abspath(output_file)
        print(f"[OK] Сохранено {len(scent_events)} событий в файл: {путь}")

    except Exception as e:
        print(f"[ОШИБКА] Что-то пошло не так: {e}")

# Запуск с примером ID
generate_scent_track_by_id(462606)  # Пример ID фильма