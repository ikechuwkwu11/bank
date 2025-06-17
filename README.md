# 🏦 Bank App API
A full-featured backend banking system built with Django and Django REST Framework (DRF). This RESTful API provides comprehensive features for customers, admins, and bank staff to manage user profiles, perform transactions, and handle account operations in a secure and scalable way.

## ✨ Features
👤 Customer
- Register and log in
- Update profile information
- Deposit and withdraw funds
- Transfer money to other customers
- Pay utility bills
- Purchase airtime
- View transaction history
- Generate and download bank statements

## 🛠️ Admin
- Register and log in
- Update admin profile
- View all admins
- View individual admin profiles

👨‍💼 Bank Staff
- Add new staff members
- View all bank staff
- View individual staff profiles

📋 Account Management
- View all registered customers
- View details for a single customer
- View all transactions
- View specific transaction details

## 🧰 Tech Stack
| Layer             | Technology                                   |
| ----------------- | -------------------------------------------- |
| Backend Framework | Django, Django REST Framework                |
| Database          | SQLite (default, easily replaceable)         |
| Authentication    | Django sessions (JWT/Token support planned)  |
| Serialization     | DRF Serializers                              |
| Utilities         | Python's `random` module for account numbers |


## 🔐 Authentication
Currently uses Django session-based authentication via DRF. JWT or Token-based authentication can be added for production environments.

## 📁 Example API Endpoints
| Method | Endpoint                 | Description                           |
| ------ | ------------------------ | ------------------------------------- |
| POST   | `/api/register/`         | Customer registration                 |
| POST   | `/api/login/`            | Login (Customer/Admin/Staff)          |
| GET    | `/api/customers/`        | List all customers (admin/staff only) |
| POST   | `/api/deposit/`          | Deposit funds                         |
| POST   | `/api/withdraw/`         | Withdraw funds                        |
| POST   | `/api/transfer/`         | Transfer between accounts             |
| GET    | `/api/transactions/`     | View user's transaction history       |
| POST   | `/api/utility-payment/`  | Pay utility bills                     |
| POST   | `/api/airtime-purchase/` | Purchase airtime                      |


More endpoints available depending on role and permissions.

## 🧪 API Testing Tools
You can test the endpoints using:
- Postman
- cURL
- httpie

## 🛠️ Future Enhancements
✅ JWT Authentication (djangorestframework-simplejwt)
✅ Swagger/OpenAPI Documentation
✅ Role-Based Permissions (Admin, Staff, Customer)
✅ Email Notifications for Transactions
✅ Docker Support for Easy Deployment

