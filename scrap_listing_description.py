import csv
import re
import requests
import json
import logging

# Setup logging
logging.basicConfig(
    filename='scrapy_log.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

DATA_FILENAME = 'data/airbnb_results.csv'
LISTINGS_DESCRIPTION_FILENAME = "data/listing_descriptions.jsonl"


def extract_html_text(listing_id):
    url = f"https://www.airbnb.ca/rooms/{listing_id}"
    response = requests.get(url)

    if response.status_code == 200:
        text = response.text

        # Use regex to find the 'htmlDescription' section in the text
        pattern = re.compile(r'"htmlDescription":\{.*?\}')
        match = pattern.search(text)

        if match:
            htmlDescription = match.group(0).replace('"htmlDescription":', '')

            # Use a non-greedy match to find the 'htmlText' value
            htmlTextPattern = re.compile(r'"htmlText":"(.*?)"')
            matchText = htmlTextPattern.search(htmlDescription)

            if matchText:
                htmlText = matchText.group(1)
                return htmlText
            else:
                logging.error(f"htmlText not found for listing ID: {listing_id}")
                return None
        else:
            logging.error(f"htmlDescription not found for listing ID: {listing_id}")
            return None
    else:
        logging.error(f"Failed to fetch URL for listing ID: {listing_id}")
        return None


# Read the CSV file and save results to a JSONL file
with open(DATA_FILENAME, 'r') as csvfile, open(LISTINGS_DESCRIPTION_FILENAME, 'w') as jsonlfile:
    reader = csv.DictReader(csvfile)
    total_ids = sum(1 for row in reader)
    csvfile.seek(0)  # Reset the reader to the beginning of the file
    reader = csv.DictReader(csvfile)

    for count, row in enumerate(reader, 1):
        listing_id = row['id']
        html_text = extract_html_text(listing_id)

        if html_text:
            result = {
                'id': listing_id,
                'description': html_text
            }
            jsonlfile.write(json.dumps(result) + '\n')

        logging.info(f"Processed listing ID: {listing_id} ({count}/{total_ids})")
        print(f"Processed listing ID: {listing_id} ({count}/{total_ids})")

print(f"Processing complete. Results saved to {LISTINGS_DESCRIPTION_FILENAME}")
