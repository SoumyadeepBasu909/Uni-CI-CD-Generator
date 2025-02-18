# 🚀 Universal CI/CD Pipeline Generator

## 📌 Overview
The **Universal CI/CD Pipeline Generator** is a web-based tool that helps developers generate **Jenkinsfiles**, **GitHub Actions**, and **GitLab CI** pipelines based on their project configuration. This eliminates the need for manually writing pipeline files, speeding up the CI/CD setup process.

## 🎯 Features
- Supports **Jenkins**.
- Generates pipelines dynamically based on user input.
- Provides an easy-to-use web interface.
- Uses **FastAPI** as the backend for handling requests.
- Supports **templating** with Jinja2 to generate pipeline files.

---

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, FastAPI
- **Templating Engine:** Jinja2
- **Package Management:** Pip
- **Server:** Uvicorn (for running FastAPI)

---

## 🚀 Installation & Setup

### **1️⃣ Clone the Repository**

$ git clone https://github.com/your-repo/universal-cicd-generator.git

$ cd universal-cicd-generator

### **3️⃣ Install Dependencies**

$ pip install -r requirements.txt


### **4️⃣ Run the FastAPI Backend**

$ uvicorn main:app --host 0.0.0.0 --port 8000 --reload


This starts the API server at `http://127.0.0.1:8000/`

### **5️⃣ Open the Web Interface**
1. Open `index.html` in your browser.
2. Fill in the form with your project details.
3. Click **Generate Pipeline** to get your CI/CD script.

---

## 🎮 Usage Guide

### **1️⃣ Input Fields in the Web Form**
| Field | Description |
|-------|------------|
| CI/CD Tool | Select Jenkins, GitHub Actions, or GitLab CI |
| Project Type | Specify your tech stack (e.g., Java, Python, Node.js) |
| GitHub Repository | Enter the repository URL |
| Build Tool | Specify the build tool (e.g., Maven, Gradle, NPM) |
| Deployment | Define deployment type (e.g., Docker, Kubernetes) |
| Build Command | Enter the build command (e.g., `mvn clean install`) |
| Test Command | Enter test command (e.g., `pytest`, `npm test`) |
| Artifact Path | Specify output files (e.g., `target/*.jar`) |
| Docker Image | (Optional) Specify a Docker image if used |

### **2️⃣ Generating a Pipeline**
1. Fill in the required details.
2. Click **Generate Pipeline**.
3. The tool will generate a **Jenkinsfile**.

### **3️⃣ Running the Generated Pipeline**
- **Jenkins:** Copy the generated `Jenkinsfile` into your repository root and configure Jenkins.

---

## 🛠️ API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | `/generate` | Generates a pipeline file based on user input |

### **Request Format**

{
  "ci_cd_tool": "github",
  
  "github_url": "https://github.com/example/repo.git",
  
  "project_type": "python",
  
  "build_tool": "pip",
  
  "deployment": "docker",
  
  "build_command": "pip install -r requirements.txt",
  
  "test_command": "pytest",
  
  "artifact": "dist/*.whl",
  
  "docker_image": "python:3.9"
}
`

### **Response Format**
Returns a generated pipeline file as plain text.

---

## 🔥 Future Enhancements
- Add support for **Bitbucket Pipelines**.
- Support **custom CI/CD configurations**.
- Improve UI with **Bootstrap or React**.
- Implement a **pipeline preview** feature.

---

## 💡 Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

---

## 📜 License
This project is licensed under the **MIT License**.

---

## 📞 Contact
For any questions, reach out via:
📧 Email: soumyadeepbasu1998.sb@gmail.com

