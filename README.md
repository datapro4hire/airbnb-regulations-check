# Leveraging Data to Enforce Short-Term Rental Rules

## Introduction:
In response to Vancouver's housing affordability crisis, regulations now require Airbnb hosts to live on the property they rent out. To enforce these rules, I've developed a data-driven approach using Airbnb data.

## Summary of Approach:
I collected data from 300 Vancouver Airbnb listings, including property details and host information. Code relies on rapidAPI API from here: https://rapidapi.com/3b-data-3b-data-default/api/airbnb13 .
Free quota is 100 requests per month. 300 Vancouver Airbnb listings were 10 requests.

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