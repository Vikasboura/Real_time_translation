document.getElementById('startButton').addEventListener('click', () => {
  const button = document.getElementById('startButton');
  button.textContent = 'Listening...';
  button.disabled = true;

  chrome.runtime.sendMessage({ command: "start" }, (response) => {
    if (chrome.runtime.lastError) {
      console.error(chrome.runtime.lastError.message);
      button.textContent = 'Error!';
    } else {
      console.log('Start command bhej diya gaya hai.');
    }
  });
});

