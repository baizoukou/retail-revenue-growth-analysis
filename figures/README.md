# Data Visualisations

This folder is where I'll save the charts I create while analysing the Online Retail II dataset.

I want to use visualisations to better understand the data and explain my findings in a way that's easy to follow.

Rather than creating charts for the sake of it, I'll focus on what each chart tells me about the business and whether it helps answer a specific question.

## Planned Visualisations

### 01 — Sales Trends

I'll start by looking at how revenue changes from month to month.

I want to see when sales increase or decrease and whether there are any seasonal patterns.

For example, if revenue rises towards Christmas, I'll look more closely at which products or customer groups contributed to that growth.

### 02 — Product Performance

I'll compare products based on the revenue they generate and the quantities sold.

I'm interested in finding out whether a small group of products accounts for most sales or whether revenue is spread more evenly across the product range.

I'll also look for products whose performance changes over time.

### 03 — Customer Behaviour

Here, I'll explore how customers shop, how often they place orders, and how much they spend.

One question I'd like to answer is whether the business relies more on repeat customers or occasional buyers.

Since some transactions don't have customer IDs, I'll also consider how this affects the analysis.

### 04 — Sales by Country

I'll compare revenue across countries to understand where most sales come from.

I'll also look at how performance changes over time. A country generating high revenue doesn't necessarily mean it's growing quickly, so I'll try to distinguish between the two.

### 05 — Returns and Cancellations

I'll create charts to understand how often products are returned or orders are cancelled.

I want to see whether certain products or periods have more returns than others and how these transactions affect revenue.

This should help me build a more accurate picture of sales performance.

### 06 — Revenue Growth Drivers

This is where I'll bring the different parts of the analysis together.

If revenue increases or decreases, I want to understand what contributed to that change.

I'll look at the impact of different products, countries, and customer groups. I'll also explore whether changes in order volumes or average order values help explain the results.

## Tools and Approach

I'll mainly use **Matplotlib and Seaborn** in Python to create the charts.

I'll keep the visualisations simple, with clear titles, labelled axes, and consistent formatting.

I'll also check that the numbers shown in the charts match my Python and SQL calculations.

If there are limitations in the data or assumptions behind a calculation, I'll explain them rather than present the results as certain.

## File Organisation

I'll give each chart a descriptive filename so it's easy to find and reuse in my reports.

Some examples of the files I plan to create are:

- `monthly_revenue_trend.png`
- `top_products_by_revenue.png`
- `customer_purchase_frequency.png`
- `revenue_by_country.png`
- `monthly_returns_trend.png`
- `revenue_growth_contributors.png`

These filenames may change depending on what I discover during the analysis.

## Project Status

**In progress**

I'll add the charts as I work through the notebooks and complete each stage of the project.

My aim is to make sure every visualisation adds something useful to the analysis and helps explain the business findings clearly.
