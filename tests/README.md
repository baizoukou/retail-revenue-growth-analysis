# Data Validation and Testing

This folder is where I'll keep the tests for my Online Retail II project.

As I work through the data, I want to make sure my Python code works properly and that the numbers I'm using are accurate.

A mistake in how I clean the data or calculate revenue could affect the whole analysis. I'd rather catch these problems early than discover them after I've already created charts and written reports.

## Planned Tests

### 01 — Data Quality
`test_data_quality.py`

I'll start by checking the dataset for missing values, duplicate records, invalid dates, and unusual quantities or prices.

Some records might look incorrect at first but actually represent normal business activity. For example, a negative quantity could mean a customer returned an item.

I'll take this into account when writing the tests so I don't treat every unusual value as an error.

### 02 — Data Cleaning
`test_data_cleaning.py`

Once I start cleaning the data, I'll need to check that the changes are working as expected.

I'll test how my cleaning functions handle missing customer IDs, cancelled orders, returns, and other unusual transactions.

I also want to make sure I'm not accidentally removing valid records or changing information that should stay the same.

### 03 — Revenue Calculations
`test_revenue_calculations.py`

Since revenue is central to this project, I want to be confident that my calculations are correct.

I'll test transaction values, monthly revenue, average order values, and revenue growth percentages.

I'll also check how returns and cancellations affect the totals.

For example, if I update the way revenue is calculated, I want to know whether the change produces the results I expect.

### 04 — Data Reconciliation
`test_data_reconciliation.py`

This part will help me understand what happens to the data during cleaning.

I'll compare the number of records and transaction values before and after making changes.

If the totals are different, I want to be able to explain why.

I'll also compare some of my Python and SQL results to check whether both methods give me the same figures.

### 05 — Analysis
`test_analysis.py`

As I develop the analysis, I'll add tests for the functions I use to calculate business measures.

These might include customer purchase frequency, product revenue, order values, and sales growth.

I'll use small examples where I already know the correct answer. That way, I can check whether the code is doing what I intended.

## How I'll Test My Work

I'll use **pytest** to run the tests.

I'll begin with basic checks and add more as I develop the Python scripts.

I want the tests to be straightforward, with clear names and explanations of what they're checking.

The idea isn't to test everything at once. It's to build confidence in the analysis as I work through each stage.

## What I'll Be Checking

Some of the main questions I want my tests to answer are:

- Does the data contain the values and formats I expect?
- Am I handling missing information, returns, and cancellations correctly?
- Are my revenue calculations accurate?
- Can I explain any changes in the figures after cleaning?
- Do my Python and SQL calculations agree?
- Can I run the analysis again and get the same results?

I know that passing these tests won't automatically mean every conclusion is correct. However, they should help me spot mistakes and make the results more reliable.

## Project Status

**In progress**

I'll add the tests as I build the cleaning and analysis scripts, starting with data quality and revenue calculations.

I want testing to become a normal part of how I work on this project, rather than something I leave until everything else is finished.
