#!/usr/bin/env python3
# coding: utf-8

import os
import sys
sys.path.insert(1, os.path.realpath(os.path.pardir))

import matplotlib.cm as mcm
import ef08plot as ef08

vals = {
    '': {
        'HL-LHC': [1.52, ''],
        'HE-LHC': [3.11, ''],
        'FCC-hh': [7.17, ''],
        'current limits': .680,
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

xlabel = r'$m(\widetilde{\mu})$ [TeV]'
ylabel = r'$\tau = 0.1$ns'

ef08.plot(filename, vals, styles, xlabel=xlabel, ylabel=ylabel)
