# CVE Data Extraction and Analysis Using NLP

An automated system for extracting, processing, and analyzing Common Vulnerabilities and Exposures (CVE) data using Natural Language Processing (NLP). The application enables security professionals to search, view, and retrieve insights on vulnerabilities for enhanced security analysis.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Workflow](#workflow)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Deployment](#deployment)
- [Demo and Links](#demo-and-links)
- [Contributing](#contributing)

## Project Overview
This project automates the extraction and classification of CVE entries by leveraging NLP. It processes essential fields like CVE ID, description, CVSS score, published date, and vulnerability status to create an organized dataset. Data is then stored for efficient retrieval and similarity search, helping cybersecurity professionals quickly identify similar vulnerabilities.

## Features
- *Automated CVE Data Extraction:* Collects data from repositories, processes JSON files, and extracts relevant information.
- *Text Preprocessing and Standardization:* Cleans, formats, and standardizes key text fields (e.g., CVE IDs and descriptions) for consistent analysis.
- *Similarity Search Using FAISS:* Embeds descriptions using Sentence Transformers and indexes them with FAISS for fast similarity searches.
- *SQLite Integration:* Stores processed CVE data in SQLite for efficient querying and retrieval.
- *Web Interface with Flask:* Allows users to search for CVE information via a simple web form.

## Workflow

### 1. Data Collection and Extraction
   - Clone the GitHub repository containing CVE data and scripts.
   - Extract data in JSON format and parse necessary fields (CVE ID, description, CVSS score, etc.).
   - Save extracted data to a CSV file for processing.

### 2. Data Preprocessing
   - *Text Cleaning:* Remove noise, special characters, and stopwords, apply lemmatization or stemming.
   - *Field Standardization:* Normalize CVE ID and Source Identifier formats.
   - *Data Conversion:* Convert CVSS scores to numeric values, and dates to a datetime format.
   - *Data Cleanup:* Remove rows missing critical information and save processed data to CSV.

### 3. Storing and Retrieving Data
   - *Embedding Descriptions:* Use Sentence Transformers to generate vector embeddings for CVE descriptions.
   - *Similarity Search with FAISS:* Create a FAISS index for efficient retrieval of similar CVE entries.
   - *SQLite Database Setup:* Store the CVE data in an SQLite database, allowing for SQL-based querying.

### 4. Deployment on Render
   - Develop a Flask application to create a web interface for CVE data search.
   - Deploy the app on Render with automatic database unzipping, SSL setup, and containerized hosting.

## Installation and Setup

1. *Clone the Repository:*
   ```bash
   git clone https://github.com/Abhishek1234567899/NPL_PROJECT 
