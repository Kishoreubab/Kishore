# 🧪 Saucedemo Automation Testing Suite

This repository contains an automated test suite for [Saucedemo](https://www.saucedemo.com), a sample e-commerce web application used for testing. The automation is built using **Selenium** and **Pytest**, following the Page Object Model (POM) structure.

---

## 📁 Project Structure

```
saucedemo-automation/
│
├── tests/                  # Test scripts grouped by feature
│   ├── test_login.py
│   ├── test_add_to_cart.py
│   └── test_checkout.py
│
├── pages/                  # Page Object Models for each screen
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── conftest.py             # Pytest fixtures and setup
├── requirements.txt        # Python package dependencies
```

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.7+
- Mozilla Firefox browser
- GeckoDriver (ensure it matches your Firefox version and is in your PATH)

---

### 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Kishoreubab/Kishore/tree/main/saucedemo_automatin  
   cd saucedemo_automatin
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   > Only `selenium` and `pytest` are required for this project.

---

## 🧪 Running Tests

To run all tests:
```bash
pytest
```

To run a specific test file:
```bash
pytest tests/test_login.py
```

To view detailed output:
```bash
pytest -v
```

---

## 📄 Author

**Kishore Babu**  
[Your GitHub Profile](https://github.com/Kishoreubab)

---

## 📌 Notes

- Make sure your GeckoDriver is installed and compatible with your version of Firefox.
- The test scripts are written using basic locators and assertions tailored for Saucedemo UI.

---

## ✅ Sample Test Scenarios

- Login with valid and invalid credentials
- Add products to cart and verify cart contents
- Complete checkout process with valid data

---

## License

This project is for educational/demo purposes only.
