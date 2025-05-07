# ATM System
This project implements a simple ATM system that includes inserting a card, verifying a PIN, selecting an account, and performing balance inquiries, deposits, and withdrawals.

## Structure
The project is organized with the following structure:
<pre><code>```text
atm/
├── utils/
│   ├── credit_card.py  # Card information data model
│   ├── card_checker.py  # Card validation
│   └── bank_account.py  # Bank account management
├── controller/
│   └── atm_controller.py  # ATM controller
├── test.py  # Unit tests
└── play_ground.py  # Simulation
```</code></pre>

## Getting Started
### Installation
1. Clone the repository
   ```bash
   git clone https://github.com/park-sangbeom/atm-controller.git

   
2. Install dependencies
   ```bash
   pip install pytest

### Test 
1. To run the unit test:
   ```bash 
   pytest atm/test.py -v
2. To see the basic operation of the system:
   ```bash 
   python atm/play_ground.py