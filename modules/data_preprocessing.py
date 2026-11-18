import pandas as pd


def load_data(path="datasets/library_occupancy.csv"):
    df = pd.read_csv(path)

    df["date"] = pd.to_datetime(df["date"])

    return df


def prepare_features(df):

    data = df.copy()

    data["month"] = data["date"].dt.month
    data["day_of_month"] = data["date"].dt.day

    data["hour_sin"] = __import__("numpy").sin(
        2 * __import__("numpy").pi * data["hour"] / 24
    )

    data["hour_cos"] = __import__("numpy").cos(
        2 * __import__("numpy").pi * data["hour"] / 24
    )

    data = pd.get_dummies(
        data,
        columns=["area", "resource"],
        dtype=int
    )

    return data


def get_occupancy_features(df):

    data = prepare_features(df)

    target = "occupied_seats"

    feature_columns = [
        "hour",
        "day_of_week",
        "is_weekend",
        "exam_period",
        "month",
        "day_of_month",
        "hour_sin",
        "hour_cos"
    ]

    area_columns = [
        column for column in data.columns
        if column.startswith("area_")
    ]

    feature_columns.extend(area_columns)

    X = data[feature_columns]
    y = data[target]

    return X, y


def get_demand_features(df):

    data = prepare_features(df)

    target = "resource_demand"

    feature_columns = [
        "hour",
        "day_of_week",
        "is_weekend",
        "exam_period",
        "month",
        "day_of_month",
        "hour_sin",
        "hour_cos"
    ]

    area_columns = [
        column for column in data.columns
        if column.startswith("area_")
    ]

    resource_columns = [
        column for column in data.columns
        if column.startswith("resource_")
    ]

    feature_columns.extend(area_columns)
    feature_columns.extend(resource_columns)

    X = data[feature_columns]
    y = data[target]

    return X, y