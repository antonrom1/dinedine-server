# DineDine Project

Welcome to **DineDine**, an application designed to help users find restaurants based on their dietary preferences. This project was developed by Anton, Ismael. It's built using Django and leverages geographic location services, restaurant information, and dietary filtering.

## Project Setup

### Prerequisites

Before setting up the project, ensure your system has the following:

- **Python 3.8+**
- **PostgreSQL** with the PostGIS extension
- **GDAL** and **GEOS** libraries (for handling geographic data)
- **pip** (Python package installer)
- **virtualenv** (for creating isolated Python environments)

### Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/dinedine.git
cd dinedine
```

### Set Up the Environment

Create a virtual environment to isolate your Python dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### Database Setup

1. **Configure PostgreSQL with PostGIS:**

   Ensure PostgreSQL is running and has the PostGIS extension installed. Create a new database for the project:

   ```bash
   sudo -u postgres psql
   CREATE DATABASE dinedine;
   CREATE USER yourusername WITH PASSWORD 'yourpassword';
   ALTER ROLE yourusername SET client_encoding TO 'utf8';
   ALTER ROLE yourusername SET default_transaction_isolation TO 'read committed';
   ALTER ROLE yourusername SET timezone TO 'UTC';
   GRANT ALL PRIVILEGES ON DATABASE dinedine TO yourusername;
   \q
   ```

2. **Set up environment variables:**

   Create a `.env` file in the project root and add the following (replace with your actual values):

   ```bash
   DBNAME=dinedine
   DBUSER=yourusername
   DBPASS=yourpassword
   DBHOST=localhost
   DBPORT=5432
   SECRET_KEY=your-secret-key
   GOOGLE_API_KEY=your-google-api-key
   GDAL_LIBRARY_PATH=/usr/local/lib/libgdal.dylib
   GEOS_LIBRARY_PATH=/usr/local/lib/libgeos_c.dylib
   ```

3. **Apply migrations to set up the database schema:**

   ```bash
   python manage.py migrate
   ```

### Run the Application

To start the development server, use:

```bash
python manage.py runserver
```

Before being able to manage data, you need to create a superuser:

```bash
python manage.py createsuperuser
```

You can now access the application at `http://127.0.0.1:8000/`.
API is available at `http://127.0.0.1:8000/api/`.
And admin (to manage data) is available at `http://127.0.0.1:8000/admin/`.


## Development

### Directory Structure

- `dinedine/` - Contains the main Django project settings.
- `restaurants/` - Contains the app responsible for managing restaurant data.
- `diet/` - Contains the app for handling dietary preferences.
