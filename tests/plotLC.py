import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import grbpy as grb

day = 86400.0

jetType = 0
specType = 0
thV = 0.4
E0 = 1.0e53
thC = 0.1
thW = 0.3
n0 = 1.0
p = 2.15
epse = 1.0e-1
epsB = 1.0e-2
ksiN = 1.0
dL = 1.96e27


Y = np.array([thV, E0, thC, thW, n0, p, epse, epsB, ksiN, dL])

ta = 1.0e1 * day
tb = 1.0e2 * day
t = np.logspace(np.log10(ta), np.log10(tb), base=10.0, num=10)

nuR  = np.empty(t.shape)
nuO  = np.empty(t.shape)
nuX  = np.empty(t.shape)

nuR[:] = 6.0e9
nuO[:] = 1.0e14
nuX[:] = 1.0e18

print("Calc Radio")
FnuR = grb.fluxDensity(t, nuR, jetType, specType, *Y)
print(FnuR.min(), FnuR.max())
print("Calc Optical")
FnuO = grb.fluxDensity(t, nuO, jetType, specType, *Y)
print(FnuO.min(), FnuO.max())
print("Calc X-ray")
FnuX = grb.fluxDensity(t, nuX, jetType, specType, *Y)
print(FnuX.min(), FnuX.max())

c = ["tab:blue", "tab:orange", "tab:green", "tab:red", "tab:purple"]
ls = ["-", "--", ":"]

td = t/day

print("Plot")
fig, ax = plt.subplots(1,1)
ax.plot(td, FnuR, color='tab:green')
ax.plot(td, FnuO, color='tab:blue')
ax.plot(td, FnuX, color='tab:purple')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel(r'$t$ (d)')
ax.set_ylabel(r'$F_\nu$ (mJy)')
fig.savefig("lc.png")
plt.close(fig)
