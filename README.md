# Quarterly-Assessment

# Quiz Bowl Application

This repository contains a Quiz Bowl application implemented in Python. The application allows users to play a quiz game by selecting a category and answering questions.

## Files in the Repository

### 1. Database file (quiz_bowl_db.sql)

- **Purpose:** Contains the SQLite database structure and tables for storing quiz questions and answers.
- **Content:**
  - Defines tables for each category (e.g., StrategicManagement, DigitalMarketing) with columns for question text and correct answer.
- **Usage:**
  - Execute this file to create the database structure with predefined tables.

### 2. Create file (populate_db.py)

- **Purpose:** Populates the database with questions and answers.
- **Content:**
  - Provides functions to populate tables with data.
  - Uses placeholder data or generative AI to create questions and answers.
- **Usage:**
  - Execute this file to insert questions and answers into the database tables.

### 3. Read file (read_db.py)

- **Purpose:** Provides functions to retrieve data from the database.
- **Content:**
  - Contains functions to fetch table names and data from tables in the database.
- **Usage:**
  - Import functions from this file to retrieve table names and data in other modules.

### 4. App file (quiz_bowl.py)

- **Purpose:** Main application file where users can play the Quiz Bowl game.
- **Content:**
  - Implements the main logic for the Quiz Bowl game.
  - Allows users to select a category, display questions, accept user input for answers, and provide feedback on correctness.
- **Usage:**
  - Run this file to start the Quiz Bowl application.

### 5. README.md

- **Purpose:** Provides an overview of the repository and explanations for each file.
- **Content:**
  - Describes the purpose and usage of each file in the repository.
  - Includes instructions on running the Quiz Bowl application.
- **Usage:**
  - Refer to this file for information on the repository and its contents.

## Running the Application

To run the Quiz Bowl application:
1. Execute the `quiz_bowl.py` file.
2. Follow the on-screen prompts to select a category and answer questions.

Ensure you have the required Python libraries installed to run the application.

