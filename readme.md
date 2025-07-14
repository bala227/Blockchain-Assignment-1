#  Blockchain Dashboard

A fully functional, beginner-friendly blockchain implementation built with Python and Flask, featuring a modern interactive dashboard using Tailwind CSS.

This project demonstrates core blockchain concepts like proof-of-work, decentralized node registration, transaction handling, and consensus resolution — all visualized beautifully through a responsive UI.

---

##  Features

-  Add & broadcast new transactions
-  Mine new blocks via Proof-of-Work
-  View the full blockchain in a clean UI
-  Register and manage peer nodes
-  Resolve chain conflicts using consensus algorithm
-  Tailwind-powered UI for real-time blockchain interaction

---

##  Tech Stack

- **Backend**: Python 3, Flask
- **Blockchain Logic**: Custom Python module (`blockchain.py`)
- **Frontend**: HTML, Tailwind CSS, JavaScript
- **Peer-to-peer**: RESTful API + Flask server

---

##  Getting Started

###  Prerequisites

- Python 3.7+
- `pip` package manager

###  Clone the Repository

```bash
git clone https://github.com/your-username/blockchain-dashboard.git
cd blockchain-dashboard
```

###  Install Dependencies
```bash
pip install flask requests

python app.py -p 5000
python app.py -p 5001
python app.py -p 5002

Then open in your browser:

http://localhost:5001

Register Nodes

curl -X POST -H "Content-Type: application/json" \
  -d '{"nodes":["http://127.0.0.1:5000", "http://127.0.0.1:5002"]}' \
  http://127.0.0.1:5001/nodes/register
