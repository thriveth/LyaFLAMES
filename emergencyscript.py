#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from astropy.table import Table
from astropy.io import fits
import glob

mw126015035a = fits.getdata(
    "./Data/Runs/106.219R.001/science_products/GOODSS_F3_2/mw126015035_1D.fits"
)
mw126015035b = fits.getdata(
    "./Data/Runs/106.219R.001/science_products/GOODSS_F3_3/mw126015035_1D.fits"
)

def get_spec(intable, kernel=1):
    print(kernel)
    kern = np.ones(kernel)/kernel
    wave = intable["WAVE"].flatten()
    flux = intable["FLUX_REDUCED"].flatten()
    flux = np.convolve(flux, kern, mode="same")
    return wave, flux

def plot_them(OB, color='black', ax=None, kernel=1):
    if not ax:
        fig, ax = plt.subplots(1, 1, dpi=200)
    files = glob.glob(f"./Data/Runs/106.219R.001/science_products/{OB}/*_1D.fits")
    for f in files:
        tempspec = fits.getdata(f)
        ax.plot(*get_spec(tempspec, kernel=kernel), lw=0.1, color=color)
    return files

kernwidth = 75
fig, ax = plt.subplots(1, 1, dpi=200)
f1 = plot_them("GOODSS_F3_2", color='C0', kernel=kernwidth, ax=ax)
f2 = plot_them("GOODSS_F3_3", color='C1', kernel=kernwidth, ax=ax)
ax.set_ylim(0, 20)
plt.show()
