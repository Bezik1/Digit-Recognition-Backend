# 0️⃣ Digit Recognition App – Backend

## 💡 Overview

This is the backend of Digit Reconigition App project. Server was built using Python and FastAPI framework. Application involes usage of machine learning digit recognition model, which is based on resnet architecture, fine-tuned to work with MNIST dataset.

## 🎯 Model Training

Model was trained, with such hyperparameters:
```python
num_class = 10
num_epochs = 2
batch_size = 100
learning_rate = 0.01
step_size = 100 
gamma = 0.9
```

## 🗒️ Features

* 🛜 Easy to use and develop REST API based on FastAPI
* 🤖 Pytorch model, with it's parameters ready to be used in practice
* ⚙️ Docker support for local development

## ⚙️ Command Tools

To work with this project locally or in a containerized environment, use the following commands:
```bash
conda env export > environment.yml # generates list of dependencies, which are used by conda

uvicorn index:app --reload # dev run command

uvicorn index:app --host 0.0.0.0 --port 8000 # run command

docker-compose up # 🐳 Run with Docker (backend + frontend)
````

## 🧠 Tech Stack
<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=python,fastapi,pytorch,anaconda,docker" />
  </a>
</p>
 
