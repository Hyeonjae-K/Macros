let g_process = 0;
let g_size = null;

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message === "get_status") {
    if (g_process) {
      g_process++;
    }
    sendResponse([g_process, g_size]);
  }
});

function runFunction(input_size) {
  g_size = input_size;
  g_process = 1;
}

function resetFunction() {
  g_process = 0;
}