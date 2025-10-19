# 🧭 Job Search App

A simple **Python command-line application** that loads job postings from a CSV file and lets you view or search them.

---

## ✨ Features
- 🔹 **View all job postings**
- 🔹 **View most recent jobs** (from the current year)
- 🔹 **Search jobs** by keyword and location

---

## ⚙️ How It Works
1. The program reads job data from `fake_jobs.csv`.
2. Each job is stored as a `Job_Class` object containing:
   - Job title  
   - Company name  
   - Location  
   - Date posted  
3. Users can choose from a simple text-based menu to browse or search jobs.

---

## ▶️ How to Run
1. Make sure `fake_jobs.csv` is in the same folder as `main.py`.
2. Run the program:
   ```bash
   python main.py
