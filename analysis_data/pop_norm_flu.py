"""
pop_norm_flu.py

Goal:
- Normalize weekly flu hospitalizations by state population
- Produce comparable hospitalization rates across states

Input:
- analysis_data/formatted_flu.csv

Output:
- analysis_data/hosps_pop_norm.csv

Definition:
- hosps_pop_norm = value / (population / 100000)
"""

import os
import pandas as pd

IN_PATH = os.path.join("analysis_data", "formatted_flu.csv")
OUT_PATH = os.path.join("analysis_data", "hosps_pop_norm.csv")


def main():
    if not os.path.exists(IN_PATH):
        raise FileNotFoundError(f"Input file not found: {IN_PATH}")

    df = pd.read_csv(IN_PATH)

    # Sanity check
    required_cols = {"value", "population"}
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # Normalize hospitalizations per 100k population
    df["hosps_pop_norm"] = df["value"] / (df["population"] / 100_000)

    # Optional: keep things tidy
    df = df.sort_values(
        ["season", "location", "season_week"]
    ).reset_index(drop=True)

    df.to_csv(OUT_PATH, index=False)

    print(f"Wrote {OUT_PATH} with {len(df):,} rows.")
    print(
        "   hosps_pop_norm summary:",
        f"min={df['hosps_pop_norm'].min():.3f},",
        f"max={df['hosps_pop_norm'].max():.3f}",
    )


if __name__ == "__main__":
    main()
