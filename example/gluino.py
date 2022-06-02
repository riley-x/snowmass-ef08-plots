#!/usr/bin/env python3
# coding: utf-8

import os
import sys
sys.path.insert(1, os.path.realpath(os.path.pardir))

import matplotlib.cm as mcm
import ef08plot as ef08

xlabel = r'$m(\widetilde{g})$ [TeV]'
filename = 'gluino'

vals = {
        r'$\widetilde{g} \to q \overline{q} \widetilde{\chi}_1^0$': {
            'HL-LHC': [(3.0,3.1,3.2), 'Run 2 extrapolation'],
            'HE-LHC': [(5.5,5.7,5.9), 'Run 2 extrapolation'],
            'FCC-hh': [(17.5, (17.7+19.2)/2.,19.2), 'Run 2 extrapolation'],
            'annotation': r'$m(\widetilde{\chi}_1^0) = 0$',
            'current limits': 2.3,
        },
        r'compressed $\widetilde{g} \to q\overline{q}\widetilde{\chi}_1^0$': {
            'HL-LHC': [(1.5,1.8,1.8), 'Run 2 extrapolation'],
            'HE-LHC': [(2.2,3.4,3.4), 'Run 2 extrapolation'],
            'FCC-hh': [(8.6,10,10), 'Run 2 extrapolation'],
            'annotation': r'$m(\widetilde{g})-m(\widetilde{\chi}_1^0)$ < 50 GeV',
            'current limits': 1.1,
        },
        r'$\widetilde{g} \to t\overline{t} \widetilde{\chi}_1^0$': {
            'HL-LHC': [(2.5,3.05,3.05), 'Run 2 extrapolation'],
            'HE-LHC': [5.6, 'Run 2 extrapolation'],
            'FCC-hh': [(12.4,18.1,18.1), 'Run 2 extrapolation'],
            'annotation': r'$m(\widetilde{\chi}_1^0) = 0$',
            'current limits': 2.15,
        },
        r'compressed $\widetilde{g} \to t\overline{t}\widetilde{\chi}_1^0$': {
            'HL-LHC': [(1.25,2.5,2.5), 'Run 2 extrapolation'],
            'HE-LHC': [3.9, 'Run 2 extrapolation'],
            'FCC-hh': [11.6, 'Run 2 extrapolation'],
            'annotation': r'$m(\widetilde{g})-m(\widetilde{\chi}_1^0)$ < 50 GeV',
            'current limits': 1.3,
        },
}


cmap = mcm.get_cmap('Set3')
styles = {
        'HL-LHC': {'annotation':'14 TeV, 3 ab$^{-1}$', 'color':cmap(0), 'hatch':None},
        'HE-LHC': {'annotation':'27 TeV, 15 ab$^{-1}$', 'color':cmap(3), 'hatch':'-'},
        'FCC-hh': {'annotation':'100 TeV, 30 ab$^{-1}$', 'color':cmap(7), 'hatch':'/'},
        'CLIC': {'annotation':'3 TeV, 5 ab$^{-1}$', 'color':cmap(4), 'hatch':'|'},
        'FCC-ee': {'annotation':'0.35 TeV, 12.6 ab$^{-1}$', 'color':cmap(2), 'hatch':'+'},
        'CEPC': {'annotation':'0.24 TeV, 10 ab$^{-1}$', 'color':cmap(5), 'hatch':'x'},
}

ef08.plot(vals, styles, filename=filename, xlabel=xlabel)
