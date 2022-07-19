
setInterval(() => {
  document.querySelectorAll('div[role="presentation"]').forEach((el) => {
    if (el.innerHTML === 'Brad is typing') {
      el.innerHTML = 'Brad is typing something highly inappropriate';
    }
  });
}, 250);
