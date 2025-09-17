let subtitleBox = document.createElement('div');
subtitleBox.id = 'translator-subtitle-box';
subtitleBox.textContent = 'Translator taiyar hai. Shuru karne ke liye extension icon par click karein.';
document.body.appendChild(subtitleBox);

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.type === "subtitle" && request.data) {
    const messageData = request.data;
    if (messageData.status === 'translated') {
        subtitleBox.className = 'translated';
        subtitleBox.textContent = messageData.text;
    } else {
        subtitleBox.className = 'info';
        subtitleBox.textContent = messageData.text;
    }
  } else if (request.type === "status") {
    subtitleBox.className = 'info';
    subtitleBox.textContent = request.text;
  }
});

