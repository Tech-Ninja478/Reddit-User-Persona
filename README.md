# 🧠 Reddit User Persona Generator

This tool generates a detailed user persona based on a Reddit user's activity by:

🔹 Scraping their posts and comments  
🔹 Analyzing content using Google's Gemini API  
🔹 Structuring the results into a readable persona profile  
🔹 Exporting the final persona as both `.txt` and styled `.pdf`

---

## ⚙️ Features

✅ Reddit profile scraping (posts + comments)  
✅ Gemini-powered persona generation  
✅ Inline content citations for each insight  
✅ Unicode-safe, well-formatted PDF output  
✅ Works in virtual environments, with `.env` support

---

## 🔧 Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/reddit-persona-generator.git
   cd reddit-persona-generator

2. python -m venv venv
venv\Scripts\activate  # Windows

3. pip install -r requirements.txt

4.Create a .env file:
GEMINI_API_KEY=
REDDIT_CLIENT_ID=
REDDIT_CLIENT_SECRET=
REDDIT_USER_AGENT=
   
