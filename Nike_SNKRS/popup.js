const run_btn = document.getElementById("runBtn");
const reset_btn = document.getElementById("resetBtn");

run_btn.addEventListener("click", function() {
  const url = document.getElementById("url").value;
  const size = document.getElementById("size").value;
  chrome.runtime.getBackgroundPage(function(background) {
    background.runFunction(size);
    chrome.tabs.executeScript(null, {code: `
    console.log('${ url }');
    window.location.href = '${ url }';
    `})
  })
})

reset_btn.addEventListener("click", function() {
  chrome.runtime.getBackgroundPage(function(background) {
    background.resetFunction();
  })
})