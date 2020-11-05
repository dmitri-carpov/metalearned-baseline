import numpy as np

Forecast = np.ndarray
Target = np.ndarray


def mase(forecast: Forecast, insample: np.ndarray, outsample: Target, frequency: int) -> np.ndarray:
    """
    Calculate MASE of each point for each timeseries.
    https://en.wikipedia.org/wiki/Mean_absolute_scaled_error

    :param forecast:
    :param insample:
    :param outsample:
    :param frequency:
    :return:
    """
    return np.mean(np.abs(forecast - outsample)) / np.mean(np.abs(insample[:-frequency] - insample[frequency:]))


def nd(forecast: Forecast, target: Target) -> float:
    """
    Normalized deviation as defined in https://www.cs.utexas.edu/~rofuyu/papers/tr-mf-nips.pdf

    :param forecast:
    :param target:
    :return:
    """
    return np.mean(np.abs(target - forecast)) / np.mean(np.abs(target))


def nrmse(forecast: Forecast, target: Target) -> float:
    """
    Normalized RMSE as defined in https://www.cs.utexas.edu/~rofuyu/papers/tr-mf-nips.pdf

    :param forecast:
    :param target:
    :return:
    """
    return np.sqrt(np.mean(np.power((forecast - target), 2))) / (np.mean(np.abs(target)))


def mape(forecast: Forecast, target: Target) -> np.ndarray:
    """
    Calculate MAPE.
    This method accepts one or many timeseries.
    For multiple timeseries pass matrix (N, M) where N is number of timeseries and M is number of time steps.

    :param forecast: Predicted values.
    :param target: Target values.
    :return: Same shape array with sMAPE calculated for each time step of each timeseries.
    """
    return 100 * np.abs(forecast - target) / target


def smape_1(forecast: Forecast, target: Target) -> np.ndarray:
    """
    Calculate Armstrong's original definition of sMAPE.
    This method accepts one or many timeseries.
    For multiple timeseries pass matrix (N, M) where N is number of timeseries and M is number of time steps.

    :param forecast: Predicted values.
    :param target: Target values.
    :return: Same shape array with sMAPE calculated for each time step of each timeseries.
    """
    return 200 * np.abs(forecast - target) / (target + forecast)


def smape_2(forecast: Forecast, target: Target) -> np.ndarray:
    """
    Calculate sMAPE.
    This method accepts one or many timeseries.
    For multiple timeseries pass matrix (N, M) where N is number of timeseries and M is number of time steps.

    :param forecast: Predicted values.
    :param target: Target values.
    :return: Same shape array with sMAPE calculated for each time step of each timeseries.
    """
    denom = np.abs(target) + np.abs(forecast)
    denom[denom == 0.0] = 1.0  # divide by 1.0 instead of 0.0, in case when denom is zero the enum will be 0.0 anyways.
    return 200 * np.abs(forecast - target) / denom
