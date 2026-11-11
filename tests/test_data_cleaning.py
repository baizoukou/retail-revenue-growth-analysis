"""Tests for the reusable revenue classification function."""

import pandas as pd
import pytest

from src.cleaning import classify_revenue_transactions


@pytest.fixture
def sample_transactions():
    return pd.DataFrame({
        "Invoice": [
            "1001", "C1002", "1003", "1004",
            "1005", "1006", "1007", "C1008",
            "1009", None
        ],
        "StockCode": [
            "12345", "12345", "12345", "12345",
            "DOT", "M", "B", "TEST001",
            "12345", "12345"
        ],
        "Description": [
            "Product A", "Product A", "Product A",
            "Product A", "DOTCOM POSTAGE",
            "Manual transaction", "Adjust bad debt",
            "Test product", "Product A", None
        ],
        "Quantity": [
            2, -1, 1, -2, 1, 1, 1, -1, 0, 1
        ],
        "Price": [
            10, 10, 0, 0, 5, 5, -100, 10, 10, 10
        ],
    })


def test_revenue_categories(sample_transactions):
    result = classify_revenue_transactions(sample_transactions)

    expected = [
        "Merchandise sale candidate",
        "Merchandise cancellation candidate",
        "Zero-price positive transaction",
        "Zero-price negative adjustment",
        "Postage / delivery",
        "Manual transaction",
        "Bad debt adjustment",
        "Test transaction",
        "Other / Review",
        "Merchandise sale candidate",
    ]

    assert result["RevenueCategory"].tolist() == expected


def test_test_transaction_overrides_cancellation(sample_transactions):
    result = classify_revenue_transactions(sample_transactions)

    assert result.loc[7, "RevenueCategory"] == "Test transaction"


def test_original_dataframe_unchanged(sample_transactions):
    original = sample_transactions.copy(deep=True)

    classify_revenue_transactions(sample_transactions)

    pd.testing.assert_frame_equal(sample_transactions, original)


def test_row_count_preserved(sample_transactions):
    result = classify_revenue_transactions(sample_transactions)

    assert len(result) == len(sample_transactions)


def test_no_missing_classifications(sample_transactions):
    result = classify_revenue_transactions(sample_transactions)

    assert result["RevenueCategory"].notna().all()


def test_missing_description_handled(sample_transactions):
    result = classify_revenue_transactions(sample_transactions)

    assert result.loc[9, "RevenueCategory"] == (
        "Merchandise sale candidate"
    )
