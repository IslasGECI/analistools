#!/usr/bin/env python

import matplotlib

matplotlib.use("Agg")
matplotlib.rcParams["figure.dpi"] = 300

from matplotlib.ticker import MaxNLocator
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar

import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams["mathtext.fontset"] = "stix"
matplotlib.rcParams["font.family"] = "STIXGeneral"

islet_markers = {
    "Asuncion": "o",
    "Coronado": "^",
    "Morro Prieto and Zapato": "s",
    "Guadalupe": "X",
    "Natividad": "p",
    "San Benito": "h",
    "San Jeronimo": "D",
    "San Martin": "P",
    "San Roque": "*",
    "Todos Santos": ">",
}

islet_colors = {
    "Asuncion": "black",
    "Coronado": "red",
    "Morro Prieto and Zapato": "peru",
    "Guadalupe": "gold",
    "Natividad": "green",
    "San Benito": "blue",
    "San Jeronimo": "purple",
    "San Martin": "hotpink",
    "San Roque": "lightgreen",
    "Todos Santos": "skyblue",
}


def geci_plot():
    fig, ax = plt.subplots(figsize=(11, 8))
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    plt.yticks(rotation=90)
    return fig, ax

def plot_histogram_with_limits(x, bins, limits = [], plot_options = {}, lines_options = {}):
    fig, ax = geci_plot()
    ax.hist(x, bins=bins, **plot_options)
    for lines in limits:
        ax.axvline(x=lines, **lines_options)
    return ax

def roundup(x, multiplo):
    return np.ceil(x / multiplo) * multiplo

def fix_date(date):
    return (
        date.replace("Abr", "Apr").replace("Ene", "Jan").replace("Ago", "Aug").replace("Dic", "Dec")
    )


def set_map_tick_labels(fontsize=15):
    ejes = plt.gca()
    y_min, y_max = ejes.get_ylim()
    plt.yticks(
        [
            int(limite)
            for i_limite, limite in enumerate(np.linspace(y_min, y_max, 5))
            if i_limite > 0
        ],
        [
            f"{limite:.0f} mN" if i_limite == 4 else int(limite)
            for i_limite, limite in enumerate(np.linspace(y_min, y_max, 5))
            if i_limite > 0
        ],
        fontsize=fontsize,
    )

    ejes = plt.gca()
    x_min, x_max = ejes.get_xlim()
    plt.xticks(
        [
            int(limite)
            for i_limite, limite in enumerate(np.linspace(x_min, x_max, 5))
            if i_limite > 0
        ],
        [
            f"{limite:.0f} mE" if i_limite == 4 else int(limite)
            for i_limite, limite in enumerate(np.linspace(x_min, x_max, 5))
            if i_limite > 0
        ],
        fontsize=fontsize,
    )


def set_scale_bar(ax, length, width, loc="lower right"):
    scalebar = AnchoredSizeBar(
        ax.transData,
        length,
        f"{length} m",
        loc,
        pad=0.1,
        color="black",
        frameon=False,
        size_vertical=width,
    )
    ax.add_artist(scalebar)


def plot_location_plot(ax, linea_costa, margen_x, margen_y, box_length=500):
    axins = ax.inset_axes([0.05, 0.50, 0.2, 0.45])
    axins.fill(
        linea_costa.x, linea_costa.y, facecolor="#fffae6", edgecolor="black", linewidth=1, zorder=0
    )

    margen_subplot_x = np.array(margen_x) + np.array([-box_length, box_length])
    margen_subplot_y = np.array(margen_y) + np.array([-box_length, box_length])

    axins.set_xticklabels("")
    axins.set_yticklabels("")
    axins.set_facecolor("#E6FFFF")
    axins.set_xticks([])
    axins.set_yticks([])
    axins.plot(
        [
            margen_subplot_x[1],
            margen_subplot_x[0],
            margen_subplot_x[0],
            margen_subplot_x[1],
            margen_subplot_x[1],
        ],
        [
            margen_subplot_y[0],
            margen_subplot_y[0],
            margen_subplot_y[1],
            margen_subplot_y[1],
            margen_subplot_y[0],
        ],
        "red",
        linewidth=2,
    )

    for axis in ["top", "bottom", "left", "right"]:
        axins.spines[axis].set_linewidth(2)







