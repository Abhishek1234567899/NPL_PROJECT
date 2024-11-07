import sqlite3
import os
import zipfile
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Path to the zip file
ZIP_FILE_PATH = 'cve_data.zip'

# Function to unzip the database file if not already extracted
def unzip_db():
    # Check if the database file exists. If not, unzip it.
    if not os.path.exists('cve_data.db'):
        with zipfile.ZipFile(ZIP_FILE_PATH, 'r') as zip_ref:
            zip_ref.extractall()  # Extract to the current directory

# Connect to the SQLite database
def get_db_connection():
    unzip_db()  # Ensure database is unzipped before connecting
    conn = sqlite3.connect('cve_data.db')  # Connect to the unzipped DB
    conn.row_factory = sqlite3.Row  # Allows accessing columns by name
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    cve_id = request.form['cve_id']
    cve_data = search_cve(cve_id)
    
    if isinstance(cve_data, str):  # In case no result is found (string message)
        return render_template('search_result.html', message=cve_data)
    else:
        # Convert the dataframe to HTML and pass it to the template
        return render_template('search_result.html', cve_data=cve_data.to_html(index=False))

def search_cve(cve_id):
    cve_id = cve_id.strip().upper()  # Convert input to uppercase
    
    # Define the query to fetch data
    query = '''SELECT "CVE ID", "Source Identifier", "Published Date", "Last Modified Date", 
               "Vulnerability Status","Description", "CVSS Score", "Weaknesses", "Configuration", 
               "reference_links", "Category" 
               FROM cve_info WHERE "CVE ID" = ?'''
    
    conn = get_db_connection()
    cve_data = pd.read_sql(query, conn, params=(cve_id,))
    conn.close()
    
    if cve_data.empty:
        return f"No CVE found with the ID: {cve_id}"
    else:
        return cve_data

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
