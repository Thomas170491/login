# Flask-Smorest Login Form

A simple login form API built with Flask and Flask-Smorest, featuring validation and OpenAPI documentation.

## Features

- **Flask-Smorest** for API management and documentation.
- **Marshmallow** for schema validation.
- **OpenAPI/Swagger** documentation available at `/swagger-ui`.

## Project Structure

```
flask_login_form/
│
├── venv/                 # Virtual environment
├── app.py                # Main application file
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Installation

1. Clone the repository and navigate to the project directory:

   ```bash
   git clone <repository-url>
   cd flask_login_form
   ```

2. Create and activate a virtual environment:

   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:

   ```bash
   python app.py
   ```

2. Open your browser and visit `http://127.0.0.1:5000/swagger-ui` to access the Swagger UI for the API documentation.

## API Endpoints

- **POST** `/login`: Allows users to log in by providing their credentials.

### Example API Request

#### Request

**POST** `/login`

```json
{
  "username": "example_user",
  "password": "example_password"
}
```

#### Response

- **Success** (200):

  ```json
  {
    "message": "Login successful"
  }
  ```

- **Failure** (400):

  ```json
  {
    "message": "Invalid credentials"
  }
  ```

## Dependencies

Make sure to have the following dependencies installed:

- Flask
- Flask-Smorest
- Marshmallow

They are included in the `requirements.txt` file. To install them:

```bash
pip install -r requirements.txt
```

## Development

To add or update routes, edit the `app.py` file. You can define new endpoints, add schemas for validation, and expand the API functionality.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Contact

For any questions or issues, feel free to open an issue on the repository or contact the project maintainer.
