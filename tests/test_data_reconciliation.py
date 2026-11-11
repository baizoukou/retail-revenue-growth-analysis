"""Independent revenue reconciliation tests."""

import pandas as pd
import pytest


@pytest.fixture
def transactions():
    data = pd.DataFrame({
        "Invoice": [
            "1001", "1001", "1002",
            "C1003", "1004", "1005"
        ],
        "StockCode": [
            "A", "B", "A", "A", "B", "A"
        ],
        "Country": [
            "United Kingdom", "United Kingdom",
            "France", "United Kingdom",
            "France", "United Kingdom"
        ],
        "Month": [
            "2010-09", "2010-09", "2010-09",
            "2010-09", "2010-11", "2010-11"
        ],
        "Quantity": [2, 3, 1, -1, 4, 2],
        "Price": [10, 20, 10, 10, 20, 10],
    })

    data["LineValue"] = data["Quantity"] * data["Price"]
    return data


def test_transaction_total(transactions):
    assert transactions["LineValue"].sum() == pytest.approx(180)


def test_monthly_reconciliation(transactions):
    monthly = transactions.groupby("Month")["LineValue"].sum()

    assert monthly["2010-09"] == pytest.approx(80)
    assert monthly["2010-11"] == pytest.approx(100)
    assert monthly.sum() == pytest.approx(
        transactions["LineValue"].sum()
    )


def test_product_reconciliation(transactions):
    products = transactions.groupby("StockCode")["LineValue"].sum()

    assert products["A"] == pytest.approx(40)
    assert products["B"] == pytest.approx(140)
    assert products.sum() == pytest.approx(
        transactions["LineValue"].sum()
    )


def test_country_reconciliation(transactions):
    countries = transactions.groupby("Country")["LineValue"].sum()

    assert countries["United Kingdom"] == pytest.approx(90)
    assert countries["France"] == pytest.approx(90)
    assert countries.sum() == pytest.approx(
        transactions["LineValue"].sum()
    )


def test_gross_cancellations_net_reconciliation(transactions):
    gross = transactions.loc[
        transactions["Quantity"] > 0, "LineValue"
    ].sum()

    cancellations = transactions.loc[
        transactions["Quantity"] < 0, "LineValue"
    ].sum()

    net = transactions["LineValue"].sum()

    assert gross == pytest.approx(190)
    assert cancellations == pytest.approx(-10)
    assert net == pytest.approx(gross + cancellations)
