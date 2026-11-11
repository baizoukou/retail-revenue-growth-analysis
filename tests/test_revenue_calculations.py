"""Tests for retail revenue and growth calculations."""

import pandas as pd
import pytest


def test_positive_transaction_value():
    quantity = 4
    price = 12.50

    line_value = quantity * price

    assert line_value == pytest.approx(50.00)


def test_cancellation_transaction_value():
    quantity = -2
    price = 15.00

    line_value = quantity * price

    assert line_value == pytest.approx(-30.00)


def test_net_revenue_includes_cancellations():
    transactions = pd.DataFrame({
        "Quantity": [3, 2, -1],
        "Price": [10.00, 20.00, 10.00],
    })

    transactions["LineValue"] = (
        transactions["Quantity"] * transactions["Price"]
    )

    assert transactions["LineValue"].sum() == pytest.approx(60.00)


def test_revenue_growth_percentage():
    august_revenue = 800.00
    november_revenue = 1200.00

    growth_pct = (
        (november_revenue - august_revenue)
        / august_revenue
    ) * 100

    assert growth_pct == pytest.approx(50.00)


def test_symmetric_growth_decomposition():
    old_units = 100
    new_units = 120

    old_unit_value = 10.00
    new_unit_value = 12.00

    old_sales = old_units * old_unit_value
    new_sales = new_units * new_unit_value

    volume_effect = (
        (new_units - old_units)
        * (old_unit_value + new_unit_value) / 2
    )

    unit_value_effect = (
        (new_unit_value - old_unit_value)
        * (old_units + new_units) / 2
    )

    assert volume_effect == pytest.approx(220.00)
    assert unit_value_effect == pytest.approx(220.00)

    assert (
        volume_effect + unit_value_effect
        == pytest.approx(new_sales - old_sales)
    )


def test_product_revenue_reconciliation():
    transactions = pd.DataFrame({
        "StockCode": ["A", "A", "B", "B"],
        "Quantity": [2, 3, 1, 4],
        "Price": [10.00, 10.00, 20.00, 20.00],
    })

    transactions["LineValue"] = (
        transactions["Quantity"] * transactions["Price"]
    )

    product_revenue = (
        transactions.groupby("StockCode")["LineValue"]
        .sum()
    )

    assert product_revenue["A"] == pytest.approx(50.00)
    assert product_revenue["B"] == pytest.approx(100.00)

    assert product_revenue.sum() == pytest.approx(
        transactions["LineValue"].sum()
    )
