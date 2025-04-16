# Hodgkin-Huxley Neuron Simulation 
The simulation of the generation of action potentials in a neuron using the **Hodgkin-Huxley model**. It captures how membrane potential evolves due to ion channel dynamics, modeling the ionic currents responsible for neuronal firing.

### Overview 
The rate of change of the membrane potential is governed by the current flowing across the membrane and the cell's capacitance.
```
dv/dt = i / c
```
The membrane is depolarized and repolarized by ion channel activity, specifically potassium $(K^+)$ and sodium $(Na^+)$ channels, along with a passive leak channel. Ionic currents are modeled as:
```
I = G * (V - E)
```
Where:
+ $G$ is the ion channel conductance (voltage dependent)
+ $V$ is the membrane potential
+ $E$ is the reverse potential for the ion
  
Three different gates are used to simulate time evolution of voltage:
+ Potassium - ``` n ``` gate
+ Sodium - ``` m ``` and ```h``` gates
+ Leak channel

It implements voltage-dependent rate equations for channel gating variables and injects a step current into the neuron and tracks the resulting action potential.

### Biophysical Model Details
**Gating Dynamics** : Each gate (```n```, ```m```, ```h```) follows a first-order differential equation representing open/close probabilties.
```math
\frac {dn}{dt} = \alpha_n * (1 - n) - \beta_n * n
```
Rate constants ($\alpha$ and $\beta$) depend on voltage and determine the speed of gate transitions.
**Channels**
+ Potassium $(K^+)$ : $n^4$ dependence for conductance.
+ Sodium $(Na^+)$ : $m^3h$ dependence for conductance.
+ Leak channel : passive, constant conductance.

### Simulation Output
The simulation plots membrane potential (V) vs. time (s) showing action potential behavior in response to current injection.
 <p align="center">
   <img src="https://github.com/user-attachments/assets/6cae7fff-ff77-48ef-a42f-6136e4e56858" alt="Gesturon" width=70%>
 </p>
