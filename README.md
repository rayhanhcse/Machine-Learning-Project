
<h1 align="center">
  <span style="background: linear-gradient(to right, #1e3c72, #2a5298); -webkit-background-clip: text; color: transparent;">
    🛂 US Visa Prediction Project
  </span>
</h1>

<p align="center">
  <strong>Predict US Visa application approval using Machine Learning & deploy via AWS CI/CD</strong>
</p>

<p align="center">
  <a href="https://github.com/rayhanhcse/Machine-Learning-Project">
    <img src="https://img.shields.io/badge/GitHub-rayhanhcse-181717?style=for-the-badge&logo=github" alt="GitHub Badge"/>
  </a>
  <a href="mailto:rayhanhcse@gmail.com">
    <img src="https://img.shields.io/badge/Email-rayhanhcse@gmail.com-D14836?style=for-the-badge&logo=gmail" alt="Email Badge"/>
  </a>
  <a href="https://linkedin.com/in/rayhanchse">
    <img src="https://img.shields.io/badge/LinkedIn-rayhanchse-0077B5?style=for-the-badge&logo=linkedin" alt="LinkedIn Badge"/>
  </a>
  <img src="https://img.shields.io/badge/Python-3.8-3776AB?style=for-the-badge&logo=python" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/Anaconda-202020?style=for-the-badge&logo=anaconda" alt="Anaconda Badge"/>
</p>

---

## 📘 Overview
The **US Visa Prediction Project** predicts whether a US visa application will be **approved** or **denied** using **Machine Learning** techniques.  
It analyzes historical visa data to identify key factors influencing visa approval decisions.

---

## 🎯 Project Objectives
- Predict approval/denial of US visa applications  
- Identify important features impacting visa approval  
- Provide insights for applicants and organizations  

---

## 🧩 Key Features
1. Data Cleaning & Preprocessing  
2. Exploratory Data Analysis (EDA)  
3. Feature Engineering  
4. Machine Learning Model Training  
5. Model Evaluation & Visualization  
6. Web/App Interface for Prediction (optional)  

---

## 🛠 Tools You Need
| Tool | Link |
|------|------|
| Anaconda | [Download](https://www.anaconda.com/) |
| VS Code | [Download](https://code.visualstudio.com/download) |
| Git | [Download](https://git-scm.com/) |

---

## 🗂 Database Used
- **MongoDB**: [Login](https://account.mongodb.com/account/login)  

---

## 📁 Dataset
- **Kaggle Dataset:** [EasyVisa Dataset](https://www.kaggle.com/datasets/moro23/easyvisa-dataset)  

---

## 🚀 Project Workflow
```

1. constant
2. config_entity
3. artifact_entity
4. component
5. pipeline
6. app.py / demo.py

````

---

## ⚡ How to Run

### Clone Repository
```bash
git clone https://github.com/rayhanhcse/Machine-Learning-Project.git
cd Machine-Learning-Project
````

### Create & Activate Environment

```bash
conda create -n visa python=3.8 -y
conda activate visa
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Export Environment Variables

> Replace with your actual keys/URLs

```bash
export MONGODB_URL="your_mongodb_url"
export AWS_ACCESS_KEY_ID="your_aws_access_key_id"
export AWS_SECRET_ACCESS_KEY="your_aws_secret_access_key"
```

---

## ☁️ AWS CI/CD Deployment Steps

### 1️⃣ Login to AWS Console

### 2️⃣ Create IAM User for Deployment

* Permissions required:

  * **EC2 Full Access**
  * **ECR Full Access**

**Deployment Steps:**

1. Build Docker image of source code
2. Push Docker image to **ECR**
3. Launch **EC2** instance
4. Pull Docker image from **ECR**
5. Run Docker image on EC2

---

### 3️⃣ Create ECR Repository

* Save URI: `315865595366.dkr.ecr.us-east-1.amazonaws.com/usvisarepo`

---

### 4️⃣ Launch EC2 Instance (Ubuntu)

---

### 5️⃣ Install Docker on EC2

```bash
sudo apt-get update -y
sudo apt-get upgrade -y
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```

---

### 6️⃣ Configure EC2 as Self-Hosted GitHub Runner

* Go to GitHub → **Settings → Actions → Runners → New self-hosted runner**
* Choose OS and follow commands

---

### 7️⃣ Setup GitHub Secrets

| Secret Name           | Description                  |
| --------------------- | ---------------------------- |
| AWS_ACCESS_KEY_ID     | AWS Access Key               |
| AWS_SECRET_ACCESS_KEY | AWS Secret Key               |
| AWS_DEFAULT_REGION    | AWS Region (e.g., us-east-1) |
| ECR_REPO              | ECR Repository URI           |
| MONGODB_URL           | MongoDB Connection URL       |

---

### 🌐 Flowchart Tool

* [Whimsical](https://whimsical.com/a)

---

### 👨‍💻 Author

**Rayhan Hussain**
📧 Email: [rayhanhcse@gmail.com](mailto:rayhanhcse@gmail.com)
🌐 GitHub: [rayhanhcse](https://github.com/rayhanhcse)
💼 LinkedIn: [rayhanchse](https://linkedin.com/in/rayhanchse)

---

<p align="center">
  <img src="https://media.giphy.com/media/l0HlPjez2i0gTSmFe/giphy.gif" width="100" alt="Deployment GIF"/>
</p>
```

---


