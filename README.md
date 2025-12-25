# 🤖 Gemini AI ChatBot

An interactive **AI-powered chatbot** built using **Google Gemini API** and **Streamlit**.
This project allows users to chat with Google’s Gemini model through a clean and responsive web interface.

---

## 🚀 Features

* 💬 Real-time chat with Google Gemini AI
* 🧠 Context-aware responses using session history
* 🎨 Clean UI using Streamlit theme configuration
* 🔐 Secure API key handling using `.env` file
* ⚡ Lightweight and easy to run locally

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Google Gemini API**
* **python-dotenv**

---

## 📁 Project Structure

```
GeminiAI_ChatBot/
│
├── app.py
├── requirements.txt
├── .env
├── .streamlit/
│   └── config.toml
└── README.md
```

---

## 🔑 Prerequisites

* Python 3.9 or higher
* A Google Gemini API key

👉 Get your API key from:
[https://ai.google.dev/](https://ai.google.dev/)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/srinidhi-2006-bit/GeminiAI_ChatBot.git
cd Gemini_ChatBot
```

---

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Create `.env` File

In the project root, create a file named `.env` and add:

```env
GEMINI_API_KEY=your_api_key_here
---

### 5️⃣ Streamlit Theme Configuration (Optional)

Create a folder `.streamlit` and inside it create `config.toml`:

```toml
[theme]
primaryColor = "#4F46E5"
backgroundColor = "#0E1117"
secondaryBackgroundColor = "#262730"
textColor = "#FAFAFA"
font = "sans serif"
```

---

### 6️⃣ Run the Application

```bash
streamlit run app.py
```

Open in browser:
👉 [http://localhost:8501](http://localhost:8501)

---

## 🧪 Sample Usage

* Type a greeting like **“Hi”**
* Ask questions like:

  * *What is Artificial Intelligence?*
  * *Explain machine learning in simple terms*
  * *What are the latest AI trends?*

---

## ⚠️ API Quota & Billing Note

If you encounter an error like:

```
RESOURCE_EXHAUSTED (429)
```

It means:

* You have reached the **free-tier quota limit**
* Please wait and retry, or
* Enable billing in Google AI Studio for higher usage limits

🔗 More info:
[https://ai.google.dev/gemini-api/docs/rate-limits](https://ai.google.dev/gemini-api/docs/rate-limits)

---

