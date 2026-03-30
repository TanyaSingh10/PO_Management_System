# 🚀 Purchase Order Management System

A full-stack **ERP-style Purchase Order Management System** built with **FastAPI, PostgreSQL, and JavaScript**, featuring authentication and dynamic UI.

---

## 📌 Features

* 🔐 **Authentication**

  * Google OAuth Login
  * JWT-based secure APIs

* 📦 **Purchase Order Management**

  * Create Purchase Orders
  * Multiple products per order
  * Automatic total calculation (with tax)

* 🏢 **Vendor & Product Management**

  * Add and view vendors
  * Add and manage products

* 🎨 **Dynamic Frontend**

  * Interactive dashboard
  * Dynamic product rows
  * Real-time data updates

* 🤖 **AI Feature (Optional)**

  * Generate product descriptions

---

## 🏗️ Tech Stack

### Backend

* ⚡ FastAPI
* 🐘 PostgreSQL
* 🧠 SQLAlchemy
* 🔐 JWT Authentication

### Frontend

* 🌐 HTML, CSS, JavaScript
* 🎨 Bootstrap

---

## 📂 Project Structure

```
po-management-system/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── auth.py
│   ├── dependencies.py
│   └── routes/
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── styles.css
│
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```
git clone https://github.com/YOUR_USERNAME/po-management-system.git
cd po-management-system
```

---

### 2️⃣ Backend Setup

```
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 3️⃣ Run Backend

```
uvicorn main:app --reload --port 8001
```

👉 Open API docs:

```
http://127.0.0.1:8001/docs
```

---

### 4️⃣ Frontend Setup

```
cd frontend
python3 -m http.server 5500
```

👉 Open:

```
http://127.0.0.1:5500
```

---

## 🔐 Authentication Flow

1. User logs in via Google
2. Frontend receives Google JWT
3. Backend verifies token
4. Backend generates its own JWT
5. All API requests use:

```
Authorization: Bearer <token>
```

---

## 📊 API Endpoints

* `POST /login` → Manual login
* `POST /google-login` → Google OAuth
* `GET /vendors/`
* `POST /vendors/`
* `GET /products/`
* `POST /products/`
* `GET /po/`
* `POST /po/`

---

## 🧠 Future Enhancements

* ✏️ Edit / Delete Purchase Orders
* 📊 Dashboard analytics
* 📦 Inventory tracking
* ☁️ Deployment on AWS / Render
* 🤖 Real AI integration (OpenAI)

---

## Submitted by: Tanya Singh

---



