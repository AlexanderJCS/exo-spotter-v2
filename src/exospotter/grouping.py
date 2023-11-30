from dataclasses import dataclass


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
    Used to represent a group of datapoints between two time intervals.
    """

    start_time: float
    end_time: float
    mean_flux: float
    peak_flux_dp: Datapoint
    min_flux_dp: Datapoint

    def middle_time(self) -> float:
        """
        :return: The midpoint of self.start_time and self.end_time
        """

        return (self.end_time - self.start_time) / 2
