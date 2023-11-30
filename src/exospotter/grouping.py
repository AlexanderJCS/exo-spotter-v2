from dataclasses import dataclass
import pandas as pd


@dataclass(frozen=True)
class Datapoint:
    """
    Used to represent a lightcurve datapoint.
    """

    flux: float
    time: float


@dataclass(frozen=True)
class Group:
    """
    Used to represent a group of lightcurve datapoints between two time intervals.
    """

    start_time: float
    end_time: float
    mean_flux: float
    peak_flux: float
    min_flux: float

    def middle_time(self) -> float:
        """
        :return: The midpoint of self.start_time and self.end_time
        """

        return (self.end_time - self.start_time) / 2

    @staticmethod
    def generate_group(data: pd.DataFrame):
        """
        Generates a group from a list of datapoints sorted by time.
        There must be at least one item in the datapoints dataframe to avoid an exception.

        :param data: The datapoints to convert into a group. There must be two columns: flux and time.
        :return: A group object that references the datapoints
        """

        start_time = data.time[0]
        end_time = data.time[-1]

        mean_flux = data.flux.mean()
        peak_flux = data.flux.max()
        min_flux = data.flux.min()

        return Group(start_time, end_time, mean_flux, peak_flux, min_flux)

