"""Plot the exactly soluble local probe; no simulation or hardness claim."""
from pathlib import Path
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
u = np.linspace(0, 2, 500)
mf = 1 / np.cosh(u)
bare = np.cos(u)
with plt.rc_context({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False,'svg.fonttype':'path'}):
    fig, ax = plt.subplots(figsize=(7.4,4.3), layout='constrained')
    ax.plot(u,mf,color='#087f8c',lw=2.6,label='Self-consistent: sech(u)')
    ax.plot(u,bare,color='#bd5b35',lw=2.3,label='Feedback-free: cos(u)')
    ax.vlines(2,bare[-1],mf[-1],color='#5a6772',lw=1.2,ls='--')
    ax.scatter([2,2],[mf[-1],bare[-1]],c=['#087f8c','#bd5b35'],s=28,zorder=4)
    ax.text(1.95,0.10,'Δz = 0.682',ha='right',color='#33414b',fontsize=10)
    ax.set(xlabel='Dimensionless probe time  u = λt',ylabel='Centered occupation  z',xlim=(0,2.08),ylim=(-0.5,1.08))
    ax.set_title('An exactly soluble, active mean-field response',loc='left',pad=14,fontsize=14)
    ax.grid(alpha=.16)
    ax.legend(frameon=False,loc='lower left')
    (ROOT/'assets').mkdir(parents=True,exist_ok=True)
    fig.savefig(ROOT/'assets/feedback-probe.svg',metadata={'Date':None,'Creator':'Exact analytical probe functions'})
    if '--preview' in sys.argv:
        fig.savefig(ROOT/'assets/feedback-probe-preview.png',dpi=150)
    plt.close(fig)
print('Wrote assets/feedback-probe.svg.')
