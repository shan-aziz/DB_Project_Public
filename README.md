# Telemedicine App - Database Project (CS 6360)

## Team Members

*   SXB220013 - Sai Kumar Boddu
*   SXD210166 - Sandeep Reddy Daida
*   CXA220003 - Chandan Alwala
*   JXP220032 - Jayanth Avinash Potnuru
*   SXA220103 - Shan Aziz

---

## Table of Contents

1.  [Introduction](#introduction)
2.  [Features](#features)
3.  [Technology Stack](#technology-stack)
4.  [Database Design](#database-design)
5.  [Project Structure](#project-structure)
6.  [Prerequisites](#prerequisites)
7.  [Setup and Installation](#setup-and-installation)
8.  [Running the Application](#running-the-application)
9. [Report Reference](#report-reference)

---

## Introduction

This project is a web-based Telemedicine Application developed as part of the CS 6360 Database Design course. The application aims to connect Patients, Doctors, and Administrators within a virtual healthcare system. It facilitates user management, basic browsing, and role-specific functionalities, all backed by a relational database designed and implemented according to database design principles.

---

## Features

Based on the project's functional requirements:

*   **Login Functionalities:** Secure user authentication for registered Admins, Patients, and Doctors.
*   **Browsing Functionalities:** (Details would depend on specific implementation - e.g., viewing profiles, available services).
*   **Admin Functionalities:**
    *   Manage users (Patients, Doctors).
    *   View system information (e.g., customer lists as seen in `app.py`).
    *   (Potentially others like managing suppliers/orders based on `app.py` routes, though the report focuses on Doc/Pat/Admin).
*   **Patient Functionalities:** (Details would depend on specific implementation - e.g., booking appointments, viewing records).
*   **Doctor Functionalities:** (Details would depend on specific implementation - e.g., managing appointments, viewing patient info).
*   **User Registration:** Allows new users to register into the system (Admin, Customer/Patient roles implemented in `app.py`).

---

## Technology Stack

*   **Backend:** Python with Flask Framework
*   **Database:** MySQL
*   **Database Connector:** Flask-MySQLdb, PyMySQL, MySQLdb
*   **Configuration:** YAML (for database credentials)
*   **Frontend:** HTML, CSS, JavaScript (inferred, templates required by Flask)

---

## Database Design

A significant focus of this project was the database design:

*   **Conceptual Design:** An Entity-Relationship (ER) Diagram was created to model the data requirements. (Refer to the project report for the diagram).
*   **Logical Design:** A relational schema was derived from the ER diagram. (Refer to the report for the detailed schema).
*   **Normalization:** Functional dependencies were analyzed, and the database schema was normalized to reduce redundancy and improve data integrity (likely to 3NF or BCNF, check report).
*   **Integrity Constraints:** Business rules and constraints (e.g., primary keys, foreign keys, data types, checks) were defined and implemented.
*   **Data Dictionary:** A comprehensive data dictionary defining all tables, attributes, and data types was created. (Refer to the report).

---

## Project Structure


```text
.
|-- app.py            # Main Flask application file
|-- constants.py      # Defines constants (ADMIN, CUS, SUP, etc.)
|-- db.yaml           # Database configuration (user needs to create this)
|-- requirements.txt  # Python package dependencies
|-- static/           # Optional: For CSS, JS, images
|   `-- ...           # (Subdirectories/files for static assets)
`-- templates/        # HTML templates rendered by Flask
    |-- index.html    # Login page
    |-- register.html # Registration page
    |-- admin_home.html # Admin dashboard
    `-- ...           # (Other templates for different user roles and pages)

```
---

## Prerequisites

*   Python 3.x
*   pip (Python package installer)
*   MySQL Server

---

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <repository-directory>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    *   Create a `requirements.txt` file with the following content:
        ```txt
        Flask
        Flask-MySQLdb
        PyYAML
        PyMySQL
        mysqlclient # Or specific MySQLdb driver if needed
        ```
    *   Install the packages:
        ```bash
        pip install -r requirements.txt
        ```

4.  **Set up the MySQL Database:**
    *   Ensure your MySQL server is running.
    *   Create a database (e.g., `telemedicine` or `ecommerce_db_project` based on usage in `app.py`).
        ```sql
        CREATE DATABASE your_database_name;
        USE your_database_name;
        ```
    *   **Execute the SQL Schema:** Obtain the `CREATE TABLE` statements from the **"SQL Statements used to construct the Schema"** section or the **Appendix** of the project report (`Phase-5 Final Report.pdf/docx`). Execute these SQL commands in your MySQL client (like MySQL Workbench, DBeaver, or the command line) to create the necessary tables (`accounts`, `admin`, `customer`/`patient`, `doctor`, etc.).

5.  **Configure Database Connection:**
    *   Create a file named `db.yaml` in the root directory.
    *   Add your MySQL database credentials:
    ```yaml
    mysql_host: localhost
    mysql_user: <your_mysql_user>
    mysql_password: <your_mysql_password>
    mysql_db: <your_database_name> # Must match the database created in step 4
    ```
    *   Replace placeholders with your actual MySQL credentials.

6.  **Create HTML Templates:**
    *   Ensure the `templates` directory exists.
    *   Place all required HTML files (`index.html`, `register.html`, `admin_home.html`, etc.) inside the `templates` directory. These files are necessary for the `render_template` calls in `app.py`.

---

## Running the Application

1.  **Ensure your virtual environment is activated.**
2.  **Run the Flask development server:**
    ```bash
    python app.py
    ```
    or if Flask CLI is configured:
    ```bash
    flask run
    ```
3.  **Access the application:** Open your web browser and navigate to `http://127.0.0.1:5000/` (or the address provided by Flask).

---


## Report Reference

For detailed information on requirements, database design (ER Diagram, Schema, Normalization, Constraints), SQL queries, tuning suggestions, and screenshots, please refer to the full project report: **`Final Report`**
