import pandas as pd


def get_seat_availability(
    area,
    hour,
    exam_period=0,
    file_path="datasets/library_occupancy.csv"
):

    df = pd.read_csv(file_path)

    filtered = df[
        (df["area"] == area) &
        (df["hour"] == hour) &
        (df["exam_period"] == exam_period)
    ]

    if filtered.empty:

        filtered = df[
            (df["area"] == area) &
            (df["hour"] == hour)
        ]

    if filtered.empty:
        return None

    latest = filtered.iloc[-1]

    total_seats = int(latest["total_seats"])
    occupied_seats = int(latest["occupied_seats"])

    available_seats = max(
        0,
        total_seats - occupied_seats
    )

    occupancy_rate = round(
        occupied_seats / total_seats * 100,
        2
    )

    return {
        "area": area,
        "total_seats": total_seats,
        "occupied_seats": occupied_seats,
        "available_seats": available_seats,
        "occupancy_rate": occupancy_rate
    }


if __name__ == "__main__":

    result = get_seat_availability(
        "General Reading",
        18,
        0
    )

    print(result)