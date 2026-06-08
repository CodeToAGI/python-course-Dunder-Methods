# CodeToAGI — Episode 15: OOP Part 2

## 🎯 Dunder Methods, Properties, Class Methods & Static Methods

## 📺 Episode Overview

Most Python beginners write classes that print ugly output like "Product object at memory address", can't be compared with ==, and have no readable string representation.

**In Episode 15, you'll learn how to fix ALL of these problems.**

### What You Will Learn

| # | Technique | What It Does |
|---|-----------|---------------|
| 1 | `__str__` | Controls what print() shows (user-friendly output) |
| 2 | `__repr__` | Developer version shown in terminal |
| 3 | `__eq__` | Makes == work correctly on your objects |
| 4 | `__lt__` | Enables sorting with < and sorted() |
| 5 | `__len__` | Makes len() work on custom objects |
| 6 | `@property` | Smart attributes with getter and setter |
| 7 | `@classmethod` | Alternative constructors like datetime.fromisoformat |
| 8 | `@staticmethod` | Utility functions in class namespace |

### Mini Project

**Smart Product Catalog** - A professional class using all 8 features

---

## 🏆 Your Challenge: Smart Temperature Class

Build a Temperature class with these requirements:

```python
# Step 1 - Store temperature internally in Celsius
# Step 2 - @property fahrenheit that converts on the fly
# Step 3 - @property kelvin that converts on the fly
# Step 4 - __str__ returns formatted string like "25°C"
# Step 5 - __eq__ compares two temperatures by Celsius value
# Step 6 - @classmethod from_fahrenheit to create from Fahrenheit
# Step 7 - @staticmethod is_freezing returns True if Celsius <= 0
