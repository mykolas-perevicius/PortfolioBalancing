# PortfolioBalancing

## Introduction
Brief introduction to your project.

## Prerequisites
Before you begin, ensure you have the following installed:
- Python (3.8+)
- Node.js and npm (for React Native)
- PostgreSQL
- Git

## Installation

### Backend Setup
1. **Clone the Repository**:
   ```bash
   git clone [repository URL]
   ```

2. **Navigate to the backend directory**:
   ```bash
   cd backend
   ```

3. **Set up a Python virtual environment**:
   ```bash
   python3 -m venv venv
   ```
    > If you don't have `venv` installed, run `pip3 install venv` first.

4. **Activate the virtual environment**:
    ```bash
    source venv/bin/activate
    ```
     > If you're on Windows, run `venv\Scripts\activate` instead.

5. **Install the required Python packages**:
    ```bash
    pip3 install -r requirements.txt
    ```
    > If you make any changes to the Python packages, run `pip3 freeze > requirements.txt` to update the `requirements.txt` file.

6. **Set up PostgreSQL**:
    - Download and install PostgreSQL from [here](https://www.postgresql.org/download/).
    - Configure connection settings in .env file:
        ```
        DB_HOST=localhost
        DB_PORT=5432
        DB_NAME=postgres
        DB_USER=postgres
        DB_PASSWORD=postgres
        DATABASE_URL=postgresql://username:password@localhost/your_database_name
        ```

7. **Create the database**:
    ``` psql -U postgres -c "CREATE DATABASE balancing_main;" ```
