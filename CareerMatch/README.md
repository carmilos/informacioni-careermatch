# CareerMatch Project

CareerMatch is a full-stack web application designed to connect job seekers with potential employers. This project utilizes Angular for the frontend, FastAPI with Python for the backend, and PostgreSQL for the database.

## Project Structure

The project is organized into two main directories: `frontend` and `backend`.

### Frontend

The frontend is built using Angular and contains the following structure:

- **src/app/components**: Contains Angular components representing different parts of the user interface.
- **src/app/services**: Contains Angular services for data fetching and business logic.
- **src/app/models**: Contains TypeScript models defining the data structures used in the application.
- **src/app/app.component.ts**: The root component of the Angular application.
- **src/assets**: Contains static assets such as images and fonts.
- **src/styles**: Contains global styles and CSS files.
- **src/main.ts**: The entry point of the Angular application.
- **src/index.html**: The main HTML file serving the Angular application.

### Backend

The backend is built using FastAPI and contains the following structure:

- **app/main.py**: The entry point of the FastAPI application.
- **app/models**: Contains data models used with SQLAlchemy or Pydantic.
- **app/routes**: Defines the API routes for the application.
- **app/schemas**: Contains Pydantic schemas for request and response validation.
- **app/services**: Contains business logic and service functions.
- **app/config.py**: Contains configuration settings for the FastAPI application.
- **requirements.txt**: Lists the Python dependencies required for the backend.

## Getting Started

To get started with the CareerMatch project, follow these steps:

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd CareerMatch
   ```

2. **Set up the frontend**:
   - Navigate to the `frontend` directory.
   - Install dependencies:
     ```
     npm install
     ```
   - Run the development server:
     ```
     ng serve
     ```

3. **Set up the backend**:
   - Navigate to the `backend` directory.
   - Create a virtual environment and activate it:
     ```
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```
   - Install dependencies:
     ```
     pip install -r requirements.txt
     ```
   - Run the FastAPI application:
     ```
     uvicorn app.main:app --reload
     ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.