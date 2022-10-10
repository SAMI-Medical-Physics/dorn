import numpy as np
from dorn import Gui
from datetime import datetime, timedelta


def test_administered_activity():
    calib_activity = 100
    calib_datetime = datetime(year=2021, month=10, day=25, hour=10, minute=15)
    half_life = 6  # h
    n_half_lives = 2.3

    admin_datetime = calib_datetime + timedelta(hours=n_half_lives * half_life)
    residual = None
    a0 = Gui.administered_activity(
        calib_activity, calib_datetime, admin_datetime, half_life, residual=residual
    )
    assert a0 == calib_activity * (1 / 2) ** n_half_lives
    assert (
        Gui.administered_activity(
            0.0, calib_datetime, admin_datetime, half_life, residual=residual
        )
        == 0.0
    )

    residual_activity = 5
    n_half_lives = 1.3
    residual_datetime = admin_datetime + timedelta(hours=n_half_lives * half_life)
    a0_hand = a0 - (2**n_half_lives) * residual_activity
    residual = (residual_activity, residual_datetime)
    a0_calc = Gui.administered_activity(
        calib_activity, calib_datetime, admin_datetime, half_life, residual=residual
    )
    assert np.isclose(a0_calc, a0_hand)

    assert (
        Gui.administered_activity(
            calib_activity, calib_datetime, calib_datetime, half_life, residual=None
        )
        == calib_activity
    )


def test_discharge_activity_exp():
    effective_half_life = 11.0
    admin_datetime = datetime(year=2021, month=10, day=25, hour=10, minute=15)
    n_half_lives = 2.3
    a0 = 1000.0
    discharge_datetime = admin_datetime + timedelta(
        hours=n_half_lives * effective_half_life
    )

    discharge_activity_hand = a0 * (1 / 2) ** n_half_lives

    model = "exponential"
    dose_rate_xm_init = np.nan
    model_parameters = [dose_rate_xm_init, effective_half_life]

    discharge_activity_calc = Gui.discharge_activity(
        admin_datetime, discharge_datetime, model, model_parameters, a0
    )
    assert np.isclose(discharge_activity_calc, discharge_activity_hand)

    assert (
        Gui.discharge_activity(
            admin_datetime, admin_datetime, model, model_parameters, a0
        )
        == a0
    )


def test_discharge_activity_biexp():
    dose_rate_xm_init = np.nan
    fraction_1 = 0.2
    half_life_1 = 8.0
    half_life_2 = 20.0

    admin_datetime = datetime(year=2021, month=10, day=25, hour=10, minute=15)
    hrs = 21
    a0 = 1000.0
    discharge_datetime = admin_datetime + timedelta(hours=hrs)

    discharge_activity_hand = a0 * (
        (fraction_1 * (1 / 2) ** (hrs / half_life_1))
        + ((1 - fraction_1) * (1 / 2) ** (hrs / half_life_2))
    )

    model = "biexponential"
    dose_rate_xm_init = 80.0
    model_parameters = [dose_rate_xm_init, fraction_1, half_life_1, half_life_2]

    discharge_activity_calc = Gui.discharge_activity(
        admin_datetime, discharge_datetime, model, model_parameters, a0
    )
    assert np.isclose(discharge_activity_calc, discharge_activity_hand)

    assert (
        Gui.discharge_activity(
            admin_datetime, admin_datetime, model, model_parameters, a0
        )
        == a0
    )


def test_discharge_dose_rate_exp():
    dose_rate_xm_init = 80.0
    effective_half_life = 11.0
    admin_datetime = datetime(year=2021, month=10, day=25, hour=10, minute=15)
    n_half_lives = 2.3
    measurement_distance = 2.0

    discharge_datetime = admin_datetime + timedelta(
        hours=n_half_lives * effective_half_life
    )
    model = "exponential"
    model_parameters = [dose_rate_xm_init, effective_half_life]

    discharge_dose_rate_xm_hand = dose_rate_xm_init * (1 / 2) ** n_half_lives
    discharge_dose_rate_1m_hand = (
        discharge_dose_rate_xm_hand * measurement_distance**1.5
    )

    discharge_dose_rate_1m, discharge_dose_rate_xm = Gui.discharge_dose_rate(
        admin_datetime,
        discharge_datetime,
        model,
        model_parameters,
        measurement_distance,
    )
    assert np.isclose(discharge_dose_rate_1m, discharge_dose_rate_1m_hand)
    assert np.isclose(discharge_dose_rate_xm, discharge_dose_rate_xm_hand)

    assert (
        Gui.discharge_dose_rate(
            admin_datetime,
            admin_datetime,
            model,
            model_parameters,
            measurement_distance,
        )[0]
        == model_parameters[0] * measurement_distance**1.5
    )
    assert (
        Gui.discharge_dose_rate(
            admin_datetime,
            admin_datetime,
            model,
            model_parameters,
            measurement_distance,
        )[1]
        == model_parameters[0]
    )


def test_discharge_dose_rate_biexp():
    dose_rate_xm_init = 50.0
    fraction_1 = 0.2
    half_life_1 = 8.0
    half_life_2 = 20.0

    admin_datetime = datetime(year=2021, month=10, day=25, hour=10, minute=15)
    hrs = 30.1
    measurement_distance = 2.0

    discharge_datetime = admin_datetime + timedelta(hours=hrs)
    model = "biexponential"
    model_parameters = [dose_rate_xm_init, fraction_1, half_life_1, half_life_2]

    discharge_dose_rate_xm_hand = dose_rate_xm_init * (
        (fraction_1 * (1 / 2) ** (hrs / half_life_1))
        + ((1 - fraction_1) * (1 / 2) ** (hrs / half_life_2))
    )
    discharge_dose_rate_1m_hand = (
        discharge_dose_rate_xm_hand * measurement_distance**1.5
    )

    discharge_dose_rate_1m, discharge_dose_rate_xm = Gui.discharge_dose_rate(
        admin_datetime,
        discharge_datetime,
        model,
        model_parameters,
        measurement_distance,
    )
    assert np.isclose(discharge_dose_rate_1m, discharge_dose_rate_1m_hand)
    assert np.isclose(discharge_dose_rate_xm, discharge_dose_rate_xm_hand)

    assert (
        Gui.discharge_dose_rate(
            admin_datetime,
            admin_datetime,
            model,
            model_parameters,
            measurement_distance,
        )[0]
        == model_parameters[0] * measurement_distance**1.5
    )
    assert (
        Gui.discharge_dose_rate(
            admin_datetime,
            admin_datetime,
            model,
            model_parameters,
            measurement_distance,
        )[1]
        == model_parameters[0]
    )
