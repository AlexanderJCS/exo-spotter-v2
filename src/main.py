import exospotter

import pandas as pd


def main():
    data = pd.read_csv("../data/wasp-126.csv")
    data.rename(columns={"julian_date": "time"}, inplace=True)

    for group in exospotter.grouping.group_datapoints(data, 0.01):
        print(f"{group.middle_time()},{group.mean_flux}")


if __name__ == "__main__":
    main()
