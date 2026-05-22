# 📂 Project 1: File Organizer

## 📌 Overview
Automatically organize files in a directory by creating subdirectories for different file types (images, documents, videos, audio, etc.) and moving files accordingly.

## 🎯 Learning Objectives
- ✅ Working with file system (os module)
- ✅ Loops and conditionals
- ✅ String operations (file extensions)
- ✅ Dictionary data structures
- ✅ Error handling
- ✅ File operations (move/copy)

## 📂 Project Structure
```
01-file-organizer/
├── main.py          # Main file organizer program
├── organizer.py     # Core functions
└── README.md        # This file
```

## 🚀 How to Run

### Step 1: Create a test directory with files
```bash
mkdir test_files
cd test_files

# Create some test files
touch image1.jpg image2.png document.pdf video.mp4 music.mp3 code.py
```

### Step 2: Run the organizer
```bash
cd ../01-file-organizer
python main.py
```

### Step 3: Follow the prompts
```
Enter the directory path to organize: ../test_files
Organizing files in: ../test_files

✅ Created folder: Images
✅ Moved image1.jpg to Images/
✅ Moved image2.png to Images/
...

🎉 File organization complete!
```

## 💡 Code Explanation

### Key Concepts

1. **os Module**: Interact with the operating system
   ```python
   import os
   files = os.listdir(directory)
   ```

2. **Dictionary**: Map file extensions to categories
   ```python
   file_types = {
       'Images': ['.jpg', '.png', '.gif'],
       'Documents': ['.pdf', '.docx', '.txt'],
       'Videos': ['.mp4', '.avi']
   }
   ```

3. **Loops**: Iterate through files
   ```python
   for file in files:
       if os.path.isfile(file):
           # Process file
   ```

4. **String Operations**: Extract file extensions
   ```python
   name, ext = os.path.splitext(filename)
   ```

5. **Error Handling**: Handle file operations safely
   ```python
   try:
       shutil.move(source, destination)
   except Exception as e:
       print(f"Error: {e}")
   ```

## 🎓 Practice Challenges

### Level 1 (Easy)
- [ ] Only display files (don't move them)
- [ ] Show count of each file type
- [ ] Add more file type categories

### Level 2 (Medium)
- [ ] Organize by date (created, modified)
- [ ] Add undo functionality
- [ ] Create a log file of all operations

### Level 3 (Hard)
- [ ] Create a GUI using tkinter
- [ ] Add recursive folder organization
- [ ] Backup original files before organizing

## 📚 Key Takeaways

✨ **What You'll Learn:**
- How to interact with the file system
- How to work with dictionaries
- How to handle errors when working with files
- How to build practical automation tools

---

**Next Project**: Move to Web Scraper!
