//Fetch the imtes from the Json file
function loadItems() {
    return fetch('data/data.json')
    .then(response => response.json())
    .then(json => json.items);
}

function displayItems(item) {
    const container = document.querySelector('.items');
    container.innerHTML = item.map(item=>createHTMLString(item)).join('');
}

function onButtonClick(event,items) {
    const dataset = event.target.dataset;
    const key = dataset.key;
    const value = dataset.value;

    if(key == null || value == null) {
        return ;
    }
    displayItems(items.filter(items[key]===value))
}

function setEventListeners(items) {
    const logo = document.querySelector('.logo');
    const buttons = document.querySelector('.buttons');
    logo.addEventListener('click', () => displayItems(items));
    buttons.addEventListener('click',event=>onButtonClick(event,items));
}
function createHTMLString(item) {
    return `
    <li class="item">
        <img src="${item.image}" alt="${item.type}" class="item__thumbnail" />
        <span class="item__description">${item.gender}, ${item.size}</span>
    </li>
    `
}
//main


loadItems()
    .then(items =>{
        displayItems(items);
        setEventListeners(items)
    })
.catch(console.log)