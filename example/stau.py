#!/usr/bin/env python3
# coding: utf-8

import os
import sys
sys.path.insert(1, os.path.realpath(os.path.pardir))

import matplotlib.cm as mcm
import ef08plot as ef08

filename = 'stau'
vals = {
    r'$\Delta m(\widetilde{\tau}, \widetilde{\chi}^0_1)$'"\n$=10$ GeV": {
        'HE-LHC': [.176, 'CERN-LPCC-2018-05'],
        'FCC-hh': [.392, 'HE-LHC Re-scaled'],
        'ILC': [0.25, '2203.15729'],
    },
    r'$\Delta m(\widetilde{\tau}, \widetilde{\chi}^0_1)$'"\n$=100$ GeV": {
        'HL-LHC': [[.207, .27, .373], 'CMS-PAS-FTR-18-010'],
        'HE-LHC': [.767, 'LHC Run-2 Re-scaled'],
        'FCC-hh': [1.748, 'LHC Run-2 Re-scaled'],
        'ILC': [0.25, '2203.15729'],
        'CLIC': [1.25, 'CERN-ESU-004'],
        'current limits': .163,
    },
    r'$\Delta m(\widetilde{\tau}, \widetilde{\chi}^0_1)$'"\n$>400$ GeV": {
        'HL-LHC': [[.638, .638, .679], 'CMS-PAS-FTR-18-010'],
        'HE-LHC': [[1.116,2.621,2.751], 'HL-LHC Re-scaled'],
        'FCC-hh': [[6.375,6.375,6.745], 'HL-LHC Re-scaled'],
        'ILC': [0.25, '2203.15729'],
    },
}

cmap = mcm.get_cmap('Set3')
styles = {
    'HL-LHC': {'annotation':'14 TeV, 3 ab$^{-1}$', 'color':cmap(0), 'hatch':None},
    'HE-LHC': {'annotation':'14 TeV, 3 ab$^{-1}$', 'color':cmap(1), 'hatch':'\\'},
    'FCC-hh': {'annotation':'100 TeV, 30 ab$^{-1}$', 'color':cmap(7), 'hatch':'/'},
    'ILC': {'annotation':'0.5 TeV, 4 ab$^{-1}$', 'color':cmap(3), 'hatch':'-'},
    'CLIC': {'annotation':'3 TeV, 5 ab$^{-1}$', 'color':cmap(4), 'hatch':'|'},
    'FCC-ee': {'annotation':'0.35 TeV, 12.6 ab$^{-1}$', 'color':cmap(2), 'hatch':'+'},
    'CEPC': {'annotation':'0.24 TeV, 10 ab$^{-1}$', 'color':cmap(5), 'hatch':'x'},
}

xlabel = r'$m(\widetilde{\tau})$ [TeV]'
ylabel = 'Colliders'

ef08.plot(filename, vals, styles, xlabel=xlabel, ylabel=ylabel, legend_nrow=3)
