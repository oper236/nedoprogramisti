
function getCurrentTimeSeconds() {
  const video = document.querySelector("video");
  return video ? Math.floor(video.currentTime) : 0;
}

async function syncTime() {
  const ts = getCurrentTimeSeconds();
  await fetch(`http://localhost:8000/time?ts=${ts}`);
  console.log("[SYNC] Время отправлено:", ts);
}

async function startScentTrack() {
  await fetch("http://localhost:8000/start");
  console.log("[SYNC] Аромадорожка запущена");
}

window.addEventListener("trigger-scent", async () => {
  await syncTime();
  await startScentTrack();
});
