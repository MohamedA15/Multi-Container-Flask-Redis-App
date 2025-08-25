# Multi-Container Flask Redis App

A simple Flask web application using **Redis** as a backend, designed to run in a **multi-container environment** with Docker and Docker Compose.

---

## Features

- Flask-based web application
- Redis integration for fast, in-memory data storage
- Multi-container setup using Docker Compose
- Easy to run and scale

---

## Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Python 3.9+ (for local development if not using Docker)

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/MohamedA15/Multi-Container-Flask-Redis-App.git
cd Multi-Container-Flask-Redis-App

.
├── app.py                  # Main Flask web app (backend logic)
├── templates/              # Folder for HTML templates
│   └── index.html          # Main page template for the counter
├── Dockerfile              # Dockerfile for Flask app
├── docker-compose.yml      # Docker Compose configuration (Flask + Redis)
├── requirements.txt        # Python dependencies
├── .gitignore              # Files and folders to ignore in Git
└── README.md               # Project documentation

Usage
The Flask app connects to Redis to store and retrieve data.
You can extend the app by adding more routes, APIs, or connecting additional services.
Contributing
Fork the repository
Create a new branch: git checkout -b feature-name
Make your changes and commit: git commit -m "Add feature"
Push to the branch: git push origin feature-name
Open a Pull Request
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Flask documentation: https://flask.palletsprojects.com
Redis documentation: https://redis.io/documentation
Docker documentation: https://docs.docker.com