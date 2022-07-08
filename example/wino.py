#!/usr/bin/env python3
# coding: utf-8

import os
import sys
sys.path.insert(1, os.path.realpath(os.path.pardir))

import matplotlib.cm as mcm
import ef08plot as ef08

xlabel = r'$m(\widetilde{\chi}_2^0)=m(\widetilde{\chi}_1^{\pm})$ [TeV]'
filename = 'wino'

vals = {
        '$\\Delta$m = 10 GeV\n(3-lepton)': {
                    #'ILC500 direct': [0.25, '~$\\sqrt{s}/2$'],
                    #'ILC500 indirect': [0.45, '1504.03402'],
                    #'ILC1000 direct': [0.5, '~$\\sqrt{s}/2$'],
                    #'ILC1000 indirect': [0.7, '1504.03402'],                    
                    'current limits': 0.244, # arxiv: 2106.01676
                    'HL-LHC': [0.532, 'Run-2 Extrapolation'],
                    'HE-LHC': [1.08, 'Run-2 Extrapolation'],
                    'FCC-hh (3/ab)': [1.43, 'Run-2 Extrapolation'],
                    'FCC-hh (30/ab)': [2.53, 'Run-2 Extrapolation'],
                    'ILC500': [[0.25,0.25,0.45,1], '~$\\sqrt{s}/2$, 1504.03402'],
                    'ILC1000': [[0.5,0.5,0.7,1], '~$\\sqrt{s}/2$, 1504.03402'],
                    'CLIC/Muon 3': [1.5, '~$\\sqrt{s}/2$'],
                    #'Muon 3': [1.5, '$\\sqrt{s}/2$'],
                    'Muon 10': [5, '~$\\sqrt{s}/2$'],
                    'Muon 30': [15, '~$\\sqrt{s}/2$'],
                    #'annotation': r'$\widetilde{\chi}_2^0/\widetilde{\chi}_1^{\pm} \to t\widetilde{\chi}_1^0$,qq',
                    
        },
        '$\\Delta$m = 90 GeV\n(3-lepton)': {
                    #'ILC500 direct': [0.25, '~$\\sqrt{s}/2$'],
                    #'ILC500 indirect': [0.45, '1504.03402'],
                    #'ILC1000 direct': [0.5, '~$\\sqrt{s}/2$'],
                    #'ILC1000 indirect': [0.7, '1504.03402'],
                    'current limits': 0.275, # arxiv: 2106.01676
                    'HL-LHC': [0.59, 'Run-2 Extrapolation'],
                    'HE-LHC': [1.20, 'Run-2 Extrapolation'],
                    'FCC-hh (3/ab)': [[1.37,1.37,1.61,0], '1410.6287, Run-2 Extrapolation'],
                    #'ESR FCC_hh 3L': [1.37, '1410.6287'],
                    'FCC-hh (30/ab)': [2.82, 'Run-2 Extrapolation'],
                    'ILC500': [[0.25,0.25,0.45,1], '~$\\sqrt{s}/2$, 1504.03402'],
                    'ILC1000': [[0.5,0.5,0.7,1], '~$\\sqrt{s}/2$, 1504.03402'],
                    'CLIC/Muon 3': [1.5, '~$\\sqrt{s}/2$'],
                    #'Muon 3': [1.5, '~$\\sqrt{s}/2$'],
                    'Muon 10': [5, '~$\\sqrt{s}/2$'],
                    'Muon 30': [15, '~$\\sqrt{s}/2$'],
                    #'annotation': r'$\widetilde{\chi}_2^0/\widetilde{\chi}_1^{\pm} \to t\widetilde{\chi}_1^0$,qq',
                   
        },
        #'$\\Delta$m = 600 ': {
        #            'current limits': 0.651, # arxiv: 2106.01676
        #            'HL-LHC': [1.22, 'Run-2 Extrapolation'],
        #            'HE-LHC': [2.43, 'Run-2 Extrapolation'],
        #            'FCC-hh (3/ab)': [3.88, 'Run-2 Extrapolation'],
        #            #'ESR FCC_hh 3L': [2.56, '1410.6287'],
        #            'FCC-hh (30/ab)': [6.20, 'Run-2 Extrapolation'],
        #            'ILC': [0.5, '~$\\sqrt{s}/2$'],
        #            'CLIC': [1.5, '~$\\sqrt{s}/2$'],
        #            'Muon 3': [1.5, '~$\\sqrt{s}/2$'],
        #            'Muon 10': [5, '~$\\sqrt{s}/2$'],
        #            'Muon 30': [15, '~$\\sqrt{s}/2$'],
                    #'annotation': r'$\widetilde{\chi}_2^0/\widetilde{\chi}_1^{\pm} \to t\widetilde{\chi}_1^0$,qq',
                    #'ESR HL-LHC': [0.886, 'ATL-PHYS-PUB-2018-048'],
        #},
        'Large $\\Delta$m (~750 GeV)\n(all hadronic)      ': {
                    #'ILC500 direct': [0.25, '~$\\sqrt{s}/2$'],
                    #'ILC500 indirect': [0.45, '1504.03402'],
                    #'ILC1000 direct': [0.5, '~$\\sqrt{s}/2$'],
                    #'ILC1000 indirect': [0.7, '1504.03402'],
                    'current limits': 0.96, # arxiv: 2108.07586
                    'HL-LHC': [[1.59,1.59,1.66,0], 'CMS-PAS-FTR-22-001, Run-2 Extrapolation'],
                    'HE-LHC': [3.27, 'Run-2 Extrapolation'],
                    'FCC-hh (3/ab)': [5.84, 'Run-2 Extrapolation'],
                    #'ESR FCC_hh 3L': [4.15, '1410.6287'],
                    'FCC-hh (30/ab)': [8.80, 'Run-2 Extrapolation'],
                    'ILC500': [[0.25,0.25,0.45,1], '~$\\sqrt{s}/2$, 1504.03402'],
                    'ILC1000': [[0.5,0.5,0.7,1], '~$\\sqrt{s}/2$, 1504.03402'],
                    'CLIC/Muon 3': [1.5, '~$\\sqrt{s}/2$'],
                    #'Muon 3': [1.5, '~$\\sqrt{s}/2$'],
                    'Muon 10': [5, '~$\\sqrt{s}/2$'],
                    'Muon 30': [15, '~$\\sqrt{s}/2$'],
                    #'annotation': r'$\widetilde{\chi}_2^0/\widetilde{\chi}_1^{\pm} \to t\widetilde{\chi}_1^0$,qq',
                    #'ESR HL-LHC': [0.886, 'ATL-PHYS-PUB-2018-048'],
        },
}


