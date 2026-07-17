from datetime import datetime
from enum import Enum

class Season(Enum):
    SUMMER = 0
    SPRING_AUTUMN = 1
    WINTER = 2

class PowerLoad(Enum):
    LIGHT = 0
    MEDIUM = 1
    PEAK = 2

LOAD_SCHEDULE = {
    Season.SUMMER: {
        PowerLoad.LIGHT: [(22, 8)],
        PowerLoad.MEDIUM: [(8, 15), (21, 22)],
        PowerLoad.PEAK: [(15, 21)],
    },

    Season.SPRING_AUTUMN: {
        PowerLoad.LIGHT: [(22, 8)],
        PowerLoad.MEDIUM: [(8, 15), (21, 22)],
        PowerLoad.PEAK: [(15, 21)],
    },

    Season.WINTER: {
        PowerLoad.LIGHT: [(22, 8)],
        PowerLoad.MEDIUM: [(8, 9), (12, 16), (19, 22)],
        PowerLoad.PEAK: [(9, 12), (16, 19)],
    },
}

ENERGY_CHARGE_TABLE = ( 
    (84.1, 84.1, 92.8),     # LIGHT
    (135.3, 91.5, 123.2),  # MEDIUM
    (157.8, 102.8, 138.0)   # PEAK
) # SUMMER  SPRING_AUTUMN  WINTER

def month_to_season(month: int) -> Season:
    if not 1 <= month <= 12:
        raise ValueError("ERROR::get_current_season()::month is not in 1~12")
    
    if 6 <= month <= 8:
        return Season.SUMMER

    if 3 <= month <= 5 or 9 <= month <= 10:
        return Season.SPRING_AUTUMN

    return Season.WINTER

def get_state() -> PowerLoad:
    now = datetime.now()

    season = month_to_season(now.month)
    hour = now.hour

    for power_load, time_ranges in LOAD_SCHEDULE[season].items():
        for start_hour, end_hour in time_ranges:
            if start_hour < end_hour:
                if start_hour <= hour < end_hour:
                    return season, hour, power_load
            else:
                if hour >= start_hour or hour < end_hour:
                    return season, hour, power_load

def get_energy_charge() -> float:
    season, hour, power_load = get_state()
    return ENERGY_CHARGE_TABLE[power_load.value][season.value], season, hour, power_load

if __name__ == "__main__":
    energy_charge, season, hour, power_load = get_energy_charge()
    print(f'state : {season.name}, {hour}H, {power_load.name}({energy_charge}원/kWh)')