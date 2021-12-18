const run_btn = document.getElementById("run-btn");
const reset_btn = document.getElementById("rest-btn");

run_btn.addEventListener("click", function() {
  const url = document.getElementById("url").value;
  const size = document.getElementById("size").value;
  chrome.runtime.getBackgroundPage(function(background) {
    background.runFunction(size);
    chrome.tabs.executeScript(null, {code: `
    window.location.href = '${ url }';
    `})
  })
})

reset_btn.addEventListener("click", function() {
  chrome.runtime.getBackgroundPage(function(background) {
    background.resetFunction();
  })
})