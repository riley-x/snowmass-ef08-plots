#!/usr/bin/env python3
# coding: utf-8

import matplotlib.pyplot as plt
import matplotlib.cm as mcm
import matplotlib.lines as mlines
import matplotlib.colors as mcolors
import atlas_mpl_style
import colorsys
import numpy as np
atlas_mpl_style.use_atlas_style(fancyLegend=True)

import ef08plot as ef08

################################################################
###                          INPUTS                          ###
###                                                          ###
### Edit the `vals` and `styles` variables with your data    ###
### and configuration                                        ###
###                                                          ###
################################################################

# A dictionary of group:data, with each entry corresponding to a group of bars
# in top to bottom order. The group name is shown on the y-label. `data` should be
# a dictionary containing entries collider:[limit, reference], in top to bottom
# order. It can also have optional entries
#       - 'annotation': An annotation is added to the group label
#       - 'current limits': A value for the current limit, which is drawn as a vertical bar

xlabel = r'$m(\widetilde{t}_1)$ [GeV]'
filename = 'stop'

vals = {
        '2-body': {
                    'HL-LHC': [1.7, 'ATL-PHYS-PUB-2018-021'],
                    'FCC-hh': [10.8, 'CERN-ACC-2018-0056'],
                    'ILC': [0.25, '$\\sqrt{s}/2$'],
                    'CLIC': [1.5, '$\\sqrt{s}/2$'],
                    'annotation': r'$\widetilde{t}_1 \to t\widetilde{\chi}_1^0$',
                    'current limits': 1.25,
                },
        '3-body': {
                    'HL-LHC': [0.85, 'ATL-PHYS-PUB-2018-021'],
                    'FCC-hh': [10, 'CERN-ACC-2018-0056'],
                    'ILC': [0.25, '~$\\sqrt{s}/2$'],
                    'CLIC': [1.5, '~$\\sqrt{s}/2$'],
                    'annotation': r'$\widetilde{t}_1 \to bW\widetilde{\chi}_1^0$',
                    'current limits': 0.75,
                },
        '4-body': {
                    'HL-LHC': [0.95, 'ATL-PHYS-PUB-2018-021'],
                    'FCC-hh': [5, 'CERN-ACC-2019-0036'],
                    'ILC': [0.25, '~$\\sqrt{s}/2$'],
                    'CLIC': [1.5, '~$\\sqrt{s}/2$'],
                    'annotation': r"$\widetilde{t}_1 \to bff'\widetilde{\chi}_1^0$",
                    'current limits': 0.625,
                },
        'Precision\nHiggs': {
                    'FCC-ee': [1, '1707.03399'],
                    'CEPC': [0.8, '1707.03399'],
                },
    }


# A dictionary of collider:styles, where the colliders correspond to those
# in `vals`. The order here is the order they appear in the legend. Styles
# is a dictionary of options to Axes.barh. You can optionally also include
# a style option 'annotation':annotation, which will append the annotation
# to the legend description.
#
# Note that an option, if used, must be specified for all colliders.
#
# https://matplotlib.org/3.5.0/api/_as_gen/matplotlib.axes.Axes.barh.html
cmap = mcm.get_cmap('Set3')
styles = {
        'HL-LHC': {'annotation':'14 TeV, 3 ab$^{-1}$', 'color':cmap(0), 'hatch':None},
        'FCC-hh': {'annotation':'100 TeV, 30 ab$^{-1}$', 'color':cmap(7), 'hatch':'/'},
        'ILC': {'annotation':'0.5 TeV, 4 ab$^{-1}$', 'color':cmap(3), 'hatch':'-'},
        'CLIC': {'annotation':'3 TeV, 5 ab$^{-1}$', 'color':cmap(4), 'hatch':'|'},
        'FCC-ee': {'annotation':'0.35 TeV, 12.6 ab$^{-1}$', 'color':cmap(2), 'hatch':'+'},
        'CEPC': {'annotation':'0.24 TeV, 10 ab$^{-1}$', 'color':cmap(5), 'hatch':'x'},
    }


ef08.plot(filename, xlabel, vals, styles)
