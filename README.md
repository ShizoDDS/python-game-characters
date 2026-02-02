# 🗡️ python-game-characters

A small console-based Python project that demonstrates **Object-Oriented Programming (OOP)** concepts, including **abstract base classes**, **inheritance**, **polymorphism**, and simple **turn-based combat logic**.

The project simulates a battle between a hero and an enemy with random events such as critical hits, healing, and magical attacks.

---

## 🚀 Features

* Abstract base class for characters (`CharacterBase`)
* Base character implementation (`Character`)
* Role separation:

  * `Hero` — character with healing ability
  * `Enemy` — basic enemy class
* Hero specializations:

  * 🗡️ **Warrior** — critical hit chance (x2 damage)
  * 🔥 **Mage** — enhanced magic attack
* Turn-based battle loop
* Random events using the `random` module
* Delays between turns using `time.sleep`
* Clean and readable console output

---

## 🧠 Python Concepts Used

* Object-Oriented Programming (OOP)
* `abc.ABC` and `@abstractmethod`
* Inheritance and method overriding
* Polymorphism
* `super()` usage
* Modules: `random`, `time`

---

## 🧩 Project Structure

* `CharacterBase` — abstract interface for all characters
* `Character` — base implementation
* `Hero` — base class for playable characters
* `Enemy` — enemy implementation
* `Warrior` — hero with critical damage mechanic
* `Mage` — hero with magic damage bonus
* Main battle loop

---

## ▶️ How to Run

1. Make sure Python **3.8+** is installed
2. Save the file as `game.py`
3. Run the script:

```bash
python game.py
```

---

## 🕹️ Gameplay Overview

* The hero and the enemy attack each other in turns
* Critical hits may occur randomly
* The hero can heal when health is low
* The battle ends when one character's health reaches zero

---

## 🎯 Project Purpose

This project was created to:

* Practice **clean OOP architecture** in Python
* Demonstrate junior-level backend / logic skills
* Serve as a **portfolio project** for freelance platforms

---

## 🔮 Possible Improvements

* Add more character classes
* Implement experience and leveling system
* Add inventory and items
* Allow player choice for actions
* Convert the project to GUI or API-based version

---

## 👨‍💻 Author

Junior Python Developer

This project is for educational and portfolio purposes.

