"""Tests for final revenue classification refinements."""

import pandas as pd

from src.cleaning import refine_revenue_classifications


def make_data():
    codes = [
        "POST", "D", "S", "ADJUST", "AMAZONFEE",
        "DOT", "C2", "BANK CHARGES", "ADJUST2",
        "GIFT_0001_10", "12345", None,
    ]

    return pd.DataFrame({
        "StockCode": codes,
        "RevenueCategory": [
            "Merchandise sale candidate"
        ] * len(codes),
    })


def test_special_stock_code_classifications():
    result = refine_revenue_classifications(make_data())

    expected = [
        "Postage / delivery",
        "Discount",
        "Samples / Review",
        "Accounting adjustment",
        "Marketplace fee",
        "Postage / delivery",
        "Postage / delivery",
        "Bank charges",
        "Accounting adjustment",
        "Gift voucher / Review",
        "Merchandise sale candidate",
        "Merchandise sale candidate",
    ]

    assert result["RevenueCategory"].tolist() == expected


def test_classification_is_case_insensitive():
    df = pd.DataFrame({
        "StockCode": ["post", " d ", "bank charges"],
        "RevenueCategory": ["Other / Review"] * 3,
    })

    result = refine_revenue_classifications(df)

    assert result["RevenueCategory"].tolist() == [
        "Postage / delivery",
        "Discount",
        "Bank charges",
    ]


def test_original_dataframe_unchanged():
    df = make_data()
    original = df.copy(deep=True)

    refine_revenue_classifications(df)

    pd.testing.assert_frame_equal(df, original)


def test_row_count_and_missing_stock_codes():
    df = make_data()
    result = refine_revenue_classifications(df)

    assert len(result) == len(df)
    assert result["RevenueCategory"].notna().all()
    assert (
        result.loc[
            result["StockCode"].isna(),
            "RevenueCategory"
        ].iloc[0]
        == "Merchandise sale candidate"
    )
