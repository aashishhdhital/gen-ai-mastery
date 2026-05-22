# 🧮 Project 2: Simple Calculator

## 📌 Overview
A command-line calculator that performs basic arithmetic operations (add, subtract, multiply, divide).

## 🎯 Learning Objectives
- ✅ Functions and function parameters
- ✅ User input handling
- ✅ Error handling (try-except)
- ✅ Data types and operations
- ✅ Control flow (if-else)
- ✅ String formatting

## 📂 Project Structure
```
02-calculator/
├── main.py          # Main calculator program
├── calculator.py    # Calculator functions
└── README.md        # This file
```

## 🚀 How to Run

### Step 1: Navigate to the project
```bash
cd 02-calculator
```

### Step 2: Run the program
```bash
python main.py
```

### Step 3: Use the calculator
```
Welcome to Simple Calculator!
================================
Enter first number: 10
Enter an operator (+, -, *, /): +
Enter second number: 5

10 + 5 = 15
```

## 💡 Code Explanation

### Key Concepts

1. **Functions**: Encapsulate logic for reusability
   ```python
   def add(a, b):
       return a + b
   ```

2. **User Input**: Get data from the user
   ```python
   number = float(input("Enter a number: "))
   ```

3. **Error Handling**: Handle invalid inputs gracefully
   ```python
   try:
       result = divide(a, b)
   except ZeroDivisionError:
       print("Cannot divide by zero!")
   ```

4. **String Formatting**: Display results nicely
   ```python
   print(f"{a} + {b} = {result}")
   ```

## 🎓 Practice Challenges

### Level 1 (Easy)
- [ ] Add a square root function
- [ ] Add a power function (x^y)
- [ ] Add memory feature (store last result)

### Level 2 (Medium)
- [ ] Create a calculator class
- [ ] Add percentage calculations
- [ ] Add calculation history

### Level 3 (Hard)
- [ ] Save calculation history to a file
- [ ] Create a GUI version using tkinter
- [ ] Support multiple operations in one line (e.g., 5 + 3 * 2)

## 📚 Key Takeaways

✨ **What You'll Learn:**
- How to structure code with functions
- How to validate user input
- How to handle errors gracefully
- How to build a practical application

---

**Next Project**: Move to File Organizer!
