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
```
---
## Usage

Run the script:

```bash
python main.py

```
After execution, a CSV file will be generated:
```markdown
books_after_2000.csv
```


## Sample Output
Example structure of the generated CSV file:
```markdown

title,author,publish_year,edition_count  
Python Cookbook,David Beazley,2013,5  
Fluent Python,Luciano Ramalho,2015,3  

```

## Project Structure
Currently, the project is implemented in a single Python file (`main.py`) 
for simplicity. However, the code is structured in a way that allows 
easy modularization in the future. Functions are separated logically, 
making it straightforward to split into multiple modules if the project grows.

```bash
├── main.py
├── books_after_2000.csv
├── requirements.txt
└── README.md
