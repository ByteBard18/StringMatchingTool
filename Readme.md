
# 🌟 String Matching Tool

  

## Project Overview 📑

  

The **String Matching Tool** is a web application designed to allow users to search across multiple `.txt` documents simultaneously. The tool utilizes two powerful algorithms:

  

- ⚡ **BM25 Algorithm**: Used for document relevancy ranking based on the search query.

- 🔍 **Boyer-Moore Algorithm**: Efficient for fast string searching to detect lines containing the queried term.

  

The application is built using a **React frontend** and a **Django backend**, effectively leveraging modern data structures such as **Stacks** to detect and store relevant lines in documents.

  

## Features ✨

  

- 📄 Simultaneous search across multiple `.txt` documents.

- 📈 **BM25 Algorithm** for document relevancy ranking.

- 🧠 **Boyer-Moore Algorithm** for efficient string searching.

- 💡 Data structures like **Stacks** used for results formatting and optimization.

- 🖥️ Easy-to-use web interface for uploading documents and querying search terms.

- 🗣️ Search terms can include **phrases** as well.

  

>  **Note**:

>  - 📁 Currently, only up to **5 files** can be uploaded at a time, and all files must be in `.txt` format.

>  - 🗂️ All uploaded files are stored in the `media/` folder of the Django server.

  

## Tech Stack 🛠️

  

-  **Frontend**: React.js ⚛️

-  **Backend**: Django (Python) 🐍

-  **Search Algorithms**: BM25 (document relevancy) 📊, Boyer-Moore (string searching) 🔍

-  **Data Structures**: Stacks 🏗️

-  **File Handling**: Support for `.txt` files only 📄 (up to 5 files at once)

  

## System Architecture 🏗️

  

1.  **Frontend (React)**: Users can upload `.txt` files and input search queries.

2.  **Backend (Django)**: Manages the search operations using the BM25 and Boyer-Moore algorithms, and returns the lines of text where the search term appears.

  

## Key Algorithms 🔑

  

### BM25 (Best Matching 25) 🧠

  

The BM25 algorithm is used to evaluate the relevance of a document to a given query by:

  

- Calculating term frequency and inverse document frequency.

- Ranking documents based on their relevance scores.

  

Here is the Algorithm Library referred to while developing this project: [BM25 ALGORITHM](https://github.com/dorianbrown/rank_bm25)

  

### Boyer-Moore Algorithm ⚡

  

The Boyer-Moore algorithm is a string searching technique that skips sections of the text where the search term cannot possibly match. Its efficiency makes it suitable for large documents.

Learn more about the algorithm here: [Boyer Moore Algorithm for Pattern Searching - GeeksforGeeks](https://www.geeksforgeeks.org/boyer-moore-algorithm-for-pattern-searching/)

  

## Setup Instructions 🛠️

  

Follow these steps to set up and run the project on your local machine.

  

### Prerequisites 📋

  

Make sure you have the following installed on your machine:

  

- ⚛️ Node.js and npm

- 🐍 Python 3.x and pip

- 🖥️ Django

- 🔄 Virtualenv (recommended for Django)

  

### 1. Clone the Repository 💻

  

```bash

git clone https://github.com/ByteBard18/StringMatchingTool.git

cd string-matching-tool

```

### 2. Frontend Setup (REACT-VITE) 🚀

```bash

cd frontend

npm install

```

### 3. Backend Setup (DJANGO) 🛠️

```bash

cd ../backend

pip install -r requirements.txt  # Install all the dependencies

```

### 4. Creating Superuser for Admin Access 🧑‍💻

```bash

python manage.py createsuperuser

```

You will be prompted to enter a username, email, and password for the admin account.

Once the superuser is created, you can access the Django admin panel by navigating to http://localhost:8000/admin/.

  

### 5. Running the Application 🏃‍♂️

Run the Django Backend 🚀

Navigate to the backend directory.

Apply migrations and start the Django development server.

```bash

python manage.py migrate

python manage.py runserver

```

By default, this will start the backend on http://localhost:8000/.

  

Run the React Frontend ⚛️

In another terminal, navigate to the frontend directory and run the React app:

```bash

cd frontend

npm run dev

```

This will start the React development server on http://localhost:5173/.

  

### 6. Testing the Application 🧪

Open your browser and go to http://localhost:5173/ to interact with the frontend. You can now upload .txt files (up to 5 at a time) and start querying search terms, including phrases. The React frontend communicates with the Django backend to process the search.

  

## Folder Structure 🗂️

```bash

string-matching-tool/

├──  docs/

├──  frontend/  # React frontend

│  ├──  public/

│  ├──  src/

│  └──  package.json

│

├──  StringMatchingTool/  # Django backend

│  ├──  StringMatchingTool/  #project

| ├──  search_handler/  #app

│  ├──  media/  # Directory where uploaded files are stored

│  ├──  manage.py

│  └──  requirements.txt

│

└──  README.md  # Project documentation

```

## Future Enhancements 🚀

Handling Larger Datasets: Scaling with more efficient indexing and storage mechanisms such as Elasticsearch for faster retrieval.

Support for More File Types: Adding support for PDFs and Word documents.

Improved UX: Incorporating advanced filtering options and fuzzy search capabilities for better user experience.

Machine Learning Integration: Using NLP models for better relevancy ranking beyond BM25.

## Contributing 🤝

Feel free to submit issues or pull requests if you want to contribute to the project. Contributions are always welcome!
