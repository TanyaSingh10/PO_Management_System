const API = "http://127.0.0.1:8001";

let TOKEN = localStorage.getItem("token");
let products = [];
let vendors = [];

// 🔥 LOAD DATA
async function loadData() {
    await loadProducts();
    await loadVendors();
    loadPOs();
}

async function loadProducts() {
    const res = await fetch(`${API}/products/`);
    products = await res.json();
    console.log("Products:", products);
}

async function loadVendors() {
    const res = await fetch(`${API}/vendors/`);
    vendors = await res.json();

    let vendorDropdown = document.getElementById("vendor");

    vendorDropdown.innerHTML = vendors.map(v =>
        `<option value="${v.id}">${v.name}</option>`
    ).join("");
}

// 🔥 LOAD POs
async function loadPOs() {
    const res = await fetch(`${API}/po/`);
    const data = await res.json();

    let table = document.getElementById("poTable");

    table.innerHTML = data.map(po => `
        <tr>
            <td>${po.id}</td>
            <td>${po.reference_no}</td>
            <td>${po.vendor_id}</td>
            <td>₹ ${po.total_amount}</td>
            <td><span class="badge bg-success">${po.status}</span></td>
        </tr>
    `).join("");
}

// 🔥 SHOW FORM
function showForm() {
    document.getElementById("poForm").classList.remove("d-none");
}

// 🔥 HIDE FORM
function hideForm() {
    document.getElementById("poForm").classList.add("d-none");
}

// 🔥 ADD PRODUCT ROW
function addRow() {

    if (products.length === 0) {
        alert("Products not loaded!");
        return;
    }

    let options = products.map(p =>
        `<option value="${p.id}">${p.name}</option>`
    ).join("");

    let row = `
    <div class="d-flex gap-2 mb-2 item-row">
        <select class="form-select product">
            ${options}
        </select>

        <input type="number" class="form-control qty" placeholder="Qty" min="1">

        <button class="btn btn-danger" onclick="removeRow(this)">X</button>
    </div>
    `;

    document.getElementById("items").innerHTML += row;
}

// 🔥 REMOVE ROW
function removeRow(btn) {
    btn.parentElement.remove();
}

// 🔥 SUBMIT PO (FIXED)
async function submitPO() {

    if (!TOKEN) {
        alert("Please login first!");
        return;
    }

    let items = [];

    document.querySelectorAll(".item-row").forEach(row => {
        let product = row.querySelector(".product").value;
        let qty = row.querySelector(".qty").value;

        if (product && qty && qty > 0) {
            items.push({
                product_id: parseInt(product),
                quantity: parseInt(qty)
            });
        }
    });

    if (items.length === 0) {
        alert("Add at least one product!");
        return;
    }

    let data = {
        reference_no: document.getElementById("ref").value,
        vendor_id: parseInt(document.getElementById("vendor").value),
        items: items
    };

    console.log("Sending:", data);

    const res = await fetch(`${API}/po/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${TOKEN}`
        },
        body: JSON.stringify(data)
    });

    if (!res.ok) {
        alert("Error ❌");
        return;
    }

    alert("PO Created ✅");

    document.getElementById("ref").value = "";
    document.getElementById("items").innerHTML = "";

    hideForm();
    loadPOs();
}

// 🚀 INIT
loadData();
