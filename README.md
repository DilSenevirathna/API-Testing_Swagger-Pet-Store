🐾 Swagger PetStore API Automation Framework

A Modular, Scalable API Testing Framework Built with Python + pytest

📘 Overview

This project is a fully structured API automation framework developed using the Swagger PetStore API.
It showcases clean architecture, reusable components, POM-style API clients, and maintainable test design — ideal for QA engineers building real-world API automation solutions.

The framework enables you to:

Automate Pet, Store & User endpoints

Validate request/response integrity

Run regression suites with confidence

Produce clean, readable test output

🏗️ Architecture
├── api_client
│   ├── base_client.py
│   ├── pet_client.py
│   ├── store_client.py
│   └── user_client.py
│
├── tests
│   ├── test_pet.py
│   ├── test_store.py
│   └── test_user.py
│
├── utils
│   ├── builders.py
│   └── validation.py
│
├── config
│   └── settings.py
│
├── requirements.txt
└── README.md

🔍 Sample Output (High-Quality Showcase)

These examples demonstrate the clarity, readability, and professionalism of the test execution output.

🧪 ✔️ Example: Successful Test Run
================================= Test Session Started =================================
Platform: Windows
Python: 3.11
Framework: pytest-8.2.0

Collected 15 tests

tests/test_pet.py::test_add_new_pet                    PASSED
tests/test_pet.py::test_get_pet_by_id                  PASSED
tests/test_pet.py::test_find_pets_by_status            PASSED

tests/test_store.py::test_place_order                  PASSED
tests/test_store.py::test_get_order                    PASSED

tests/test_user.py::test_create_user                   PASSED
tests/test_user.py::test_login_successful              PASSED
tests/test_user.py::test_delete_user                   PASSED

============================= 15 passed in 4.82s ========================================


✔ Clean
✔ Readable
✔ Professional
✔ Recruiter-Friendly

📝 Example API Request & Response

POST /pet – Add New Pet

Request:
{
  "id": 101,
  "name": "Snowy",
  "status": "available"
}

Response:
{
  "id": 101,
  "name": "Snowy",
  "photoUrls": [],
  "status": "available"
}


Validation:

Status code = 200

JSON schema validated

Response matches the sent payload

❌ Example Negative Test Output
tests/test_pet.py::test_get_pet_invalid_id
FAILED: 404 Not Found

Expected: Error message returned for invalid pet ID
Received:
{
  "code": 1,
  "type": "error",
  "message": "Pet not found"
}


This highlights failure clarity — extremely useful for debugging.

🚀 Features

✔️ Modular Base API Client
✔️ Domain-specific client wrappers
✔️ Shared request builders
✔️ Shared response validators
✔️ Positive + Negative tests
✔️ HTML report support
✔️ Easy CI/CD integration

🧪 Implemented Tests
🐶 Pet

Add new pet

Update pet

Get pet by ID

Find pets by status

Delete pet

Error validation (invalid IDs, bad payloads)

🏬 Store

Place order

Get order

Delete order

Get inventory

Invalid order scenarios

👤 User

Create user

Login/logout

Update/delete

Invalid credentials testing

▶️ Running the Project
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run all tests
pytest -v

3️⃣ Generate HTML report
pytest --html=report.html

🌟 Visual Quality Output

Below is what your testing report looks like in HTML:

✔ Summary Panel
✔ Execution Timeline
✔ Passed & Failed Test Badges
✔ Stacktrace (for failures)
✔ Screenshots Integration Ready (if needed)

🎯 Key Objectives

Promote real-world automation patterns

Provide a clean, scalable framework

Demonstrate professional QA engineering practices

Build confidence through structured regression testing

💡 QA Inspiration

“A clean test suite is like a clean mind — predictable, reliable, and deeply satisfying.”

🌱 Future Enhancements

Environment switching

CI/CD (GitHub Actions)

Allure reporting

Data-driven testing

Fake/mock server integration

🤝 Contributions

PRs and suggestions are welcome!
Let’s build better QA tools together. 🚀
