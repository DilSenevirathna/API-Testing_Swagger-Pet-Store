
🐾 Swagger PetStore API Automation Project

https://github.com/user-attachments/assets/c30713cc-45c4-4bc7-aff9-8e656223939b



A modular, scalable API testing framework built with Python + pytest

📘 Overview

This project is a fully structured API automation framework created using the Swagger PetStore API.
It demonstrates clean architecture, reusable components, and maintainable test design — suitable for both learning and real-world QA workflows.

The main goals of this project are to:

Build an automation-ready API client

Implement organized test suites (Pet, Store, User)

Showcase scalable, maintainable automation practices

Provide a clean template for future REST API projects

🏗️ Architecture

Below is the high-level architecture diagram used in this framework:

(Place the image in your repo root for the link to work.)

📁 Folder Structure
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

⚙️ Tech Stack

Python 3.x

pytest

Requests library

JSON schemas (optional)

Swagger PetStore API

🚀 Features

✔️ Modular Base API Client
✔️ Wrapper clients for endpoint groups
✔️ Reusable headers, configuration, and validators
✔️ Organized test structure by domain
✔️ Positive + Negative test coverage
✔️ Terminal-friendly pytest execution
✔️ Easy extension for future endpoints

🧪 Tests Implemented
🐶 Pet Endpoints

Add new pet

Update pet

Get pet by ID

Find pets by status

Delete pet

Negative tests (invalid IDs, malformed payloads)

🏬 Store Endpoints

Place order

Get order

Delete order

Get store inventory

Error validation scenarios

👤 User Endpoints

Create user

Get user

Login / logout

Update and delete user

Invalid credentials testing

▶️ Running the Project
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run all tests
pytest -v

3️⃣ Run tests with HTML report (optional)
pytest --html=report.html

🎯 Key Objectives

Promote clean, maintainable automation patterns

Demonstrate real-world API testing practices

Provide a learning foundation for QA engineers

Build a framework that can grow with project needs

💡 QA Inspiration

“There’s a special kind of ASMR in watching clean green test logs flow in the terminal.”

Because for QA engineers —
Quality isn’t just measured. It’s felt.

🌱 Future Enhancements

Add environment-based config switching

Add CI/CD pipeline integration

Add Allure or pytest-html reporting

Data-driven testing using JSON/YAML

Add mock server integration

🤝 Contributions

Contributions, improvements, and suggestions are welcome!
Feel free to open issues or submit pull requests.
