# Plantify 

## About the project

Plantify is a Django-based web application designed to help plant lovers organize and manage their indoor plant collections.

The application allows users to maintain a personal plant catalog, track plant care activities, monitor care statistics, and organize plants into custom collections.

##  Features

1. Plant Management – Create, view, edit, and delete plants.

2. Plant Catalog – Browse plants, search by scientific name, and filter by room.

3. Plant Details – View plant information and its care history.

4. Care Journal – Record watering, fertilizing, pruning, and repotting activities.

5. Care Statistics – Track the total number of recorded care activities by type.

6. Plant Collections – Create custom collections and organize plants into them.

7. Collection Management – View collection details, add plants, and delete collections.

## Technologies

- Python 3.14

- Django 6.1.3

- SQLite

- HTML5

- CSS3

## Installation and Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/mhristovaa98/plantify.git
   ```

2. Navigate to the project directory:

   ```bash
   cd plantify
   ```

3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment:

   **macOS / Linux:**
   ```bash
   source .venv/bin/activate
   ```

   **Windows:**
   ```bash
   .venv\Scripts\activate
   ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```


## Accessing the application

- After starting the development server, open:

http://127.0.0.1:8000/
