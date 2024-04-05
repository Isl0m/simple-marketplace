function compactText(text) {
    if (text.length > 50) {
        return `${text.slice(0, 50)}...`
    }
    return text
}

fetch("/api/product").then(res => res.json()).then(data => {
    const products = document.getElementById('products')
    if (data.data) {
        products.innerHTML = data.data
            .map(product =>
                `<li id="product">
                    <a href="/product/${product.id}">
                        <img src="${product.image}" width="250" />
                        <h4>${compactText(product.name)}</h4>
                        <p>${Intl.NumberFormat('ru').format(product.price)} so'm</p>
                    </a>
                </li>`).join('\n')
    }
})
