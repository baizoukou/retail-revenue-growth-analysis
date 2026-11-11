"""Regression tests for the original revenue classification baseline."""

from pathlib import Path

import pandas as pd
import pytest

from src.cleaning import classify_revenue_transactions


DATA_PATH = Path("data/raw/online_retail_II.xlsx")

EXPECTED_COUNTS = {
    "Bad debt adjustment": 3,
    "Manual transaction": 854,
    "Merchandise cancellation candidate": 9906,
    "Merchandise sale candidate": 510267,
    "Postage / delivery": 736,
    "Test transaction": 15,
    "Zero-price negative adjustment": 2121,
    "Zero-price positive transaction": 1559,
}


@pytest.fixture(scope="module")
def classified_data():
    if not DATA_PATH.exists():
        pytest.skip("Original Online Retail II dataset unavailable")

    df = pd.read_excel(
        DATA_PATH,
        sheet_name="Year 2009-2010",
    )

    return classify_revenue_transactions(df)


def test_classification_counts_match_baseline(classified_data):
    actual = classified_data["RevenueCategory"].value_counts().to_dict()
    assert actual == EXPECTED_COUNTS


def test_classification_preserves_all_records(classified_data):
    assert len(classified_data) == 525461


def test_classification_has_no_missing_categories(classified_data):
    assert classified_data["RevenueCategory"].notna().all()
