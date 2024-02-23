# Google Summer of Code Organizations Scraper

## Overview

---

This python program is designed to ease the process of shortlisting organizations and selecting from them for Google Summer of Code (GSoC) participation. It scrapes the links of GSoC organizations from a file named `links.txt` and extracts relevant data from their webpages. The extracted data is compiled into an Excel file for convenient review and analysis, aiding users in making informed decisions about which organizations to prioritize during the application process. 

## Prerequisites

---

* Python installed on your system. You can download Python from the official website: [Python Downloads](https://python.org/downloads/)
* A working version of Google Chrome installed on your computer, as the program utilizes Chrome for web scraping.

## Usage Instructions

---

1. **Clone the Repository:**
    - Clone this repository to your local machine using the following command:
      ```
      git clone https://github.com/mohamedbassem6/GSoC_Organizations_Scraper.git
      ```

2. **Navigate to the Directory:**
    - Open your terminal or command prompt and change directory to the cloned repository:
      ```
      cd GSoC_Organizations_Scraper
      ```

3. **Create a Virtual Environment:**
    - It's recommended to create a virtual environment to manage dependencies for this project. You can do this using the following command:
      ```
      python -m venv env
      ```

4. **Activate the Virtual Environment:**
    - Activate the virtual environment based on your operating system:
      - On Windows:
        ```
        .\env\Scripts\activate
        ```
      - On macOS and Linux:
        ```
        source env/bin/activate
        ```

5. **Install Dependencies:**
    - With the virtual environment activated, install the required Python dependencies using pip:
      ```
      pip install -r requirements.txt
      ```

6. **Update `links.txt`:**
    - Open the `links.txt` file using a text editor of your choice.
    - Add the URLs of the Google Summer of Code organization webpages, each on a new line. These are the pages from which the program will scrape data.
    - Save and close the `links.txt` file.

7. **Run the Script:**
    - Run the `script.py` file using Python:
      ```
      python script.py
      ```

8. **Accessing Output:**
    - After the script finishes execution, you will find the output folder in the same directory as the cloned repository.
    - Inside the output folder, you will find the Excel file named `GSoC_Shortlist.xlsx` containing the data of GSoC organizations.

9. **Deactivate the Virtual Environment:**
    - Once you're done using the program, deactivate the virtual environment to return to your system's default Python environment:
      ```
      deactivate
      ```

## Notes

---

- Ensure that the `links.txt` file contains valid URLs of the GSoC organization webpages.
- Add the links of each organization you're interested in to `links.txt` file so that the program can scrape the relevant data.
- The script utilizes Google Chrome for web scraping, so ensure it's correctly installed and configured on your system.
- Depending on the number of organizations and the internet speed, the scraping process might take some time.
