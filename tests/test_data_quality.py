"""Data-quality regression tests for Online Retail II."""

from pathlib import Path

import pandas as pd
import pytest


DATA_PATH = (
    Path(__file__).resolve().parents[1]
    / "data/raw/online_retail_II.xlsx"
)


@pytest.fixture(scope="module")
def retail_data():
    if not DATA_PATH.is_file():
        pytest.fail("Raw dataset not found at expected path")

    return pd.read_excel(
        DATA_PATH,
        sheet_name="Year 2009-2010",
    )


def test_dataset_dimensions(retail_data):
    assert retail_data.shape == (525461, 8)


def test_required_columns(retail_data):
    expected = {
        "Invoice", "StockCode", "Description",
        "Quantity", "InvoiceDate", "Price",
        "Customer ID", "Country",
    }
    assert set(retail_data.columns) == expected


def test_zero_price_count(retail_data):
    assert int(retail_data["Price"].eq(0).sum()) == 3687


def test_negative_price_count(retail_data):
    assert int(retail_data["Price"].lt(0).sum()) == 3


def test_raw_negative_quantity_count(retail_data):
    assert int(retail_data["Quantity"].lt(0).sum()) == 12326


def test_raw_cancellation_count(retail_data):
    cancelled = (
        retail_data["Invoice"]
        .astype("string")
        .str.upper()
        .str.startswith("C", na=False)
    )
    assert int(cancelled.sum()) == 10206


def test_zero_price_negative_adjustments(retail_data):
    mask = (
        retail_data["Quantity"].lt(0)
        & retail_data["Price"].eq(0)
    )
    assert int(mask.sum()) == 2121
