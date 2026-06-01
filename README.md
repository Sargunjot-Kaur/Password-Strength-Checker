# 🔐 Password Strength Checker

A Python command-line tool that evaluates the strength of a password based on length and complexity criteria.

---

## 📌 About

Built as a practical Python project to apply modular programming concepts. The tool analyses a user-entered password and provides specific feedback on what security criteria it meets or is missing.

---

## ⚙️ How It Works

The project is split across two files:

- **`checker.py`** — contains the validation logic as reusable functions
- **`main.py`** — handles user input and calls the checker functions

### Validation Criteria

| Check | Requirement |
|---|---|
| Length | Minimum 12 characters |
| Lowercase | At least one lowercase letter |
| Uppercase | At least one uppercase letter |
| Number | At least one digit |
| Symbol | At least one symbol from `!@#$%^&*_-/?~` |

If a criterion is met, the function returns `"Checked"`. If not, it returns a message specifying exactly what's missing.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x

### Run the project

```bash
git clone https://github.com/Sargunjot-Kaur/Password-Strength-Checker.git
cd Password-Strength-Checker
python main.py
```

### Example Output

```
Enter your password: hello
Length: Oops! Too short.
Missing: Upper case, number, a symbol
```

```
Enter your password: HelloWorld@99
Checked
Checked
```

---

## 📁 Project Structure

```
Password-Strength-Checker/
│
├── main.py        # Entry point — takes user input, calls checker functions
└── checker.py     # Core logic — check_length() and check_complexity()
```

---

## 🛠️ Built With

- Python 3
- Standard library only (no external dependencies)

---

## 👩‍💻 Author

**Sargunjot Kaur**  
BEng Software Engineering — GISMA University of Applied Sciences, Berlin  
[GitHub](https://github.com/Sargunjot-Kaur)
