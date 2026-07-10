# 🧠 SmartAttend — Intelligent AI Attendance System

SmartAttend is a **multi-modal AI-powered attendance system** that leverages **face recognition and voice biometrics** to provide secure, accurate, and scalable attendance tracking. Designed to eliminate proxy attendance and manual errors, it integrates modern AI pipelines with a clean, role-based dashboard.

---

## 🚀 Features

### 🔍 Multi-Modal Biometric Verification

* **Face Recognition** using `dlib` and `face_recognition`
* **Voice Identification** using `Librosa` and `Resemblyzer`
* Dual verification significantly reduces spoofing and proxy attendance

### 🔐 Secure Authentication

* Password hashing with `bcrypt`
* Role-based access control:

  * 👩‍🏫 Teacher Dashboard
  * 🎓 Student Dashboard

### 📊 Smart Dashboards

* Attendance insights and tracking
* Subject-wise attendance management
* Real-time updates

### 📷 QR-Based Robust Attendance

* QR-driven session validation for added robustness
* Prevents unauthorized attendance marking

### ☁️ Cloud-Backed Data Storage

* Integrated with **Supabase** for scalable and secure data handling

---

## 🏗️ System Architecture

```
User (Student/Teacher)
        ↓
   Streamlit UI
        ↓
 Authentication Layer (bcrypt)
        ↓
Biometric Verification Layer
 (Face + Voice Models)
        ↓
   Attendance Engine
        ↓
   Supabase Database
```

---

## 🛠️ Tech Stack

| Category     | Technologies                                 |
| ------------ | -------------------------------------------- |
| **Frontend** | Streamlit                                    |
| **Backend**  | Python                                       |
| **AI/ML**    | dlib, face_recognition, Librosa, Resemblyzer |
| **Database** | Supabase                                     |
| **Security** | bcrypt                                       |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/PranjliAgg/SmartAttend.git
cd SmartAttend
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a `.env` file and add:

```
SUPABASE_URL=your_url
SUPABASE_KEY=your_key
```

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 🧪 How It Works

1. User logs in (Student/Teacher)
2. System verifies identity via:

   * Face recognition
   * Voice matching
3. QR session validation ensures legitimacy
4. Attendance is recorded securely in the database
5. Dashboards reflect real-time updates

---

## 📈 Key Highlights

* 🎯 **High Accuracy** using multi-modal biometrics
* 🔒 **Secure & Tamper-Resistant**
* ⚡ **Real-Time Processing**
* 📊 **Scalable Cloud Integration**
* 🧩 **Modular Architecture**

---

## 🚧 Future Improvements

* Liveness detection for anti-spoofing
* Mobile app integration
* Offline attendance sync
* Advanced analytics & reporting
* Facial recognition optimization for low-light environments

## ⭐ Show Your Support

If you like this project, consider giving it a ⭐ on GitHub!
