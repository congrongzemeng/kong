"""Simple Vedic astrology utilities (stubs).

Replace these placeholder algorithms with authoritative astronomical
calculations or an ephemeris library for production use.
"""

from datetime import datetime
from typing import Dict, Any

class VedicAstro:
    def __init__(self, location: Dict[str, float] = None):
        """
        location: dict with keys 'lat' and 'lon' in decimal degrees (optional).
        """
        self.location = location or {"lat": 0.0, "lon": 0.0}

    def compute_tithi(self, dt: datetime) -> Dict[str, Any]:
        """
        Stub: returns an approximate tithi placeholder.
        Real implementation should compute Moon-Sun elongation using ephemeris data.
        """
        # Placeholder deterministic pseudo-value to make examples reproducible
        tithi_index = (dt.day % 30) + dt.hour / 24.0
        return {"tithi_index": tithi_index, "description": "placeholder tithi"}

    def compute_nakshatra(self, dt: datetime) -> Dict[str, Any]:
        """
        Stub: returns an approximate nakshatra placeholder.
        """
        nakshatra_index = (dt.timetuple().tm_yday % 27) + dt.hour / 24.0
        return {"nakshatra_index": nakshatra_index, "description": "placeholder nakshatra"}
