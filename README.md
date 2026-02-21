# Simple-Open-Library-Api-Project
This project fetches book data from the OpenLibrary API,
filters books published after the year 2000,
and exports the cleaned results into a structured CSV file.


## Features

- Fetches 50 books from OpenLibrary API
- Filters books published after 2000
- Exports results to CSV
- Clean and modular-ready Python structure
- Basic error handling


## Tech Stack

- Python 3.15.5
- requests
- csv (standard library)


## Installation

```bash
git clone <https://github.com/DM-Haider/Simple-Open-Library-Api-Project.git>
cd Simple-Open-Library-Api-Project
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

---



## Project Structure
├── main.py
├── books_after_2000.csv
├── requirements.txt
└── README.md
