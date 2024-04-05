const productElement = document.getElementById("product")

const productId = productElement.dataset['id']
if (productId) {
    fetch(`/api/product?id=${productId}`)
        .then(res => res.json())
        .then((data) => {
            if (data.data) {
                const product = data.data
                productElement.innerHTML = `
                <img src="${product.image}" width="300" />
                <div>
                    <h2>${product.name}</h2>
                    <p>${product.description}</p>
                    <p>Sotuvchi: <a class="seller" href="/seller/${product.sellerId}">${product.sellerName}</a></p>
                    <p>Narx: <span class="price">${Intl.NumberFormat('ru').format(product.price)} so'm</span></p>
                </div>
                `
            }
        })
}