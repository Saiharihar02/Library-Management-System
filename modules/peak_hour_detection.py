import pandas as pd


def detect_peak_hours(
    file_path="datasets/library_occupancy.csv"
):

    df = pd.read_csv(file_path)

    hourly = (
        df.groupby("hour")["occupancy_rate"]
        .mean()
        .reset_index()
    )

    threshold = hourly["occupancy_rate"].quantile(0.75)

    peak_hours = hourly[
        hourly["occupancy_rate"] >= threshold
    ].copy()

    peak_hours = peak_hours.sort_values(
        "occupancy_rate",
        ascending=False
    )

    return peak_hours


if __name__ == "__main__":

    result = detect_peak_hours()

    print("\nPeak Library Hours")
    print("------------------")

    print(result.to_string(index=False))