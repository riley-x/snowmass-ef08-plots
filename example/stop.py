#!/usr/bin/env python3
# coding: utf-8

import matplotlib.cm as mcm
import ef08plot as ef08

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
