# Flask Task Manager 📝

![CI/CD Pipeline](https://github.com/fanninggh/flask-task-manager/workflows/CI/CD%20Pipeline/badge.svg)
![Python](https://img.shields.io/badge/python-3.10-blue.svg)
![Flask](https://img.shields.io/badge/flask-3.0-green.svg)
![Docker](https://img.shields.io/badge/docker-enabled-blue.svg)
![Kubernetes](https://img.shields.io/badge/kubernetes-ready-brightgreen.svg)

A modern task management web application built with Flask, containerized with Docker, and orchestrated with Kubernetes. Features a complete CI/CD pipeline for automated testing and deployment.

## 🚀 Features

- ✅ Create, read, update, delete tasks (CRUD operations)
- ✅ Mark tasks as complete/incomplete
- ✅ Persistent SQLite database with SQLAlchemy
- ✅ Responsive modern UI with gradient design
- ✅ Containerized with Docker
- ✅ Kubernetes deployment ready
- ✅ Automated CI/CD pipeline with GitHub Actions
- ✅ Comprehensive test coverage with pytest

## 🛠️ Tech Stack

- **Backend:** Python 3.10, Flask 3.0
- **Database:** SQLite with SQLAlchemy ORM
- **Frontend:** HTML5, CSS3, Jinja2 templates
- **Containerization:** Docker
- **Orchestration:** Kubernetes (Minikube)
- **CI/CD:** GitHub Actions
- **Testing:** pytest, pytest-flask

## 📦 Quick Start

### Local Development
```bash
# Clone repository
git clone https://github.com/fanninggh/flask-task-manager.git
cd flask-task-manager

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
```

Access at: **http://localhost:5000**

### Docker
```bash
# Build image
docker build -t flask-task-manager .

# Run container
docker run -d -p 5000:5000 --name task-manager flask-task-manager

# Access application
open http://localhost:5000
```

### Kubernetes (Minikube)
```bash
# Start Minikube
minikube start --driver=docker

# Deploy application
kubectl apply -f k8s/all-in-one.yaml

# Wait for pods to be ready
kubectl wait --for=condition=ready pod -l app=flask-task-manager --timeout=60s

# Access service
minikube service flask-task-manager-service
```

## 🧪 Testing
```bash
# Run tests
pytest tests/ -v

# Run with coverage report
pytest tests/ --cov=. --cov-report=html

# View coverage report
open htmlcov/index.html
```

## 🔄 CI/CD Pipeline

The project includes a complete CI/CD pipeline using GitHub Actions that automatically:

1. **Test Stage:** Runs pytest with coverage on every push/PR
2. **Build Stage:** Builds Docker image if tests pass
3. **Push Stage:** Pushes image to Docker Hub
4. **Deploy Stage:** Shows deployment instructions

### Pipeline Triggers:
- ✅ Push to `main` or `develop` branch
- ✅ Pull requests to `main`

### Pipeline Jobs:
- 🧪 **Test:** Run automated tests
- 🐳 **Build:** Build Docker image
- 🚀 **Deploy:** Deployment summary

## 📊 Project Structure
```
flask-task-manager/
├── .github/
│   └── workflows/
│       └── ci-cd.yml         # CI/CD pipeline configuration
├── tests/
│   ├── __init__.py
│   └── test_app.py          # Automated tests
├── templates/               # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── add_task.html
│   └── edit_task.html
├── static/
│   └── css/
│       └── style.css        # Styling
├── k8s/                     # Kubernetes manifests
│   └── all-in-one.yaml     # Complete K8s deployment
├── app.py                   # Main Flask application
├── models.py                # Database models
├── requirements.txt         # Python dependencies
├── Dockerfile              # Docker configuration
├── .dockerignore
├── .gitignore
└── README.md
```

## 🌐 Deployment

### Pull from Docker Hub
```bash
docker pull fanninggh/flask-task-manager:latest
docker run -d -p 5000:5000 fanninggh/flask-task-manager:latest
```

### Update Kubernetes Deployment
```bash
kubectl set image deployment/flask-task-manager \
  flask-app=fanninggh/flask-task-manager:latest
  
kubectl rollout status deployment/flask-task-manager
```

## 📈 Key Features Demonstrated

- ✅ Full-stack web development
- ✅ RESTful design patterns
- ✅ Database modeling and ORM
- ✅ Test-driven development (TDD)
- ✅ Docker containerization
- ✅ Kubernetes orchestration
- ✅ CI/CD automation
- ✅ Infrastructure as Code (YAML)
- ✅ Git version control
- ✅ Cloud-native architecture

## 🔧 Configuration

### Environment Variables
```bash
FLASK_ENV=production          # Flask environment
SECRET_KEY=your-secret-key    # Flask secret key
PYTHONUNBUFFERED=1           # Python output buffering
```

### Kubernetes Resources

- **Deployment:** 2 replicas with resource limits
- **Service:** NodePort on port 30080
- **PersistentVolume:** 1Gi storage for database
- **ConfigMap:** Application configuration
- **Secret:** Sensitive data management

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**fanninggh**
- GitHub: [@fanninggh](https://github.com/fanninggh)
- Repository: [flask-task-manager](https://github.com/fanninggh/flask-task-manager)

## 🙏 Acknowledgments

- Flask framework and community
- Docker and Kubernetes ecosystems
- GitHub Actions for CI/CD
- Open source contributors

## ⭐ Show Your Support

Give a ⭐️ if this project helped you learn DevOps!

---

**Built with ❤️ for learning DevOps and Cloud Native technologies**
