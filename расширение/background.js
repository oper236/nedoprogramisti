// background.js
// Этот файл служит сервис-воркером для расширения

console.log("YouTube Scent Sync Start");

// Пример обработки событий расширения
chrome.runtime.onInstalled.addListener((details) => {
  console.log("YouTube Scent Sync install", details);
});

// Можно добавить обработчики для других событий по мере необходимости
// Например:
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  console.log("give message:", message);
  // Обработка сообщений от других частей расширения
});

// Функция для проверки состояния подключения
async function checkConnection() {
  try {
    const response = await fetch("http://localhost:8000/health");
    return response.ok;
  } catch (error) {
    console.error("error connect:", error);
    return false;
  }
}

// Экспортируем функцию для использования в других частях расширения
// (например, в popup.js, если он будет добавлен)
if (typeof window !== 'undefined') {
  window.checkConnection = checkConnection;
}