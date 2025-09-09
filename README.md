Dockerized Flask CI/CD Pipeline with GitHub Actions
A complete DevOps project demonstrating a Continuous Integration and Continuous Deployment (CI/CD) pipeline for a Dockerized Flask application using GitHub Actions.

🚀 Features
Continuous Integration: Automated testing on every push/pull request

Containerization: Dockerized Flask application

Continuous Deployment: Automated Docker image building and pushing to Docker Hub

GitHub Actions: Full CI/CD workflow configuration

Local Development: Docker Compose setup for easy local development

🛠️ Tech Stack
Framework: Flask (Python)

Containerization: Docker, Docker Compose

CI/CD: GitHub Actions

Testing: Pytest

Registry: Docker Hub

📁 Project Structure
text
my-docker-ci-cd/
├── .github/
│   └── workflows/
│       └── ci-cd-pipeline.yml    # GitHub Actions workflow
├── app.py                        # Main Flask application
├── test_app.py                   # Unit tests
├── requirements.txt              # Production dependencies
├── requirements-test.txt         # Test dependencies
├── Dockerfile                    # Docker image definition
├── docker-compose.yml            # Local development setup
└── README.md                     # This file
⚡ Quick Start
Prerequisites
Docker installed on your machine

Docker Hub account

GitHub account

1. Clone the Repository
bash
git clone https://github.com/YOUR_USERNAME/my-docker-ci-cd.git
cd my-docker-ci-docker
2. Run with Docker Compose (Recommended)
bash
docker-compose up -d --build
Visit: http://localhost:5000

3. Or Run with Docker Commands
bash
# Build the image
docker build -t my-docker-app:v1 .

# Run the container
docker run -d -p 5000:5000 --name my-running-app my-docker-app:v1
Visit: http://localhost:5000

4. Run Tests Locally
bash
# Install dependencies
pip install -r requirements.txt
pip install -r requirements-test.txt

# Run tests
python -m pytest test_app.py -v
🔧 CI/CD Pipeline Setup
1. Configure GitHub Secrets
Go to your GitHub repository → Settings → Secrets → Actions → New repository secret:

DOCKERHUB_USERNAME: Your Docker Hub username

DOCKERHUB_TOKEN: Your Docker Hub access token (not password)

2. How the Pipeline Works
The GitHub Actions workflow (.github/workflows/ci-cd-pipeline.yml) automatically:

Triggers on push to main branch or pull requests

Checks out your code

Sets up Python environment

Runs tests using pytest

Logs in to Docker Hub

Builds and pushes Docker image with two tags:

:latest (latest stable version)

:<git-commit-sha> (specific version for tracking)

Simulates deployment (in a real scenario, this would deploy to a server)

3. View Pipeline Results
Go to your GitHub repository → Actions tab

Click on the latest workflow run to see detailed logs

Check Docker Hub to see your pushed images

📦 Docker Commands Cheat Sheet
bash
# Build image
docker build -t my-docker-app:v1 .

# Run container
docker run -d -p 5000:5000 --name my-app my-docker-app:v1

# View running containers
docker ps

# View container logs
docker logs my-app

# Stop container
docker stop my-app

# Remove container
docker rm my-app

# Remove image
docker rmi my-docker-app:v1

# Use Docker Compose
docker-compose up -d --build    # Start with build
docker-compose down             # Stop and remove
docker-compose logs             # View logs
🌐 Access the Application
After running the container, access your application at:

text
http://localhost:5000
You should see: "Hello, World! This is my automated Docker CI/CD pipeline!"

🧪 Testing

The project includes automated testing:
Test file: test_app.py
Test command: python -m pytest test_app.py -v
Tests run automatically on every push via GitHub Actions
