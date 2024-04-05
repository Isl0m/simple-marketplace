const sellerElement = document.getElementById("seller")

const sellerId = sellerElement.dataset['id']
if (sellerId) {
    fetch(`/api/seller?id=${sellerId}`)
        .then(res => res.json())
        .then((data) => {
            if (data.data) {
                const seller = data.data
                sellerElement.innerHTML = `
                ${seller.banner ? `<img src="${seller.banner}" width="1000"/>` : ""}
                <div id="seller-details">
                    ${seller.profileImage ? `<img src="${seller.profileImage}" width="50" height="50"/>` : ''}
                    <div>
                        <h2>${seller.name}</h2>
                        <p>${seller.description}</p>
                    </div>
                </div>
                `
            }
        })
}