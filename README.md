Bank App API
A full-featured Django REST Framework-based backend API for a banking application. This app allows customers to register, manage their bank accounts, make transactions, and view bank statements. Admins and bank staff can also manage customer data, approve accounts, and monitor transactions.

Features
- Customer
- Register and Login
- Update profile
- Deposit & Withdraw funds
- Transfer money to other customers
- Pay utility bills
- Purchase airtime
- View bank statements
- View transaction history

Admin
- Register and Login
- Update admin profile
- View all admins
- View single admin profile

Bank Staff
- Add new staff to system
- View all bank staff
- View single bank staff profile

Account Management
- View all customers
- View single customer details
- View all transactions
- View single transaction

Tech Stack
- Backend Framework: Django, Django REST Framework
- Database: Default (SQLite) – can be swapped for PostgreSQL/MySQL
- Authentication: Basic DRF serializers (JWT/Auth to be added)
- Serialization: DRF Serializers
- Random Account Number Generator: Python random module
