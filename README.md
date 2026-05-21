#  Django DRF Employee CRUD API (CBV)

This project is a simple **Employee Management REST API** built using **Django REST Framework (DRF)** with **Class-Based Views (CBV)**.

It demonstrates full CRUD operations using JSON-based requests and a separate Python test client using the `requests` library.

---

##  Features

- Create Employee (POST)
- Fetch Employee / All Employees (GET)
- Full Update (PUT)
- Partial Update (PATCH)
- Delete Employee (DELETE)
- JSON based API communication
- Custom test client using Python `requests`

---

##  Tech Stack

- Python 3.x
- Django
- Django REST Framework
- SQLite (default DB)
- Requests Library (for testing API)

---

## 📁 Project Structure

testapp/
├── models.py
├── views.py (CBV CRUD API)
├── serializers.py
├── tests.py (API test client)

---

## 🧪 Run Test Client
 >>> \modelSerilizer\testapp> py tests.py

## ⚠️ Important Notes
  API expects JSON input
  CSRF is disabled for testing purposes
  ID must exist for update/delete operations

## 📚 Learning Outcomes

- Django REST Framework basics  
- Class-Based API Views (CBV)  
- JSON parsing and rendering in APIs  
- API testing using Python `requests` library  
- Understanding CRUD architecture in REST APIs  
