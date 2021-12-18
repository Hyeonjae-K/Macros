chrome.runtime.sendMessage('get_status', (response) => {
  let [process, size] = response;
  
  if (process === 2) {
    const sizes = document.querySelectorAll("body > div> div > div > div > div > section > div > aside > div > div > div > div > div > form > div > div > ul > li");
    const buy_btn = document.querySelector('#btn-buy');
    let possible_size = null;
    
    sizes.forEach(function(elem) {
      if (elem.textContent <= size) {
        possible_size = elem
      }
    })

    const select = setInterval(function() {
      if (possible_size.className === 'list') {
        possible_size.querySelector('a').click();
        buy_btn.click();
      }
    })
  }

  else if (process === 3) {
    const next_btn = document.querySelector('#btn-next');
    next_btn.click();
  }

  else if (process === 4) {
    document.querySelector('#payment-review > div.body > ul > li:nth-child(1) > div.payment-method-list > div:nth-child(1) > h6').click(); // 카카오페이
    document.querySelector('#isCheckoutAgree').click();
    const payment = setInterval(function() {
      const btn = document.querySelector('#complete_checkout > button');
      if (!btn.className.includes('disabled')) {
        btn.click();
      }
    })
  }
});