# Leveraging Data to Enforce Short-Term Rental Rules

## Introduction:
In response to Vancouver's housing affordability crisis, regulations now require Airbnb hosts to live on the property they rent out. To enforce these rules, I've developed a data-driven approach using Airbnb data.

## Summary of Approach:
I collected data from 300 Vancouver Airbnb listings, including property details and host information. Code relies on rapidAPI API from here: https://rapidapi.com/3b-data-3b-data-default/api/airbnb13 .
Free quota is 100 requests per month. 300 Vancouver Airbnb listings were 10 requests.

Challenges with license number extraction: missing data and unstructured data. For example, 'Lic# 23-031530', 'Registration number</b><br />24-158811', 'BUSINESS LICENCE NO: 00462568', 'City of Richmond Business License#: 24 008865'

Suggestion: to extract license number with LLM Gemini 1.5 Flash. See examples here [notebooks/license_number_extraction_gemini.ipynb](notebooks/license_number_extraction_gemini.ipynb)

## Key Insights:

1. License Verification: We'll cross-reference license numbers with the government database to ensure compliance.

2. Identifying Non-Resident Hosts: We'll flag hosts with multiple listings, suggesting they may not live on all properties.


## Future Extensions:

1. Expanding to Other BC Cities: Apply our method province-wide for broader insights.
2. Advanced Analysis: Use machine learning to improve accuracy.
3. Integrating More Data: Include property ownership records for a comprehensive view.

## Conclusion:
By using data analytics, we aim to improve enforcement of short-term rental rules, supporting Vancouver's housing affordability goals.

## Setup

To install dependencies:

```
poetry install
```

Activate poetry environment:
```
poetry shell
```

Get API key here: https://rapidapi.com/3b-data-3b-data-default/api/airbnb13

Add RAPIDAPI_KEY="your key" to `.env` file

To dump Airbnb listings info and get `data/airbnb_results.csv` file run:

```
python dump.py
```

To scrape Airbnb listings description (including license number) and get `data/listing_descriptions.jsonl` file run:
```
python scrap_listing_description.py
```

## Demo

See how to dump Airbnb data with rapid API: [notebooks/rapid_api_search_by_location.ipynb](notebooks/rapid_api_search_by_location.ipynb)

See how dumped Airbnb data look like [notebooks/data_insights.ipynb](notebooks/data_insights.ipynb)

See how scraped Airbnb listing Id and description look like [data/listing_descriptions.jsonl](data/listing_descriptions.jsonl)

See how to extract license number from Airbnb description with Gemini 1.5 Flash (free version) [notebooks/license_number_extraction_gemini.ipynb](notebooks/license_number_extraction_gemini.ipynb)
