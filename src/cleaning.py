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


def refine_revenue_classifications(df: pd.DataFrame) -> pd.DataFrame:
    """Apply the final revenue classification refinements.

    Reproduces the special-stock-code rules from notebook
    01_data_quality.ipynb, cells 110 and 115.

    Expects a DataFrame already classified by
    classify_revenue_transactions().
    Returns a new DataFrame without modifying the input.
    """
    result = df.copy()

    stock = (
        result["StockCode"]
        .astype("string")
        .str.upper()
        .str.strip()
    )

    # Cell 110: initial special-code refinements
    special_categories = {
        "POST": "Postage / delivery",
        "D": "Discount",
        "S": "Samples / Review",
        "ADJUST": "Accounting adjustment",
        "AMAZONFEE": "Marketplace fee",
    }

    for code, category in special_categories.items():
        result.loc[
            stock.eq(code).fillna(False),
            "RevenueCategory"
        ] = category

    # Cell 115: final refinements
    result.loc[
        stock.isin(["POST", "DOT", "C2"]).fillna(False),
        "RevenueCategory"
    ] = "Postage / delivery"

    result.loc[
        stock.eq("BANK CHARGES").fillna(False),
        "RevenueCategory"
    ] = "Bank charges"

    result.loc[
        stock.isin(["ADJUST", "ADJUST2"]).fillna(False),
        "RevenueCategory"
    ] = "Accounting adjustment"

    result.loc[
        stock.str.startswith("GIFT_0001_", na=False),
        "RevenueCategory"
    ] = "Gift voucher / Review"

    return result
