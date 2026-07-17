from power_load import *

from time import sleep

def update(threshold = 100) -> int:
    energy_charge, season, hour, power_load = get_energy_charge()
    print(f' state : {season.name}, {hour}H, {power_load.name}({energy_charge}원/kWh)')

    if energy_charge <= threshold:
        print(f'result : ON ({threshold} <= {energy_charge})')
        return 1
    
    print(f'result : OFF ({threshold} > {energy_charge})')
    return 0

if __name__ == '__main__':
    while True:
        update()
        sleep(3)