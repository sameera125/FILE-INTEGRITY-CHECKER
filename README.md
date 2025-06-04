
# 🔐 File Integrity Checker  
**Internship Task - 1**  
**Company:** CODTECH  

## 🧾 Description  
This tool monitors file changes in a folder by calculating and comparing their hash values using Python’s `hashlib` library. It helps detect any modifications, deletions, or newly added files — ensuring file integrity.

## 🚀 Features
- Calculates SHA-256 hashes for each file
- Saves and loads hash data from `hashes.json`
- Detects:
  - Modified files
  - Deleted files
  - New files

## 🛠️ Requirements
- Python 3.x

## 📂 Usage Instructions

### ✅ Step 1: Generate Hashes
Run this to save the current state of files:

```bash
python file_integrity_checker.py "C:\Path\To\Your\Folder" --generate
```

This creates a `hashes.json` file storing all file hashes.

### 🔍 Step 2: Verify Integrity
After any changes in files, run:

```bash
python file_integrity_checker.py "C:\Path\To\Your\Folder" --verify
```

This will compare current files against the stored hashes and show:
- `[OK]` – File unchanged
- `[MODIFIED]` – File was edited
- `[MISSING]` – File was deleted
- `[NEW]` – New file detected

## 📁 Files Included in Submission
- `file_integrity_checker.py` – Main Python script
- `README.md` – This file
- *(Optional)* `hashes.json` – Example hash record file (auto-generated)

## 🧑‍💻 Developed by
sk sameera 
For CODTECH Internship – Task 1
