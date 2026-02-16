const PRODUCT_SERVICE_URL = "http://localhost:20001/products";
const ORDER_SERVICE_URL = "http://localhost:20002/orders";

let cart = {}; // {product_id: quantity}

const cartDiv = document.getElementById("cart");
const productsDiv = document.getElementById("products");
const submitBtn = document.getElementById("submit-order");

// get all products to list on startup
async function loadProducts() {
    try {
        const res = await fetch(PRODUCT_SERVICE_URL);
        const products = await res.json();

        productsDiv.innerHTML = "";
        products.forEach(product => {
            const box = document.createElement("div");
            box.className = "product-box";

            box.innerHTML = `
                <h3>${product.product_name}</h3>
                <p><strong>Price:</strong> $${product.price}</p>
                <p>${product.product_description}</p>
            `;

            const addBtn = document.createElement("button");
            addBtn.innerText = "Add to Order";
            addBtn.onclick = () => addToCart(product.id);

            const removeBtn = document.createElement("button");
            removeBtn.innerText = "Remove from Order";
            removeBtn.onclick = () => removeFromCart(product.id);

            box.appendChild(addBtn);
            box.appendChild(removeBtn);

            productsDiv.appendChild(box);
        });
    } catch (err) {
        productsDiv.innerHTML = "<p>Error loading products.</p>";
        console.error(err);
    }
}

// manage ur cart
function addToCart(productId) {
    if (!cart[productId]) cart[productId] = 0;
    cart[productId]++;
    updateCartDisplay();
}

function removeFromCart(productId) {
    if (cart[productId]) {
        cart[productId]--;
        if (cart[productId] <= 0) delete cart[productId];
    }
    updateCartDisplay();
}

function updateCartDisplay() {
    if (Object.keys(cart).length === 0) {
        cartDiv.innerText = "No items in cart";
    } else {
        const items = Object.entries(cart).map(([id, qty]) => `Product ${id}: ${qty}`).join(", ");
        cartDiv.innerText = `Cart: ${items}`;
    }
}

// submit orders
submitBtn.onclick = async () => {
    if (Object.keys(cart).length === 0) {
        cartDiv.innerText = "No items to submit";
        return;
    }

    try {
        for (const [productId, quantity] of Object.entries(cart)) {
            await fetch(ORDER_SERVICE_URL, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ product_id: parseInt(productId), quantity })
            });
        }

        cart = {};
        cartDiv.innerText = "Order processed";
    } catch (err) {
        cartDiv.innerText = "Error submitting order";
        console.error(err);
    }
};

// upon start
loadProducts();
