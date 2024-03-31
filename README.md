
# LinkedIn Job Scraper

This project provides a Python script to automate searching for jobs on LinkedIn and scraping relevant data into a JSON file.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#insatllation)
- [Usage](#usage)
- [Video Demonstration](#video-demonstration)
- [Addtional Notes](#additional-notes)

## Features

* Conducts job searches on LinkedIn based on user-specified keywords and city.
* Extracts essential job details (title, company name, location, and URL) from search results.
* Saves scraped data in a well-formatted JSON file.

## Requirements

* Python 3 (tested with 3.x)
* Selenium WebDriver [https://www.selenium.dev/documentation/](https://www.selenium.dev/documentation/)
* ChromeDriver (download the appropriate version for your OS from [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads))
* A JSON file named `config.json` containing your LinkedIn login credentials and desired search parameters:

```json
{
  "email": "your_linkedin_email",
  "password": "your_linkedin_password",
  "keyword": "your_desired_job_keyword",
  "city": "your_desired_city"
}
```

## Installation

1. Download and install ChromeDriver for your operating system.
2. Install the required Python libraries:

   ```bash
   pip install selenium
   ```

## Usage

1. Create a `config.json` file in the same directory as this script, filling in your LinkedIn credentials and search preferences.
2. Run the script:

   ```bash
   main.py  # Assuming the script is named main.py
   ```

## Output

* The script will display job details (title, company, location, URL) on the console during scraping.
* A JSON file named `python_job_applications.json` will be created in the same directory, containing the scraped data in a structured format.

## Video Demonstration

[Consider adding a link to your video demonstration here, if applicable. Uploading it to a platform like YouTube or Vimeo is recommended.]

## Additional Notes

* This script is for educational purposes only. Use it responsibly and in accordance with LinkedIn's terms of service.
* Consider adding error handling for potential issues during the scraping process.
* You may need to update the script for any significant changes in LinkedIn's website structure.



**Feel free to contribute or ask questions!**