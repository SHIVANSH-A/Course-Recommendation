# 🔥 Course Recommendation System

A web-based application that suggests similar courses based on your selected input using a precomputed similarity matrix. Built with **Flask**, **Tailwind CSS**, and **Python**, this project provides an interactive frontend and intelligent backend to help users explore related learning content.

---

## 🚀 Features

- 🔍 Search and select from a list of courses
- 🎓 View top recommended courses
- 🌐 Direct links to course URLs
- 🖌️ Clean, responsive UI built with Tailwind CSS
- 🧠 Machine learning backend using cosine similarity

---

## 🛠️ Tech Stack

- **Frontend**: HTML, Tailwind CSS (CDN)
- **Backend**: Flask (Python)
- **Data**: Pandas, NumPy, Pickle (for similarity model)
- **Model**: Cosine similarity-based course recommendation

---

## 📁 Project Structure

```
📦 course-recommendation-app/
├── app.py                      # Main Flask app
├── templates/
│   └── index.html              # Frontend page
├── models/
│   ├── similarity.pkl          # Precomputed similarity matrix
│   ├── courses.pkl             # Course names and URLs
│   └── course_list.pkl         # Raw course list for datalist
└── static/                     # (optional) For custom styles/assets
```

---

## ⚙️ Setup Instructions

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/course-recommendation-app.git
   cd course-recommendation-app
   ```

2. **Install dependencies**:

   ```bash
   pip install flask pandas numpy
   ```

3. **Ensure model files exist** in the `models/` folder:

   - `similarity.pkl`
   - `courses.pkl`
   - `course_list.pkl`

4. **Run the Flask app**:

   ```bash
   python app.py
   ```

5. **Open in browser**:

   ```
   http://127.0.0.1:5000
   ```
