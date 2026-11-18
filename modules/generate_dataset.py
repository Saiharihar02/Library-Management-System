import os
import numpy as np
import pandas as pd

np.random.seed(42)

output_folder = "datasets"
os.makedirs(output_folder, exist_ok=True)

areas = {
    "General Reading": 120,
    "Digital Library": 60,
    "Reference Section": 50,
    "Group Study": 80,
    "Computer Section": 70
}

resources = [
    "Textbooks",
    "Reference Books",
    "Journals",
    "Digital Resources",
    "Previous Year Papers"
]

dates = pd.date_range("2026-01-01", "2026-06-30", freq="D")

rows = []

for date in dates:

    day_name = date.day_name()
    weekday = date.weekday()
    is_weekend = 1 if weekday >= 5 else 0

    exam_period = np.random.choice([0, 1], p=[0.75, 0.25])

    for hour in range(8, 21):

        for area, capacity in areas.items():

            if is_weekend:
                base = 20
            else:
                base = 35

            morning_peak = 0
            afternoon_peak = 0
            evening_peak = 0

            if 9 <= hour <= 11:
                morning_peak = 25

            if 12 <= hour <= 14:
                afternoon_peak = 10

            if 16 <= hour <= 19:
                evening_peak = 30

            area_factor = {
                "General Reading": 1.00,
                "Digital Library": 0.70,
                "Reference Section": 0.60,
                "Group Study": 0.85,
                "Computer Section": 0.75
            }[area]

            exam_boost = 25 if exam_period else 0

            seasonal_change = np.random.randint(-12, 13)

            occupied = (
                base
                + morning_peak
                + afternoon_peak
                + evening_peak
                + exam_boost
            )

            occupied = occupied * area_factor
            occupied += seasonal_change
            occupied += np.random.normal(0, 6)

            occupied = max(5, min(capacity, int(occupied)))

            occupancy_rate = round((occupied / capacity) * 100, 2)

            resource = np.random.choice(resources)

            resource_base = {
                "Textbooks": 25,
                "Reference Books": 18,
                "Journals": 10,
                "Digital Resources": 20,
                "Previous Year Papers": 15
            }[resource]

            resource_demand = (
                resource_base
                + (20 if exam_period else 0)
                + (15 if 16 <= hour <= 19 else 0)
                + np.random.randint(-8, 9)
            )

            resource_demand = max(5, resource_demand)

            if resource_demand >= 45:
                demand_level = "High"
            elif resource_demand >= 25:
                demand_level = "Moderate"
            else:
                demand_level = "Low"

            rows.append([
                date,
                day_name,
                weekday,
                is_weekend,
                hour,
                area,
                capacity,
                occupied,
                occupancy_rate,
                exam_period,
                resource,
                resource_demand,
                demand_level
            ])

columns = [
    "date",
    "day",
    "day_of_week",
    "is_weekend",
    "hour",
    "area",
    "total_seats",
    "occupied_seats",
    "occupancy_rate",
    "exam_period",
    "resource",
    "resource_demand",
    "demand_level"
]

df = pd.DataFrame(rows, columns=columns)

file_path = os.path.join(output_folder, "library_occupancy.csv")

df.to_csv(file_path, index=False)

print("Dataset generated successfully")
print("Rows:", len(df))
print("File:", file_path)
print()
print(df.head())