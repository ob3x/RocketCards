# ROCKETCARDS

_Elevate Learning with Engaging Flashcard Experiences_

![last commit](https://img.shields.io/github/last-commit/ob3x/RocketCards)
![language](https://img.shields.io/badge/javascript-78.7%25-yellow)
![languages](https://img.shields.io/github/languages/count/ob3x/RocketCards)

Built with the tools and technologies:  
![technologies](https://img.shields.io/badge/JSON-%23f7df1e.svg?logo=json&style=flat) ![JavaScript](https://img.shields.io/badge/JavaScript-%23f7df1e.svg?logo=javascript&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-%2300c7b7.svg?logo=fastapi&logoColor=white) ![React](https://img.shields.io/badge/React-%2361DAFB.svg?logo=react&logoColor=white) ![Axios](https://img.shields.io/badge/Axios-%230074ff.svg?logo=axios&logoColor=white) ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-%23d71f00.svg?logo=sqlalchemy&logoColor=white) ![Python](https://img.shields.io/badge/Python-%233776ab.svg?logo=python&logoColor=white) ![Vite](https://img.shields.io/badge/Vite-%23646cff.svg?logo=vite&logoColor=white) ![npm](https://img.shields.io/badge/npm-%23CB3837.svg?logo=npm&logoColor=white) ![ESLint](https://img.shields.io/badge/ESLint-%234B32C3.svg?logo=eslint&logoColor=white) ![CSS](https://img.shields.io/badge/CSS-%231572B6.svg?logo=css3&logoColor=white) ![TAILWINDCSS](https://img.shields.io/badge/tailwindcss-0F172A?&logo=tailwindcss) ![Pydantic](https://img.shields.io/badge/Pydantic-%2300A7E7.svg?logo=pydantic&logoColor=white)

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)

## Overview

RocketCards is an application designed to help learn English and manage interactive flashcards, combining a FastAPI backend with a dynamic React frontend.

### Why RocketCards?

This project empowers users to build scalable and secure flashcard decks effortlessly. The core features include:

- :rocket: **FastAPI Backend**: Efficient web service development with asynchronous capabilities.
- :bust_in_silhouette: **User Management**: Secure authentication and user profile management.
- :bookmark_tabs: **Flashcard Management**: Create, edit, and manage flashcards and decks seamlessly.
- :white_check_mark: **Data Validation with Pydantic**: Ensures data integrity and consistency across the application.
- :sparkles: **Responsive Frontend with React**: Engaging user interface with modern design principles.

## Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language**: JavaScript
- **Package Manager**: Pip, Npm

## Installation

Build RocketCards from the source and install dependencies:

1. Clone the repository:

    ```bash
    git clone https://github.com/ob3x/RocketCards
    ```

2. Navigate to the project directory:

    ```bash
    cd RocketCards
    ```

3. Install the dependencies:

    Using **pip**:

    ```bash
    cd backend
    pip install -r backend/requirements.txt
    ```

    Using **npm**:

    ```bash
    cd frontend
    npm install
    ```

## Usage

Run the project:

```bash
cd frontend
npm run dev

cd backend
uvicorn main:app --reload
