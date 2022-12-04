chrome.tabs.query({ active: true, lastFocusedWindow: true }, (tabs) => {
  chrome.tabs.sendMessage(tabs[0].id, { hungryPanda: 'START' }, (res) => {
    console.log(res.reviews);
  });
});

const testH2 = document.querySelector('#testH2');

const mocked_data = [
  {
    text: 'chicken',
  },
  {
    text: 'beef',
  },
  {
    text: 'beef',
  },
  {
    text: 'pork',
  },
  {
    text: 'fish',
  },
];

/**
 *
 * @param {Array} arr
 */
function sortList(arr) {
  const counter = new Map();
  arr.forEach((item) => {
    const count = (counter.get(item.text)?.count || 0) + 1;
    counter.set(item.text, { count, item });
  });
  const mapArr = Array.from(counter.entries());
  mapArr.sort((a, b) => b[1].count - a[1].count);
  return mapArr.map((mappedItem) => mappedItem[1].item);
}

const ulElement = document.createElement('ul');
const sortedMockedData = sortList(mocked_data);
sortedMockedData.forEach((dish) => {
  const li = document.createElement('li');
  li.innerHTML = `<span>${dish.text}</span>`;
  ulElement.appendChild(li);
});
document.body.appendChild(ulElement);

// console.log('this is from popup.js');

// async function testApi() {
//   fetch('http://127.0.0.1:5000/')
//     .then((res) => {
//       return res.json();
//     })
//     .then((data) => {
//       testH2.textContent = data.text;
//     })
//     .catch((err) => {
//       console.error(err);
//     });
// }

// testApi();
