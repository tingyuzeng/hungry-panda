const testH2 = document.querySelector('#testH2');

console.log('this is from popup.js');

async function testApi() {
  fetch('http://127.0.0.1:5000/')
    .then((res) => {
      return res.json();
    })
    .then((data) => {
      testH2.textContent = data.text;
    })
    .catch((err) => {
      console.error(err);
    });
}

testApi();
