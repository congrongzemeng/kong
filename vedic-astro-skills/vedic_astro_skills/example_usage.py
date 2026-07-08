"""Example usage of the vedic_astro_skills package."""

from datetime import datetime
from vedic_astro_skills.skills import VedicAstro

def demo():
    va = VedicAstro(location={"lat": 28.6139, "lon": 77.2090})  # New Delhi approx
    now = datetime.utcnow()
    tithi = va.compute_tithi(now)
    nak = va.compute_nakshatra(now)
    print("UTC now:", now.isoformat())
    print("Tithi:", tithi)
    print("Nakshatra:", nak)

if __name__ == "__main__":
    demo()
