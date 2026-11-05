# Retail Revenue & Growth Driver Analysis

**Python | SQL | Data Cleaning | Exploratory Data Analysis | Business Intelligence**

## Executive Summary

What is driving sales growth, and how can a business use its data to make better decisions?

This is the main question I wanted to explore in this project.

Using the **UCI Online Retail II dataset**, which contains approximately 1.07 million transaction records from a UK-based online retailer between 2009 and 2011, I set out to understand how sales changed over time, which customers, products, and markets contributed to those changes, and what the findings could mean for the business.

My initial analysis of the 2009–2010 data revealed a **59.1% increase in positive transaction value between September and November 2010**. The UK accounted for approximately **92% of this growth**, with Christmas decorations and winter-related products among the notable contributors.

These early findings suggest that seasonal demand may have played an important role. However, further analysis is needed to understand how much of the increase came from customer activity, purchasing behaviour, and changes in product demand.

The project is still in progress, and these findings will be reviewed as part of the full two-year analysis.

## Business Problem

An increase in sales is encouraging, but it does not tell the whole story.

For a retailer, understanding why sales are increasing or decreasing is just as important as knowing the numbers. Growth might come from new customers, repeat purchases, seasonal demand, or changes in the products people buy.

At the same time, missing customer information, cancelled orders, and inconsistent transaction records can make it difficult to measure performance accurately.

Through this project, I want to answer three main questions:

- **What changed?** How did sales, transactions, and customer activity evolve over time?
- **What drove the change?** Which products, customers, and countries contributed most to sales growth?
- **What should the business do next?** Which findings could help improve inventory planning, customer retention, and business performance?

## Project Objectives

My goal is to turn raw transaction data into meaningful business insights.

To achieve this, I will:

1. Examine the dataset to identify missing values, duplicates, and inconsistencies.
2. Investigate cancelled orders, returns, and their impact on reported sales.
3. Analyse monthly sales patterns and identify periods of growth or decline.
4. Explore which countries, products, and customer groups contribute most to revenue.
5. Investigate possible explanations for changes in sales performance.
6. Develop practical recommendations supported by the data.

## My Approach

### 1. Data Cleaning and Quality Checks

Before analysing sales performance, I need to understand how reliable the data is.

I will examine missing customer IDs, duplicate-looking transactions, negative quantities, cancelled invoices, and unusual product prices.

Rather than removing every unusual record, I will investigate what it represents. For example, a negative quantity may indicate a returned product rather than a data entry error.

The aim is to preserve useful business information while making the data more reliable for analysis.

### 2. Exploratory Data Analysis (EDA)

Once the data has been assessed and prepared, I will explore the main patterns in sales and customer activity.

This includes looking at monthly transaction values, order activity, popular products, customer purchasing behaviour, and differences between countries.

I will also investigate whether changes in sales are linked to seasonal patterns or shifts in purchasing activity.

### 3. Growth Driver Analysis

This is where I want to go beyond describing what happened and start understanding why.

I will compare performance across different periods and break down sales changes by country, product, and customer segment.

I also plan to investigate whether growth comes mainly from more orders, larger quantities purchased, or changes in average selling prices and product mix.

### 4. Data Visualisation

I will use charts to make the findings easier to understand and communicate.

The visualisations will focus on:

- Monthly sales trends and growth rates.
- Products and countries contributing most to growth.
- Customer purchasing patterns.
- Returns, cancellations, and data quality issues.
- Differences between expected and actual performance where appropriate.

### 5. Business Recommendations

The final stage will focus on what the findings mean for the retailer.

Rather than making recommendations based only on sales figures, I will consider the evidence, its limitations, and the potential business impact.

The aim is to identify realistic opportunities to improve inventory planning, understand customer behaviour, and support better business decisions.

## Tools and Technologies

- **Python and Pandas:** Data cleaning, transformation, and analysis.
- **SQL and SQLite:** Data querying, validation, and reconciliation.
- **Matplotlib:** Creating charts to explore and communicate trends.
- **Jupyter Notebook:** Documenting the analysis, code, and findings.

## Initial Findings

The first stage of the analysis has highlighted several areas worth investigating further.

**Sales growth:** Positive transaction value increased by approximately 59.1% between September and November 2010.

**Geographic contribution:** The UK accounted for around 92% of the increase, suggesting that domestic sales were the main contributor.

**Product demand:** Christmas decorations and winter-related products were among the notable growth contributors, pointing towards a possible seasonal effect.

**Data quality:** Missing customer identifiers, returns, cancellations, and non-product charges need to be handled carefully to avoid misleading conclusions.

These are preliminary observations rather than final conclusions.

## Limitations

There are several limitations to consider when interpreting the results.

The dataset covers historical transactions from 2009 to 2011, so the findings may not reflect current retail behaviour.

Some customer IDs are missing, which limits customer-level analysis. The dataset also does not provide complete information about marketing campaigns, product costs, inventory availability, or competitor activity.

As a result, I can identify patterns and possible explanations, but I cannot always establish exactly what caused a change in sales.

The full two-year reconciliation is also still outstanding.

## Data Source

**UCI Machine Learning Repository — Online Retail II**

https://archive.ics.uci.edu/dataset/502/online+retail

## Project Status

**In progress**

I have completed an initial review of the data and explored some of the main sales trends and growth contributors.

The next steps are to complete the data quality checks, reconcile the full two-year dataset, investigate customer behaviour in more detail, and validate the business recommendations.

## What's Next?

Once the exploratory analysis is complete, I plan to extend the project into **retail demand forecasting**.

This will involve experimenting with Machine Learning models such as LightGBM and XGBoost to predict future product demand.

I also intend to explore MLflow for experiment tracking and model monitoring.

The longer-term goal is to build on the analytical work and understand how predictive models can support real business planning decisions.
