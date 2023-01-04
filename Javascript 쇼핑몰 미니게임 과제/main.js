//Fetch the imtes from the Json file
function loadItems() {
    return fetch('data/data.json')
    .then(response => response.json())
    .then(json => json.items);
}

function displayItems(item) {
    const container = document.querySelector('.items');
    container.innerHTML = items.map(item=>createHTMLString(item)).join('');
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