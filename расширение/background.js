// background.js
// Этот файл служит сервис-воркером для расширения

console.log("Сервис-воркер YouTube Scent Sync запущен");

// Пример обработки событий расширения
chrome.runtime.onInstalled.addListener((details) => {
  console.log("Расширение YouTube Scent Sync установлено", details);
});

// Можно добавить обработчики для других событий по мере необходимости
// Например:
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  console.log("Получено сообщение:", message);
  // Обработка сообщений от других частей расширения
});

// Функция для проверки состояния подключения
async function checkConnection() {
  try {
    const response = await fetch("http://localhost:8000/health");
    return response.ok;
  } catch (error) {
    console.error("Ошибка подключения к серверу ароматов:", error);
    return false;
  }
}

// Экспортируем функцию для использования в других частях расширения
// (например, в popup.js, если он будет добавлен)
if (typeof window !== 'undefined') {
  window.checkConnection = checkConnection;
}