#!/usr/bin/env python
# coding: utf-8

# # Stof

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import figure, draw
from pathlib import Path
sns.set_style('ticks')
sns.set_context("talk")
fn = Path('/Users/madsmikkelsen/Desktop/Stof.pdf').expanduser()

a = np.linspace(0.001,1000,10000)
omega0 = np.linspace(0.98,1.02,3)
omegaa = omega0[0]/((omega0[0]+a*(1-omega0[0])))
omegab = omega0[2]/((omega0[2]+a*(1-omega0[2])))
omegac = 1/((1+a*(1-1)))

f1 = sns.lineplot(x=np.log(a),y=omegaa, color='xkcd:orange')
f2 = sns.lineplot(x=np.log(a),y=omegab, color='xkcd:green')
ax = sns.lineplot(x=np.log(a),y=omegac, color='xkcd:black')
ax.lines[2].set_linestyle("--")

stof = plt.gca()
stof.set_xlim([0.01,3.5])
stof.set_ylim([0.7,1.5])
stof.set_title("Hvilemasse og krumning")
plt.axvline(x=1, color='xkcd:sky blue', ls='-.')

plt.xscale('log')
plt.xlabel('a')
plt.ylabel('$\Omega(a)$')
plt.legend(loc='best', labels=['$\Omega_0=0.98$', '$\Omega_0=1.02$', '$\Omega_0 = 1$'])
plt.rcParams['figure.figsize'] = (12,8)
plt.rcParams['font.size'] = 20
plt.rcParams['legend.fontsize'] = 15

plt.savefig(fn, bbox_inches='tight')
plt.show()


# # Stråling

# In[44]:


sns.set_style('ticks')
sns.set_context("talk")
fn = Path('/Users/madsmikkelsen/Desktop/Stråling.eps').expanduser()

a = np.linspace(1,1000,10000)
omega0 = np.linspace(0.98,1.02,3)
omegad = omega0[0]/((omega0[0]+a**2*(1-omega0[0])))
omegae = omega0[2]/((omega0[2]+a**2*(1-omega0[2])))
omegaf = 1/((1+a**2*(1-1)))

f3 = sns.lineplot(x=np.log(a),y=omegad, color='xkcd:orange')
f4 = sns.lineplot(x=np.log(a),y=omegae, color='xkcd:green')
ax = sns.lineplot(x=np.log(a),y=omegaf, color='xkcd:black')
ax.lines[2].set_linestyle("--")

stof = plt.gca()
stof.set_xlim([0.01,1.8])
stof.set_ylim([0.7,1.5])
stof.set_title("Stråling og krumning")

plt.axvline(x=1, color='xkcd:sky blue', ls='-.')
plt.xscale('log')
plt.xlabel('a')
plt.ylabel('$\Omega(a)$')
plt.legend(loc='best', labels=['$\Omega_0=0.98$', '$\Omega_0=1.02$', '$\Omega_0=1$'])
plt.rcParams['figure.figsize'] = (12,8)
plt.rcParams['font.size'] = 14
plt.rcParams['legend.fontsize'] = 14
plt.savefig('Stof.png', dpi = 1000)

plt.savefig(fn, bbox_inches='tight')
plt.show()


# # Mørk Energi

# In[45]:


sns.set_style('ticks')
sns.set_context("talk")
fn = Path('/Users/madsmikkelsen/Desktop/MørkEnergi.eps').expanduser()

a = np.linspace(0.001,1000,10000)
omega0 = np.linspace(0.98,1.02,3)
omegag = a**2*omega0[0]/((1+(a**2-1)*omega0[0]))
omegah = a**2*omega0[2]/((1+(a**2-1)*omega0[2]))

f5 = sns.lineplot(x=a,y=omegag, color='xkcd:orange')
f6 = sns.lineplot(x=a,y=omegah, color='xkcd:green')

stof = plt.gca()
stof.set_xlim([1,16])
stof.set_ylim([0.98,1.02])
stof.set_title("Mørk energi og krumning")
plt.xlabel('a')
plt.ylabel('$\Omega(a)$')
plt.legend(loc='best', labels=['$\Omega_0=0.98$', '$\Omega_0=1.02$'])
plt.rcParams['figure.figsize'] = (12,8)
plt.rcParams['font.size'] = 14
plt.rcParams['legend.fontsize'] = 14
plt.savefig('Stof.png', dpi = 1000)

plt.savefig(fn, bbox_inches='tight')
plt.show()


# In[ ]:




