# 🚀 Project Name

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/docker-%E2%9D%A4-blue.svg)](https://www.docker.com/)
[![GitHub Issues](https://img.shields.io/github/issues/your-username/your-repo.svg)](https://github.com/your-username/your-repo/issues)
[![GitHub Stars](https://img.shields.io/github/stars/your-username/your-repo.svg)](https://github.com/your-username/your-repo/stargazers)

> A brief project description and motivation.

## 📋 Table of Contents

- [Features](#-features)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
- [Usage](#-usage)  
- [Docker](#-docker)
- [Contributing](#-contributing)
- [License](#-license)
- [Acknowledgments](#-acknowledgments)

## ✨ Features

- List key features of your project here.

## 🚀 Getting Started

### Prerequisites

- Python
- Poetry
- Make
- Docker

**Clone the repository:**

```bash
git clone https://github.com/your-username/your-repo.git
```

### Install Dependencies

Before running the application, you need to install its dependencies. Follow the steps below:

1. Change into the project directory:

    ```bash
    cd your-repo
    ```

2. Install `pipx` if you haven't already:

    ```bash
    pip install pipx
    ```

3. Install `poetry` using `pipx`:

    ```bash
    pipx install poetry
    ```

4. Ensure that `pipx` is in your system's PATH:

    ```bash
    pipx ensurepath
    ```

5. Configure Poetry to create virtual environments within the project:

    ```bash
    poetry config virtualenvs.in-project true
    ```

6. Install project dependencies and create a virtual environment:

    ```bash
    make install
    make venv
    ```

These commands will set up the necessary environment for the project by installing Poetry, configuring virtual environments, and installing the required dependencies. Ensure you have Python, Poetry, and `make` installed on your system before proceeding with these steps.

**Run the app locally (without docker):**

```bash
make
```

## 🎬 Usage

- Add instructions on how to use the main functionality of the project

## 🐋 Docker

### Run with normal Docker

To run the application using Docker, you can build the Docker image and run a container.

**Build the Docker image:**

```bash
docker build -t your-image-name .
```

**Run the Docker container:**

```bash
docker run -p 8967:8967 -v $(pwd):/app your-image-name
```

Replace `your-image-name` with the desired name for your Docker image.

### Run with Docker Compose

Alternatively, you can use Docker Compose to simplify the process.

**Build and run with Docker Compose:**

```bash
docker-compose up --build
```

This command will build the Docker image and start the container defined in the `docker-compose.yaml` file.

Make sure to update the `docker-compose.yaml` file with the appropriate configurations for your project.

Note: If you encounter permission issues with Docker volumes, you may need to adjust the volume settings in the `docker-compose.yaml` file or use `sudo` to run Docker commands.

## 👪 Contributing

- Add guidelines for contributing to the project

## 📜 License

- Add the license type and details

## 🙏 Acknowledgments
