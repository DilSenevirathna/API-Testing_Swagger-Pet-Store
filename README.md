# 🐾 Swagger PetStore API Automation Framework

A **Modular, Scalable API Testing Framework** Built with **Python + pytest**

---

📘 **Overview**

This project is a fully structured API automation framework built using the **Swagger PetStore API**.  
It demonstrates clean architecture, reusable components, and maintainable test design — suitable for both learning and real-world QA workflows.

The main goals of this project are to:

- Build an automation-ready API client  
- Implement organized test suites (**Pet**, **Store**, **User**)  
- Showcase scalable, maintainable automation practices  
- Provide a clean template for future REST API projects  

---

⚙️ **Tech Stack**

- Python 3.x  
- pytest  
- Requests library  
- JSON schemas (optional)  
- Swagger PetStore API  

---

🚀 **Features**

- ✔️ Modular Base API Client  
- ✔️ Wrapper clients for endpoint groups  
- ✔️ Reusable headers, configuration, and validators  
- ✔️ Organized test structure by domain  
- ✔️ Positive + Negative test coverage  
- ✔️ Terminal-friendly pytest execution  
- ✔️ Easily extendable for future endpoints  

---

🧪 **Tests Implemented**

**🐶 Pet Endpoints**  
- Add new pet  
- Update pet  
- Get pet by ID  
- Find pets by status  
- Delete pet  
- Negative tests (invalid IDs, malformed payloads)  

**🏬 Store Endpoints**  
- Place order  
- Get order  
- Delete order  
- Get store inventory  
- Error validation scenarios  

**👤 User Endpoints**  
- Create user  
- Get user  
- Login / logout  
- Update and delete user  
- Invalid credentials testing  

---

▶️ **Running the Project**

1️⃣ Install dependencies:  
```bash
pip install -r requirements.txt
2️⃣ Run all tests:

bash
Copy code
pytest -v
3️⃣ Run tests with HTML report (optional):

bash
Copy code
pytest --html=report.html

---

🎯 **Key Objectives**

- Promote clean, maintainable automation patterns  
- Demonstrate real-world API testing practices  
- Provide a learning foundation for QA engineers  
- Build a framework that can evolve with project needs  

---

💡 **QA Inspiration**

> “There’s a special kind of ASMR in watching clean green test logs flow in the terminal.”  

For QA engineers — **Quality isn’t just measured. It’s felt.**

---

🌱 **Future Enhancements**

- Environment-based configuration switching  
- CI/CD pipeline integration  
- Allure reporting or enhanced pytest HTML reports  
- Data-driven testing using JSON/YAML  
- Mock server integration  

---

🤝 **Contributions**

Contributions, improvements, and suggestions are welcome!  
Feel free to open issues or submit pull requests.