cmap = mcm.get_cmap('Set3')
styles = {
        'ILC500 direct': {'annotation':'0.5 TeV, 4 ab$^{-1}$', 'color':cmap(1), 'hatch':'|'},
        'ILC500 indirect': {'annotation':'0.5 TeV, 4 ab$^{-1}$', 'color':cmap(1), 'hatch':'\\|'},
        'ILC1000 direct': {'annotation':'1 TeV, 4 ab$^{-1}$', 'color':cmap(6), 'hatch':'o'},
        'ILC1000 indirect': {'annotation':'1 TeV, 4 ab$^{-1}$', 'color':cmap(6), 'hatch':'/o'},
        'ILC500': {'annotation':'0.5 TeV, 4 ab$^{-1}$', 'color':cmap(1), 'hatch':'|'},
        'ILC1000': {'annotation':'1 TeV, 4 ab$^{-1}$', 'color':cmap(6), 'hatch':'\\'},        
        'HL-LHC': {'annotation':'14 TeV, 3 ab$^{-1}$', 'color':cmap(0), 'hatch':None},
        'HE-LHC': {'annotation':'27 TeV, 15 ab$^{-1}$', 'color':cmap(3), 'hatch':'-'},
        'FCC-hh (3/ab)': {'annotation':'100 TeV, 3 ab$^{-1}$', 'color':cmap(2), 'hatch':'--'},
        'FCC-hh (30/ab)': {'annotation':'100 TeV, 30 ab$^{-1}$', 'color':cmap(7), 'hatch':'/'},
        'CLIC': {'annotation':'3 TeV, 5 ab$^{-1}$', 'color':cmap(4), 'hatch':'|'},
        'FCC-ee': {'annotation':'0.35 TeV, 12.6 ab$^{-1}$', 'color':cmap(2), 'hatch':'+'},
        'CEPC': {'annotation':'0.24 TeV, 10 ab$^{-1}$', 'color':cmap(5), 'hatch':'x'},
        'ESR HL-LHC': {'annotation':'14 TeV, 3 ab$^{-1}$', 'color':cmap(8), 'hatch':None},
        'ESR FCC_hh 3L': {'annotation':'100 TeV, 3 ab$^{-1}$', 'color':cmap(14), 'hatch':'.'},
        'CLIC/Muon 3': {'annotation':'TeV, 5/1 ab$^{-1}$', 'color':cmap(4), 'hatch':'\\|'},
        'Muon 3': {'annotation':'TeV, 1 ab$^{-1}$', 'color':cmap(1), 'hatch':'.'},
        'Muon 10': {'annotation':'TeV, 10 ab$^{-1}$', 'color':cmap(5), 'hatch':'x'},
        'Muon 30': {'annotation':'TeV, 10 ab$^{-1}$', 'color':cmap(9), 'hatch':'+'},

}


ef08.plot(filename, xlabel, vals, styles, legend_nrow=4, figsize=(13, 22))
