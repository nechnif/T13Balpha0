# T13Balpha0
This repository contains data from our study "New constraints on radiative seesaw models from IceCube and other neutrino detectors" (arXiv 2103.06881), authored by R. Busse, T. de Boer, A. Kappes, M. Klasen and S. Zeinstra. The data can be used to reproduce the plots in Fig. 5-8. Please cite our paper if you use this for your work.

The file ``t13balpha0_data.txt`` contains the following data for each parameter point:

- ``IC86events``: Number of expected signal events in IceCube (86-string configuration), in units of [1/GeV]
- ``sigpSI``: Spin-independent DM-proton scattering cross section, in units of [pb]
- ``sigpSD``: Spin-dependent DM-proton scattering cross section, in units of [pb]
- ``sig*v``: Velocity-averaged annihilation cross section, in units of [cm^3 s^-1]
- ``mdm``: Mass of the dark matter candidate, in units of [GeV]
- ``DM``: Indicates whether the dark matter candidate is fermionic (``F``) or scalar (``S``).

The ``examples`` directory contains a plotting script ``plot.py`` that generates simplified versions of the plots from our paper.

**We currently can not provide more data, in order to protect an ongoing analysis. We will subsequently upload more data (e.g. annihilation channels) once the respective work is published.**

Contact: michael.klasen@uni-muenster.de
