"""Reusable transaction classification functions."""

import pandas as pd


def classify_revenue_transactions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Reproduce the initial revenue classification from
    notebook 01_data_quality.ipynb, cell 101.

    Returns a classified copy without modifying the input.
    """

    result = df.copy()
    result["RevenueCategory"] = "Other / Review"

    invoice = result["Invoice"].astype("string").str.upper()
    stock = (
        result["StockCode"]
        .astype("string")
        .str.upper()
        .str.strip()
    )
    description = (
        result["Description"]
        .astype("string")
        .str.strip()
    )

    cancelled = invoice.str.startswith("C", na=False)
    positive_qty = result["Quantity"] > 0
    negative_qty = result["Quantity"] < 0
    positive_price = result["Price"] > 0
    zero_price = result["Price"] == 0

    result.loc[
        positive_qty & positive_price & ~cancelled,
        "RevenueCategory"
    ] = "Merchandise sale candidate"

    result.loc[
        negative_qty & positive_price & cancelled,
        "RevenueCategory"
    ] = "Merchandise cancellation candidate"

    result.loc[
        positive_qty & zero_price,
        "RevenueCategory"
    ] = "Zero-price positive transaction"

    result.loc[
        negative_qty & zero_price,
        "RevenueCategory"
    ] = "Zero-price negative adjustment"

    result.loc[
        stock.eq("DOT") | description.str.fullmatch(
            r"(?i)DOTCOM POSTAGE", na=False
        ),
        "RevenueCategory"
    ] = "Postage / delivery"

    result.loc[
        stock.eq("M"),
        "RevenueCategory"
    ] = "Manual transaction"

    result.loc[
        stock.eq("B") & description.str.contains(
            "bad debt", case=False, na=False
        ),
        "RevenueCategory"
    ] = "Bad debt adjustment"

    result.loc[
        stock.eq("TEST001"),
        "RevenueCategory"
    ] = "Test transaction"

    return result
