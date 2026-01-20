# CareerMatch Frontend Documentation

## Overview
CareerMatch is a web application designed to connect job seekers with potential employers. This frontend is built using Angular, providing a dynamic and responsive user interface.

## Project Structure
The frontend project is organized as follows:

- **src/**: Contains the source code for the Angular application.
  - **app/**: The main application module.
    - **components/**: Angular components representing different parts of the user interface.
    - **services/**: Services for data fetching and business logic.
    - **models/**: TypeScript models defining data structures.
    - **app.component.ts**: The root component of the application.
  - **assets/**: Static assets such as images and fonts.
  - **styles/**: Global styles and CSS files.
  - **main.ts**: Entry point of the Angular application.
  - **index.html**: Main HTML file serving the application.

## Getting Started

### Prerequisites
- Node.js and npm installed on your machine.

### Installation
1. Navigate to the frontend directory:
   ```
   cd frontend
   ```
2. Install the dependencies:
   ```
   npm install
   ```

### Running the Application
To start the development server, run:
```
ng serve
```
The application will be available at `http://localhost:4200`.

## Building for Production
To build the application for production, use:
```
ng build --prod
```
The output will be in the `dist/` directory.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.

## License
This project is licensed under the MIT License.