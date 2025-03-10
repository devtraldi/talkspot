# 🗣️ TalkSpot - Social Media Platform in Django

This project was developed as part of **Practical Assignment 2** for the **Web Programming (UpSkill - SAP/ABAP)** course.  
TalkSpot is a social media platform where users can **create posts, comment, and interact**.

## 📌 Main Features  
👉 User registration and login  
👉 Create, edit, and delete posts  
👉 Comment on posts (with editing and deletion)  
👉 Post feed ordered by date  
👉 Admin panel for managing users and content  
👉 Authentication and permission control  

---

## 📸 Screenshots  

### 🏠 Home Page  
![Home Page](screenshots/home.png)
![About](screenshots/about.png)
![quotesection](screenshots/quotesection.png)

### 🔒 Sign Up Page  
![Sign Up Page](screenshots/signup.png)

### 🏠 App Home Page  
![App Home Page](screenshots/app.png)

### 📝 Creating a Post  
![Create Post](screenshots/create_post.png)


---

## 🛠️ Technologies Used  
- **Django 5.1** (Web Framework)  
- **SQLite** (Database)  
- **Bootstrap 5** (Styling)  
- **Python 3.11**  

---

## 🚀 How to Run the Project Locally?  

1️⃣ Clone this repository:  
```sh
git clone https://github.com/YOUR_USERNAME/talkspot.git
cd talkspot
```

2️⃣ Create a virtual environment and install dependencies:  
```sh
python -m venv venv
source venv/bin/activate  # (Linux/Mac)
venv\Scripts\activate  # (Windows)

pip install -r requirements.txt
```

3️⃣ Apply migrations and start the server:  
```sh
python manage.py migrate
python manage.py runserver
```

4️⃣ Access the application in your browser:  
```
http://127.0.0.1:8000/
```

---

## 📌 Next Steps  
👉 Improve project security (XSS/CSRF protection)  
👉 Implement a REST API for external interactions  
👉 Enhance the user interface  

---

## 👥 Team  
👉 **Maya Dias**  
👉 **Rafael Oliveira**  
👉 **Rute Rodrigues**  

---

## 📝 License  
This project is for academic purposes only.

