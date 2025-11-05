# Paylocity UI Framework (Behave + Selenium)

📖 Overview
This project is a UI automation framework built with Python, Selenium, and Behave (BDD).
It automates CRUD operations (Add, Edit, Delete) for employee management on the Paylocity Benefits Dashboard, validating both UI interactions and benefits cost calculations.

🗂️ Project Structure
paylocity-ui-framework/
│
├── config/                # Configuration files (browser, environment, etc.)
├── features/              # Gherkin feature files and step definitions
│   ├── steps/             # Step definition implementations
│   └── employee.feature   # Example feature: Add/Edit/Delete employees
├── pages/                 # Page Object Model classes
├── utils/                 # Utility functions (assertions, data parsing, helpers)
├── behave.ini             # Behave configuration
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation



⚙️ Setup Instructions
1. Clone the repository
git clone https://github.com/justfer11/paylocity-ui-framework.git
cd paylocity-ui-framework


2. Create and activate a virtual environment
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate


3. Install dependencies
pip install -r requirements.txt


4. Configure environment
- Copy .env and update values if needed (e.g., credentials, base URL).
- Adjust behave.ini or config/ files for browser settings.

▶️ Running Tests
Run all scenarios
behave


Run with pretty output
behave -f pretty


Run a specific feature
behave features/employee.feature


Run tagged scenarios
behave -t @delete



✅ Example Scenarios
- Add Employee: Creates a new employee and validates benefits cost.
- Edit Employee: Updates employee details and recalculates benefits.
- Delete Employee: Removes an employee and verifies the row disappears.
- Scenario Outlines: Run the same flow with multiple employees.

🔧 Utilities
- Assertions: utils/assertions.py provides assert_true, assert_number_close.
- Data parsing: utils/data.py handles currency parsing and formatting.
- Page Objects: Encapsulate locators and actions for maintainability.

🚀 Roadmap
- Add CI/CD integration (GitHub Actions).
- Generate HTML/Allure reports.
- Expand coverage for edge cases (invalid inputs, large datasets).
- Cross‑browser testing.

🤝 Contributing
- Fork the repo
- Create a feature branch (git checkout -b feature/my-feature)
- Commit changes (git commit -m "Add new feature")
- Push branch (git push origin feature/my-feature)
- Open a Pull Request
