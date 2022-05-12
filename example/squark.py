#!/usr/bin/env python3
# coding: utf-8

import matplotlib.cm as mcm
import ef08plot as ef08

xlabel = r'$m(\widetilde{q}_1)$ [GeV]'
filename = 'squark'

vals = {
        '8 squarks': {
                    'HL-LHC': [2.5, 'CR extrapolation from CMS Run 2'],
                    'HL-LHC': [2.6, 'CR extrapolation from ATLAS Run 2'],
                    'FCC-hh': [14.4, 'CR extrapolation from CMS Run 2'],
                    'annotation': r'$m(\chi) = 0$',
                    'current limits': 1.66,
        },
        '1 squark': {
                    'HL-LHC': [1.8, 'CR extrapolation from CMS Run 2'],
                    'HL-LHC': [1.9, 'CR extrapolation from ATLAS Run 2'],
                    'FCC-hh': [10, 'CR extrapolation from CMS Run 2'],
                    'annotation': r'$m(\chi)=0$',
                    'current limits': 1.1,
        },
}


cmap = mcm.get_cmap('Set3')
styles = {
        'HL-LHC': {'annotation':'14 TeV, 3 ab$^{-1}$', 'color':cmap(0), 'hatch':None},
        'FCC-hh': {'annotation':'100 TeV, 30 ab$^{-1}$', 'color':cmap(7), 'hatch':'/'},
        'ILC': {'annotation':'0.5 TeV, 4 ab$^{-1}$', 'color':cmap(3), 'hatch':'-'},
        'CLIC': {'annotation':'3 TeV, 5 ab$^{-1}$', 'color':cmap(4), 'hatch':'|'},
        'FCC-ee': {'annotation':'0.35 TeV, 12.6 ab$^{-1}$', 'color':cmap(2), 'hatch':'+'},
        'CEPC': {'annotation':'0.24 TeV, 10 ab$^{-1}$', 'color':cmap(5), 'hatch':'x'},
}

ef08.plot(filename, xlabel, vals, styles, legend_nrow=1)
