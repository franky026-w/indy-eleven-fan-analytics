"""Illustrative scan-rate estimator from the provided model maintenance manual.
These are document-stated coefficients, NOT an independently validated model.
"""
def estimated_scan_rate(rain_level:int, fahrenheit:float, high_impact_theme:bool=False)->float:
    if rain_level not in (0,1,2):
        raise ValueError('rain_level must be 0 (clear), 1 (light), or 2 (heavy)')
    estimate = 0.39 - 0.086*rain_level - 0.0003*abs(fahrenheit-72)
    if high_impact_theme:
        estimate += 0.08
    return max(0., min(1., estimate))

if __name__ == '__main__':
    for rain in (0,1,2):
        print(f'Rain {rain}: {estimated_scan_rate(rain,72):.1%} predicted scan rate')
