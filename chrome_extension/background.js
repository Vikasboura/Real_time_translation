let port = null;
const hostName = "com.vikas.translator";

function sendToContentScript(message) {
  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    if (tabs[0] && tabs[0].id) {
      chrome.tabs.sendMessage(tabs[0].id, message, (response) => {
        if (chrome.runtime.lastError) {
          console.log(`Content script taiyar nahi: ${chrome.runtime.lastError.message}`);
        }
      });
    }
  });
}

function connect() {
  console.log(`Native host se connect ho raha hai: ${hostName}`);
  sendToContentScript({ type: "status", text: "Connecting..." });
  port = chrome.runtime.connectNative(hostName);

  port.onMessage.addListener((message) => {
    console.log("Native message prapt hua:", message);
    sendToContentScript({ type: "subtitle", data: message });
  });

  port.onDisconnect.addListener(() => {
    if (chrome.runtime.lastError) {
      const errorMsg = `Error: ${chrome.runtime.lastError.message}`;
      console.error("Error ke saath disconnect hua:", errorMsg);
      sendToContentScript({ type: "status", text: errorMsg });
    } else {
      console.log("Native host se disconnect ho gaya.");
      sendToContentScript({ type: "status", text: "Disconnected. Dobara koshish karne ke liye start par click karein." });
    }
    port = null;
  });
}

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.command === "start") {
    if (!port) {
      connect();
    }
    port.postMessage({ 
        command: "start",
        config: {
            // null set karne se Python apne aap default audio device chun lega.
            // Yeh sabse bharosemand (reliable) tareeka hai.
            meeting_audio_index: 3, 
            meeting_language: "en-US",
            your_language: "hi-IN"
        }
    });
    sendResponse({ status: "started" });
  }
  return true;
});

