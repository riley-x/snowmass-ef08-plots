#!/usr/bin/env python3
# coding: utf-8

import os
import sys
sys.path.insert(1, os.path.realpath(os.path.pardir))

import matplotlib.cm as mcm
import ef08plot as ef08

xlabel = r'$m(\widetilde{q}_1)$ [TeV]'
filename = 'squark'

vals = {
        r'$\widetilde{q}_R + \widetilde{q}_L$' "\n" r'$(\widetilde{u}, \widetilde{d}, \widetilde{s}, \widetilde{c})$': {
            'HL-LHC': [(2.5, 2.55, 2.6), 'Run 2 extrapolation'],
            'HE-LHC': [(4.6, 4.7, 4.8), 'Run 2 extrapolation'],
            'FCC-hh': [(10,(14.4+15.1)/2,15.1), 'Run 2 extrapolation'],
            'CLIC / Muon 3': [(1.45, 1.5, 1.5), r'European Strategy Report / $\sqrt{s}/2$'],
            'Muon 10': [10./2, r'$\sqrt{s}/2$'],
            'Muon 30': [30./2, r'$\sqrt{s}/2$'],
            'annotation': r'$m(\widetilde{\chi}_1^0) = 0$',
            'current limits': 1.66,
        },
#        r'single $\widetilde{q}$': {
#            'HL-LHC': [(1.8, 1.85, 1.9), 'Run 2 extrapolation'],
#            'HE-LHC': [(3.4,3.5,3.6), 'Run 2 extrapolation'],
#            'FCC-hh': [(10,10.2,10.4), 'Run 2 extrapolation'],
#            'CLIC / Muon 3': [3./2, r'$\sqrt{s}/2$'],
#            'Muon 10': [10./2, r'$\sqrt{s}/2$'],
#            'Muon 30': [30./2, r'$\sqrt{s}/2$'],
#            'annotation': r'$m(\widetilde{\chi}_1^0)=0$',
#            'current limits': 1.1,
#        },
}


cmap = mcm.get_cmap('Set3')
styles = {
        'HL-LHC': {'annotation':'14 TeV, 3 ab$^{-1}$', 'color':cmap(0), 'hatch':None},
        'HE-LHC': {'annotation':'27 TeV, 25 ab$^{-1}$', 'color':cmap(3), 'hatch':'-'},
        'FCC-hh': {'annotation':'100 TeV, 30 ab$^{-1}$', 'color':cmap(7), 'hatch':'/'},
        'CLIC / Muon 3': {'annotation':'TeV, 5 ab$^{-1}$', 'color':cmap(4), 'hatch':'|'},
        'Muon 10': {'annotation':'TeV, 10 ab$^{-1}$', 'color':cmap(5), 'hatch':'x'},
        'Muon 30': {'annotation':'TeV, 10 ab$^{-1}$', 'color':cmap(2), 'hatch':'+'}
}

ef08.plot(vals, styles, filename=filename, xlabel=xlabel, legend_nrow=2)
