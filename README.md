# DineDine Project

Welcome to **DineDine**, an application designed to help users find restaurants based on their dietary preferences. This project was developed by Anton and Ismael. It's built using Django and leverages geographic location services, restaurant information, and dietary filtering.

## Project Setup

### Prerequisites

Before setting up the project, ensure your system has the following:

- **Python 3.8+**
- **PostgreSQL** with the PostGIS extension
- **GDAL** and **GEOS** libraries (for handling geographic data)
- **pip** (Python package installer)
- **virtualenv** (for creating isolated Python environments)

### Installation of Required Software

#### 1. Installing PostgreSQL, PostGIS, GDAL, and GEOS

##### On Ubuntu:

1. **Update the package lists and install PostgreSQL:**

   ```bash
   sudo apt update
   sudo apt install postgresql postgresql-contrib
   ```

2. **Install PostGIS:**

   ```bash
   sudo apt install postgis postgresql-14-postgis-3
   ```

3. **Install GDAL and GEOS:**

   ```bash
   sudo apt install gdal-bin libgdal-dev
   sudo apt install libgeos-dev
   ```

##### On macOS:

1. **Install Homebrew (if not already installed):**

   If you don't have Homebrew, you can install it using the following command:

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install PostgreSQL:**

   ```bash
   brew install postgresql
   brew services start postgresql
   ```

3. **Install PostGIS:**

   ```bash
   brew install postgis
   ```

4. **Install GDAL and GEOS:**

   ```bash
   brew install gdal
   brew install geos
   ```

5. **Start PostgreSQL (if not already running):**

   ```bash
   pg_ctl -D /usr/local/var/postgres start
   ```

#### 2. Setting Up Google API Key for Google Maps

To use Google Maps services (like Geocoding, Places, etc.) in your application, you need an API key.

1. **Create a Google Cloud Platform (GCP) project:**

   Go to the [Google Cloud Console](https://console.cloud.google.com/), create a new project, and navigate to the "APIs & Services" dashboard.

2. **Enable the necessary APIs:**

   - **Maps JavaScript API**
   - **Places API**
   - **Geocoding API**

   You can enable these APIs from the "Library" tab in the "APIs & Services" section.

3. **Generate the API Key:**

   - Go to "Credentials" under the "APIs & Services" section.
   - Click on "Create Credentials" and choose "API key."
   - Restrict the API key to your project’s requirements (optional but recommended).

4. **Add the API Key to Your Project:**

   Copy the generated API key and paste it into your `.env` file:

   ```bash
   GOOGLE_API_KEY=your-google-api-key
   ```

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
   \c dinedine
   CREATE EXTENSION postgis;
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
   GDAL_LIBRARY_PATH=/usr/local/lib/libgdal.dylib  # Update this path if using Ubuntu or a different path
   GEOS_LIBRARY_PATH=/usr/local/lib/libgeos_c.dylib  # Update this path if using Ubuntu or a different path
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


### Potential Improvements or Missing Components

- [ ] **Docker Setup:** Consider creating Dockerfiles and docker-compose configurations for easier setup and deployment, particularly for managing dependencies and environment consistency across different machines.
  
- [ ] **Testing:** Outline testing procedures, including any tools or frameworks (e.g., pytest, unittest) that should be used.

- [ ] **Static Files Handling:** manage static files for production
