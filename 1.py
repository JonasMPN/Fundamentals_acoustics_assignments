import numpy as np
rho = 1.2
c = 343

do = {
    "1.1": True,
    "1.2": True,
    "2.1": False,
    "2.2": False
}

def spl_to_p(spl, p_ref=2e-5):
    "Sound pressure level to pressure"
    return spl_to_prms(spl, p_ref)*np.sqrt(2)

def spl_to_prms(spl, p_ref=2e-5):
    "sound pressure level to pressure_rms"
    return 10**(spl/20)*p_ref

def swr_to_spac(swr):
    "Standing wave ratio to specific power absorption coefficient"
    return 1-((swr-1)/(swr+1))**2

def R_to_impedance(R):
    "Reflection coefficient to impedance"
    return rho*c*(1+R)/(1-R)

spl_max, spl_min = 90.6, 62.7
if do["1.1"]:
    print(f"Min sound pressure amplitude: {spl_to_p(spl_min)} Pa")
    print(f"Max sound pressure amplitude: {spl_to_p(spl_max)} Pa")
    print(f"Standing wave ratio: {spl_to_p(spl_max)/spl_to_p(spl_min)}")
    print(f"Sound power absorption ratio: {swr_to_spac(spl_to_p(spl_max)/spl_to_p(spl_min))}")

if do["1.2"]:
    swr = spl_to_p(spl_max)/spl_to_p(spl_min)
    print(f"Impedance: {R_to_impedance((swr-1)/(swr+1))}")

def spl_to_P(spl, radius):
    "Sound pressure level to power"
    return spl_to_prms(spl)**2/(rho*c)*4*np.pi*radius**2

spl_distance_combi = (72.2, 10)
if do["2.1"]:
    print(f"Total acoustic power: {spl_to_P(*spl_distance_combi)} W")

freq = 20
radius = 2
u = 1.5e-3
def speed_to_intensity(velocity, frequency, radius):
    return velocity**2*rho*c/(2*(1+(c/(2*np.pi*frequency*radius))**2))

def intensity_to_sP(intensity, radius):
    return 4*np.pi*radius**2*intensity

if do["2.2"]:
    print(f"Radial intensity: {speed_to_intensity(u, freq, radius)} kg s-3")
    print(f"Total power: {intensity_to_sP(speed_to_intensity(u, freq, radius), radius)} kg m2 s-3")

