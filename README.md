# 🖼️ Image Moderation API

A **FastAPI** application designed to moderate images using the **Sightengine API**, 
featuring **token-based authentication** with **MongoDB**. The project supports both local and Docker-based deployments.

---

## 🚀 Features

- Image moderation via Sightengine
- Token-based authentication
- Admin endpoints to manage tokens
- Dockerized deployment with MongoDB
- Interactive API documentation with Swagger UI

---

## 📦 Prerequisites

Ensure the following are installed:

- [Docker & Docker Compose](https://docs.docker.com/get-docker/)
- Python 3.11 (for local setup)
- MongoDB (if running locally)
- Sightengine account and credentials

---

## ⚙️ Setup Instructions (Local)

### 1. Clone and Set Up the Project

```bash
git clone https://github.com/HaseebUrRehman123/Image-moderation.git
cd Image-moderation
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Environment Variables

Create a `.env` file in the project root with the following content:

```env
SIGHTENGINE_API_USER=your_sightengine_user
SIGHTENGINE_API_SECRET=your_sightengine_secret
MONGO_URL=mongodb://localhost:27017
SECRET_KEY=your_secret_key
```

---

## 🐳 Docker Deployment

### 1. Build and Run Containers

```bash
docker-compose up --build
```

### 2. Stop Containers

```bash
docker-compose down
```

---

## 📘 API Documentation

Once the server is running, access the interactive Swagger docs at:

```
http://localhost:7000/docs
```

Or use the ReDoc documentation:

```
http://localhost:7000/redoc
```

---

