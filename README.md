# My First CI/CD App 🚀

A simple Flask API built to practice CI/CD with GitHub Actions.

![CI/CD](https://github.com/ShashiKaran-git/my-first-ci-cd-app/actions/workflows/main.yml/badge.svg)

## Routes
- `/` → returns app name and status
- `/ping` → returns pong!

## Tech Stack
- Python + Flask
- pytest for testing
- Docker
- GitHub Actions for CI/CD

## CI/CD Pipeline
- Tests run automatically on Python 3.9, 3.10, 3.11
- Docker image built and pushed to Docker Hub on every push
- Docker Hub: [shashikarandev/my-first-ci-cd-app](https://hub.docker.com/r/shashikarandev/my-first-ci-cd-app)

## Run Locally
```bash
docker pull shashikarandev/my-first-ci-cd-app:latest
docker run -p 5002:5000 shashikarandev/my-first-ci-cd-app:latest
```
Visit http://localhost:5002
