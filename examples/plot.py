#!/usr/bin/env python3
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

data = np.loadtxt('t13balpha0_data.txt', dtype=str, unpack=True)

IC86events = np.array([float(i) for i in data[0]])
sigpSI     = np.array([float(i) for i in data[1]])
sigpSD     = np.array([float(i) for i in data[2]])
sigv       = np.array([float(i) for i in data[3]])
mdm        = np.array([float(i) for i in data[4]])
DM         = data[5]


def mscatter(x,y,ax=None, m=None, **kw):
    import matplotlib.markers as mmarkers
    if not ax: ax=plt.gca()
    sc = ax.scatter(x,y,**kw)
    if (m is not None) and (len(m)==len(x)):
        paths = []
        for marker in m:
            if isinstance(marker, mmarkers.MarkerStyle):
                marker_obj = marker
            else:
                marker_obj = mmarkers.MarkerStyle(marker)
            path = marker_obj.get_path().transformed(
                        marker_obj.get_transform())
            paths.append(path)
        sc.set_paths(paths)
    return sc


cmap = matplotlib.cm.get_cmap('tab10', 10).colors
colors, markers = [], []
for m, mass in enumerate(mdm):
    if DM[m] == 'F':
        colors.append(cmap[2])
        markers.append('^')
    else:
        colors.append(cmap[6])
        markers.append('s')


plt.rcParams.update({
    'font.family': 'stix',
    'mathtext.fontset': 'stix',
    'font.size': 16,
    'legend.fontsize': 11,
    'legend.title_fontsize': 13,
})
fig1, ax1 = plt.subplots(1, 1)
fig1.subplots_adjust(bottom=0.12, top=0.95, left=0.13, right=0.96)

ax1.yaxis.set_ticks_position('both')
ax1.xaxis.set_ticks_position('both')
ax1.tick_params(axis='both', which='both', direction='in', labelsize=13)
# ax1.grid(which='major', ls='--', alpha=0.3)
ax1.grid(which='both', ls='--', alpha=0.3)

ax1.set_axisbelow(True)
ax1.set_xscale('log')
ax1.set_xlabel(r'$m_{\mathrm{DM}}$ [GeV]')
ax1.set_xlim(3e1, 4e3)
ax1.set_yscale('log')


#--- uncomment your favorite plot below --------------------------------

#--- mDM vs sigpSI: ---
mscatter(mdm, sigpSI, ax=ax1, s=15, color='none', edgecolor=colors, m=markers)
ax1.set_ylabel(r'$\sigma_{p}(SI)$ [pb]')
ax1.set_ylim(1e-20, 1e-3)
ax2 = ax1.twinx()
ax2.set_ylabel(r'$\sigma_{p}(SI)$ [cm$^{2}$]')
ax2.set_yscale('log')
ax2.set_ylim(1e-56, 1e-39)
ax2.tick_params(axis='both', which='both', direction='in', labelsize=13)
fig1.subplots_adjust(bottom=0.12, top=0.95, left=0.13, right=0.87)
outfile = 't13balpha0_mdm-sigpSI.png'

#--- mDM vs sigpSD: ---
# mscatter(mdm, sigpSD, ax=ax1, s=15, color='none', edgecolor=colors, m=markers)
# ax1.set_ylabel(r'$\sigma_{p}(SD)$ [pb]')
# ax1.set_ylim(1e-13, 1e-1)
# ax2 = ax1.twinx()
# ax2.set_ylabel(r'$\sigma_{p}(SI)$ [cm$^{2}$]')
# ax2.set_yscale('log')
# ax2.set_ylim(1e-56, 1e-39)
# ax2.tick_params(axis='both', which='both', direction='in', labelsize=13)
# fig1.subplots_adjust(bottom=0.12, top=0.95, left=0.13, right=0.87)
# outfile = 't13balpha0_mdm-sigpSD.png'

#--- mDM vs sigv: ---
# mscatter(mdm, sigv, ax=ax1, s=15, color='none', edgecolor=colors, m=markers)
# ax1.set_ylabel(r'$\langle \sigma v\rangle$ [cm$^{3}$ s$^{-1}$]')
# ax1.set_ylim(5e-33, 1e-21)
# outfile = 't13balpha0_mdm-sigv.png'

#--- mDM vs IC86: ---
# mscatter(mdm, IC86events, ax=ax1, s=15, color='none', edgecolor=colors, m=markers)
# ax1.axhline(1e0, color='grey', ls='--')
# ax1.set_ylabel(r'IC86 events [year]$^{-1}$')
# ax1.set_ylim(1e-4, 1e3)
# outfile = 't13balpha0_mdm-IC86.png'


colors_, markers_ = [2, 6], ['^', 's']
labels = ['fermionic DM', 'scalar DM']
leg1  = [matplotlib.lines.Line2D([0], [0], color='none', markeredgecolor=cmap[colors_[l]], linestyle='none', markersize=8, marker=m, label=label) for l, m, label in zip(range(len(labels)), markers_, labels)]
leg1_ = ax1.legend(handles=leg1, loc='best', ncol=1, framealpha=0.9)

fig1.savefig(outfile, dpi=200)
