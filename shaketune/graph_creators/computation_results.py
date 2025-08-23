# Shake&Tune: 3D printer analysis tools
#
# Copyright (C) 2024 Félix Boisselier <felix@fboisselier.fr> (Frix_x on Discord)
# Licensed under the GNU General Public License v3.0 (GPL-3.0)
#
# File: computation_results.py
# Description: Specific computation result models for each graph type

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

from .base_models import ComputationResult


@dataclass
class AxesMapResult(ComputationResult):
    """Result from axes map detection computation"""

    acceleration_data: List[Tuple[np.ndarray, Tuple[np.ndarray, np.ndarray, np.ndarray]]]
    gravity: float
    average_noise_intensity_label: str
    position_data: List[Tuple[np.ndarray, np.ndarray, np.ndarray]]
    direction_vectors: List[np.ndarray]
    angle_errors: List[float]
    formatted_direction_vector: str
    accel: Optional[float] = None

    def get_plot_data(self) -> Dict[str, Any]:
        return {
            'acceleration_data_0': [d[0] for d in self.acceleration_data],
            'acceleration_data_1': [d[1] for d in self.acceleration_data],
            'gravity': self.gravity,
            'average_noise_intensity_label': self.average_noise_intensity_label,
            'position_data': self.position_data,
            'direction_vectors': self.direction_vectors,
            'angle_errors': self.angle_errors,
            'formatted_direction_vector': self.formatted_direction_vector,
            'measurements': self.measurements,
            'accel': self.accel,
            'st_version': self.metadata.version,
        }


@dataclass
class SignalData:
    """Data for a single signal in belts comparison"""

    freqs: np.ndarray
    psd: np.ndarray
    peaks: np.ndarray
    paired_peaks: Optional[List[Tuple[Tuple[int, float, float], Tuple[int, float, float]]]] = None
    unpaired_peaks: Optional[List[int]] = None


@dataclass
class BeltsResult(ComputationResult):
    """Result from belts comparison computation"""

    signal1: SignalData
    signal2: SignalData
    signal1_belt: str
    signal2_belt: str
    kinematics: Optional[str]
    test_params: Any  # testParams type
    max_freq: float
    max_scale: Optional[int]
    similarity_factor: Optional[float] = None
    mhi: Optional[str] = None

    def get_plot_data(self) -> Dict[str, Any]:
        return {
            'signal1': self.signal1,
            'signal2': self.signal2,
            'similarity_factor': self.similarity_factor,
            'mhi': self.mhi,
            'signal1_belt': self.signal1_belt,
            'signal2_belt': self.signal2_belt,
            'kinematics': self.kinematics,
            'test_params': self.test_params,
            'st_version': self.metadata.version,
            'measurements': self.measurements,
            'max_freq': self.max_freq,
            'max_scale': self.max_scale,
        }


@dataclass
class StaticFrequencyResult(ComputationResult):
    """Result from static frequency computation"""

    freq: Optional[float]
    duration: Optional[float]
    accel_per_hz: Optional[float]
    t: np.ndarray
    bins: np.ndarray
    pdata: np.ndarray
    max_freq: float

    def get_plot_data(self) -> Dict[str, Any]:
        return {
            'freq': self.freq,
            'duration': self.duration,
            'accel_per_hz': self.accel_per_hz,
            'st_version': self.metadata.version,
            'measurements': self.measurements,
            't': self.t,
            'bins': self.bins,
            'pdata': self.pdata,
            'max_freq': self.max_freq,
        }


@dataclass
class ShaperResult(ComputationResult):
    """Result from input shaper computation"""

    calibration_data: Any  # CalibrationData type
    shapers: List[Any]  # List of shaper objects
    shaper_table_data: Dict[str, Any]
    shaper_choices: List[str]
    peaks: np.ndarray
    peaks_freqs: np.ndarray
    peaks_threshold: Tuple[float, float]
    fr: float
    zeta: float
    t: np.ndarray
    bins: np.ndarray
    pdata: np.ndarray
    test_params: Any
    max_smoothing: Optional[float]
    scv: float
    max_freq: float
    max_scale: Optional[float]
    compat: bool = False
    max_smoothing_computed: Optional[float] = None

    def get_plot_data(self) -> Dict[str, Any]:
        return {
            'measurements': self.measurements,
            'compat': self.compat,
            'max_smoothing_computed': self.max_smoothing_computed,
            'max_freq': self.max_freq,
            'calibration_data': self.calibration_data,
            'shapers': self.shapers,
            'shaper_table_data': self.shaper_table_data,
            'shaper_choices': self.shaper_choices,
            'peaks': self.peaks,
            'peaks_freqs': self.peaks_freqs,
            'peaks_threshold': self.peaks_threshold,
            'fr': self.fr,
            'zeta': self.zeta,
            't': self.t,
            'bins': self.bins,
            'pdata': self.pdata,
            'test_params': self.test_params,
            'max_smoothing': self.max_smoothing,
            'scv': self.scv,
            'st_version': self.metadata.version,
            'max_scale': self.max_scale,
        }


@dataclass
class VibrationsResult(ComputationResult):
    """Result from vibrations analysis computation"""

    all_speeds: np.ndarray
    all_angles: np.ndarray
    all_angles_energy: Dict[float, np.ndarray]
    good_speeds: np.ndarray
    good_angles: np.ndarray
    kinematics: str
    accel: float
    motors: Optional[List[Any]]  # Motor objects
    motors_config_differences: Optional[str]
    symmetry_factor: float
    spectrogram_data: np.ndarray
    sp_min_energy: float
    sp_max_energy: float
    sp_variance_energy: float
    vibration_metric: float
    num_peaks: int
    vibration_peaks: List[Tuple[float, float, float, float]]
    target_freqs: List[Tuple[str, List[float]]]
    main_angles: List[float]
    global_motor_profile: Optional[Tuple[str, Tuple[float, float]]]
    motor_profiles: Optional[List[Tuple[str, Tuple[float, float]]]]
    max_freq: float
    motor_fr: Optional[float]
    motor_zeta: Optional[float]
    motor_res_idx: Optional[int]

    def get_plot_data(self) -> Dict[str, Any]:
        return {
            'measurements': self.measurements,
            'all_speeds': self.all_speeds,
            'all_angles': self.all_angles,
            'all_angles_energy': self.all_angles_energy,
            'good_speeds': self.good_speeds,
            'good_angles': self.good_angles,
            'kinematics': self.kinematics,
            'accel': self.accel,
            'motors': self.motors,
            'motors_config_differences': self.motors_config_differences,
            'symmetry_factor': self.symmetry_factor,
            'spectrogram_data': self.spectrogram_data,
            'sp_min_energy': self.sp_min_energy,
            'sp_max_energy': self.sp_max_energy,
            'sp_variance_energy': self.sp_variance_energy,
            'vibration_metric': self.vibration_metric,
            'num_peaks': self.num_peaks,
            'vibration_peaks': self.vibration_peaks,
            'target_freqs': self.target_freqs,
            'main_angles': self.main_angles,
            'global_motor_profile': self.global_motor_profile,
            'motor_profiles': self.motor_profiles,
            'max_freq': self.max_freq,
            'motor_fr': self.motor_fr,
            'motor_zeta': self.motor_zeta,
            'motor_res_idx': self.motor_res_idx,
            'st_version': self.metadata.version,
        }
