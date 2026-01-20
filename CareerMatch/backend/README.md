# CareerMatch Backend Documentation

## Overview
CareerMatch is a full-stack web application designed to connect job seekers with potential employers. This backend is built using FastAPI, a modern web framework for building APIs with Python 3.6+ based on standard Python type hints.

## Project Structure
The backend is organized into several directories and files:

- **app/**: Contains the main application code.
  - **main.py**: The entry point of the FastAPI application.
  - **models/**: Contains data models used with SQLAlchemy or Pydantic for data validation.
  - **routes/**: Defines the API routes for the application.
  - **schemas/**: Contains Pydantic schemas for request and response validation.
  - **services/**: Contains business logic and service functions that interact with the database.
  - **config.py**: Configuration settings for the FastAPI application, including database connection details.

- **requirements.txt**: Lists the Python dependencies required for the backend project.

## Getting Started

### Prerequisites
- Python 3.6 or higher
- PostgreSQL database

### Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd CareerMatch/backend
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Running the Application
To start the FastAPI application, run:
```
uvicorn app.main:app --reload
```
This will start the server at `http://127.0.0.1:8000`.

### API Documentation
Once the server is running, you can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.