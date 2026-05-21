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

* **Backend:**  
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="50"/>
  &nbsp;&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain-wordmark.svg" width="50"/>

* **Database:**  
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original-wordmark.svg" width="50"/>

---

### 🖥️ Terminal Output

![API Terminal Output](model-serialization.png)

---

## 📁 Project Structure

testapp/
  ├── models.py
  ├── views.py (CBV CRUD API)
  ├── serializers.py
  ├── tests.py (API test client)

---

## ⚠️ Important Notes
- API expects JSON input  
- CSRF is disabled for testing purposes  
- ID must exist for update and delete operations


## 📚 Learning Outcomes

- Django REST Framework basics  
- Class-Based API Views (CBV)  
- JSON parsing and rendering in APIs  
- API testing using Python `requests` library  
- Understanding CRUD architecture in REST APIs  


---
## 👨‍💻 Author

**Sajjad Ali**


## 🤝 Connect with Me

Agar aapke paas koi sawal hai ya aap connect karna chahte hain, toh aap mujhe niche diye gaye platforms par reach out kar sakte hain: <br>
<i>If you have any questions or would like to connect, feel free to reach out to me on the platforms below:"</i>

* **LinkedIn:**  
  <a href="https://www.linkedin.com/in/sajjadali-fullstack/" target="_blank">
    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linkedin/linkedin-original.svg" width="50" alt="LinkedIn"/>
  </a>

* **Gmail:**  
  <a href="mailto:sajjadali.dev01@gmail.com">
    <img src="https://raw.githubusercontent.com/tandpfun/skill-icons/main/icons/Gmail-Light.svg" width="50" alt="Gmail"/>
  </a>

---

## 💖 Support & Usage
If you find this project helpful or plan to use it as a template for your learning, please consider:
1. Giving it a **Star ⭐**
2. Giving credit to the original author means me Your Sajju 🔥✨

---

## 🧪 Run Test Client
  \modelSerilizer\testapp> py tests.py

