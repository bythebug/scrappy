# LinkedIn Email Scraper

A Python automation script that extracts email addresses from comments on any LinkedIn post and saves them to a CSV file.

## ✍️ Author

**Suraj Van Verma**  
Created: June 2025  
Contact: [suraj.verma@mail.mcgill.ca](mailto:suraj.verma@mail.mcgill.ca)  
Website: [bythebug.github.io](https://bythebug.github.io)

## 📌 Features

- 🔍 Extracts email addresses from public LinkedIn post comments
- 💬 Captures full comment text (with optional commenter name)
- ✅ Skips duplicates and plain email-only comments (optional)
- 🗂️ Auto-versioned output files (no overwriting)
- 🖥️ Uses your own Chrome session (no headless or login automation)

## ⚙️ Requirements

- macOS or Linux (tested)
- Python 3.8 or higher
- Google Chrome (installed)
- [ChromeDriver](https://chromedriver.chromium.org/downloads) (must match your Chrome version)

### 🔧 Install Python packages:

```bash
pip install selenium pandas
```

## 🚀 How to Use

1. **Clone or download** this repository.

2. **Update the post URL** in `linkedin_scraper.py`:

```python
POST_URL = 'https://www.linkedin.com/feed/update/urn:li:activity:YOUR_POST_ID/'
```

3. **Run the script:**

```bash
python3 linkedin_scraper.py
```

4. A Chrome window will open:
   - Log in to LinkedIn if needed
   - The script will scroll and extract all visible comments

## 📂 Output

You’ll get a CSV file like:

```
linkedin_emails_with_comments.csv
```

If that file already exists, it auto-generates:

```
linkedin_emails_with_comments_1.csv
linkedin_emails_with_comments_2.csv
```

### Output Columns:

| Author (optional) | Email             | Comment                          |
|-------------------|------------------|----------------------------------|
| Saurav Mehta      | saurav@xyz.com   | Please connect at saurav@...     |
| —                 | user@gmail.com   | user@gmail.com                   |

## 🛡️ Disclaimer

> This script is intended for personal use only.  
> Scraping LinkedIn at scale may violate their [Terms of Service](https://www.linkedin.com/legal/user-agreement).  
> Use responsibly and ethically.

## 🙌 Acknowledgements

- Built with ❤️ by Suraj Verma  
- Inspired by creators, mentors, and productivity tools  
- Connect on [LinkedIn](https://www.linkedin.com/in/bythebug)
