# Task Automation With Python Scripts

A collection of simple yet powerful Python scripts developed as part of my **Python Programming Internship at Code Alpha**.  
Each script performs a specific automation or data extraction task — from handling images to scraping web data.

---

## 📁 Repository Contents

### 1. jpeg_extractor.py
Moves all `.jpg` and `.jpeg` files from a source folder to a destination folder.

#### 🔹 Features:
- Automatically creates the destination folder if it doesn’t exist.
- Moves all `.jpg` or `.jpeg` files (case-insensitive).
- Displays the number of files moved.

#### Input:

- Source folder path
- Destination folder path

#### Example:

Source folder: C:\Users\Arya\Downloads
Destination folder: C:\Users\Arya\Pictures\JPGs

### 2. email_extractor.py
Extracts all valid email addresses from a `.txt` file and saves them into a new file.

#### 🔹 Features:

- Uses Regular Expressions to find emails.
- Automatically removes duplicate email addresses.
- Saves extracted emails in emails_output.txt.

#### Input:

Path to the `.txt` file containing text or data.

#### Output:

- A file named emails_output.txt containing one email per line.

### 3. title_scraper.py
Fetches the title of any given website and saves it to a text file.

🔹 Features:

- Uses requests and BeautifulSoup for web scraping.
- Automatically extracts and saves the <title> tag text.
- Handles missing or invalid titles gracefully.

#### Input:

Website URL (e.g., https://example.com)

#### Output:

A file named `title.txt` containing the website title.

---

### ⚙️ Requirements

- Make sure you have Python installed (version 3.7 or above).
- Install dependencies with:
```
pip install requests beautifulsoup4
```

---

### 🧠 Learning Outcome

This mini-project collection helped me:
- Practice file handling and regex in Python.
- Work with external libraries (requests, BeautifulSoup).
- Build small automation tools with practical real-world uses.

---

### 👨‍💻 Author

Arya Madiwale
📍 Computer Engineering Student | AI & ML Enthusiast
🧩 Developed during Code Alpha Python Internship
