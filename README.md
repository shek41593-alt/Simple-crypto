# 💰 Simple-crypto

A minimal cryptocurrency implementation in Python that demonstrates core blockchain concepts such as wallet generation, transactions, block creation, and proof-of-work mining.

---

## 🚀 Overview

This project is a lightweight simulation of a cryptocurrency system. It models how digital coins are transferred between users and how transactions are recorded securely in a blockchain.

The system includes wallet creation, transaction validation, mining, and balance updates — all implemented in a single Python file for simplicity and clarity.

---

## ⚙️ Features

* 🔐 Wallet generation using hashed private keys
* 💸 Transaction creation and validation
* 📥 Pending transaction pool
* ⛏️ Proof-of-Work mining (nonce-based)
* 🔗 Blockchain with hash-linked blocks
* 📊 Real-time balance tracking

---

## 🧠 How It Works

1. Users create wallets (Alice and Bob)
2. Each wallet is initialized with coins
3. A transaction is created (Alice → Bob)
4. Transaction is stored in a pending list
5. Mining validates transactions and creates a block
6. Block is added to the blockchain
7. Balances are updated accordingly

---

## 🏗️ Architecture

```text
Wallet → Transaction → Pending Pool → Mining → Block → Blockchain → Balance Update
```

---

## 📁 Project Structure

```text
Simple-crypto/
│── simple_cryptocurrency.py
```

---

## 🖥️ Requirements

* Python 3.x
* No external libraries required

---

## ▶️ How to Run

```bash
git clone https://github.com/shek41593-alt/Simple-crypto.git
cd Simple-crypto
python3 simple_cryptocurrency.py
```

---

## 🧪 Example Output

```text
Alice: <address> Balance: 100
Bob: <address> Balance: 100

Transaction: Alice sends 25 coins to Bob

Block mined successfully

Alice Balance: 75
Bob Balance: 125
```

---

## ✅ Advantages

* Simple and beginner-friendly
* Demonstrates real blockchain workflow
* No dependencies required
* Easy to extend

---

## ⚠️ Limitations

* No digital signatures (not secure)
* No peer-to-peer networking
* No persistent storage
* Not suitable for production

---

## 🔮 Future Scope

* Add Flask-based web interface
* Implement public/private key cryptography
* Build peer-to-peer network
* Add database support
* Introduce mining rewards

---

## 👨‍💻 Author

Abhishek K

---

## 📄 License

This project is for educational purposes only.
