# SQL Analysis

This folder is where I'll keep the SQL queries for my Online Retail II project.

I'll use SQL alongside Python to explore the data, check for inconsistencies, and understand how the business is performing.

One of my main priorities is making sure the numbers are accurate. Before analysing revenue growth, I want to understand how sales, returns, and cancellations are recorded and how they affect the results.

## Planned SQL Queries

### 01 — Data Quality Checks
`01_data_quality.sql`

I'll begin by checking for missing customer IDs, duplicate records, negative quantities, unusual prices, and cancelled orders.

Not everything that looks unusual is necessarily an error. For example, a negative quantity could mean a customer returned an item.

I want to understand these differences before deciding how to handle the records.

### 02 — Data Reconciliation
`02_data_reconciliation.sql`

This part will help me check that the figures remain consistent as I prepare the data.

I'll compare the number of records, transactions, and calculated sales values before and after cleaning.

If something changes, I want to know what caused it and whether the difference makes sense.

### 03 — Sales Performance
`03_sales_performance.sql`

Here, I'll look at how sales performed over time.

I'll calculate monthly revenue, order volumes, and average order values to see when sales increased or declined.

I'll also compare different periods to identify trends that might be worth investigating.

### 04 — Customer and Product Analysis
`04_customer_product_analysis.sql`

I'll use these queries to understand which customers, products, and countries contribute most to sales.

Some of the questions I'll explore include:

- Which products generate the most revenue?
- Which customers spend the most?
- How frequently do customers place orders?
- Which countries account for the largest share of sales?
- How do returns affect sales performance?

I want to understand not just how much the business sells, but where that revenue comes from.

### 05 — Revenue Growth
`05_revenue_growth.sql`

This section will focus on understanding why revenue changes.

For example, if sales increase from one month to another, I'll investigate whether the growth came from more orders, higher spending, or stronger performance in certain products or countries.

The aim is to identify the factors behind the numbers rather than simply reporting percentage changes.

## How I'll Document My Work

I'll keep the SQL queries organised and explain what each one is trying to answer.

I'll also document the assumptions I make, especially when dealing with returns, cancellations, missing customer information, and revenue calculations.

Where it makes sense, I'll compare the results with my Python analysis to check that both approaches produce consistent figures.

## Tools and Techniques

I plan to use **SQLite** to run the queries, with Python and SQLAlchemy to help prepare and access the data.

As the project develops, I'll practise SQL techniques such as joins, aggregations, common table expressions (CTEs), window functions, and comparisons across different periods.

## Project Status

**In progress**

I'll add the SQL files as I work through the project, starting with data quality checks and reconciliation.

My goal is to build a set of queries that are easy to understand, reliable, and useful for answering real business questions.
