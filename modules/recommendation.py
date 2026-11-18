import pandas as pd


def recommend_area(
    selected_area,
    hour,
    exam_period=0,
    file_path="datasets/library_occupancy.csv"
):

    df = pd.read_csv(file_path)

    filtered = df[
        (df["hour"] == hour) &
        (df["exam_period"] == exam_period)
    ]

    if filtered.empty:

        filtered = df[
            df["hour"] == hour
        ]

    area_data = (
        filtered.groupby(
            ["area", "total_seats"]
        )["occupied_seats"]
        .mean()
        .reset_index()
    )

    area_data["occupancy_rate"] = (
        area_data["occupied_seats"]
        / area_data["total_seats"]
        * 100
    )

    alternatives = area_data[
        area_data["area"] != selected_area
    ].copy()

    alternatives = alternatives[
        alternatives["occupancy_rate"] < 70
    ]

    alternatives = alternatives.sort_values(
        "occupancy_rate"
    )

    return alternatives


def recommend_resources(
    resource,
    hour,
    exam_period=0,
    file_path="datasets/library_occupancy.csv"
):

    df = pd.read_csv(file_path)

    filtered = df[
        (df["hour"] == hour) &
        (df["exam_period"] == exam_period)
    ]

    if filtered.empty:
        filtered = df[df["hour"] == hour]

    resource_data = (
        filtered.groupby("resource")["resource_demand"]
        .mean()
        .reset_index()
    )

    alternatives = resource_data[
        resource_data["resource"] != resource
    ]

    alternatives = alternatives.sort_values(
        "resource_demand"
    )

    return alternatives


if __name__ == "__main__":

    print("Alternative Study Areas")

    result = recommend_area(
        "General Reading",
        18,
        0
    )

    print(result)