# 🛠️ Django Signals & Python Custom Class Assignment

This repository contains solutions to the assignment on **Django Signals** and **Custom Classes in Python**, as per the given problem statement.

---

## 🔍 Problem Statement

### 1. Django Signals

#### Question 1:
**Are Django signals executed synchronously or asynchronously by default?**  
✅ **Answer:** Django signals are executed **synchronously** by default.  
📁 **Code File:** `signals_sync_demo.py`

#### Question 2:
**Do Django signals run in the same thread as the caller?**  
✅ **Answer:** Yes, by default they run in the **same thread**.  
📁 **Code File:** `signals_thread_demo.py`

#### Question 3:
**Do Django signals run in the same database transaction as the caller?**  
✅ **Answer:** Yes, Django signals execute in the **same DB transaction** by default.  
📁 **Code File:** `signals_transaction_demo.py`

---

### 2. Python Custom Class: Rectangle

A custom `Rectangle` class is implemented with the following features:
- Accepts `length` and `width` on initialization
- Can be iterated
- Returns:
  - First: `{"length": value}`
  - Then: `{"width": value}`

📁 **Code File:** `rectangle.py`

#### Example Output:
```python
{'length': 10}
{'width': 5}


✅ Submission Note

This assignment was completed as per the provided instructions.
All three Django signal questions are supported by code files and verified logic.
The Rectangle class supports iteration with required output format.

⸻

👤 Submitted By
	•	Name: Nitish
	•	Month/Year: April 2025
