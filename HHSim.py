# The rate at which the membrane potential changes is equal to the
    #current flowing divided by the cell capacitance 
                    # dv/dt = i/C 

#We care about how the membrane *changes* not what it actually is

#adding ion channels is important as they depolarize and repolarize 
    #I=G(V-E) conductance of chanel * driving force 
    #                    (membrane potential - reveral potential)
    #EPSP must depolarize so ion channel current is opposite to 
    #                       membrance capacitor current

#Adding action potential using the Hodgkin and Huxley model

        # Open(n) - A -> Closed(1-n) 
        # open channels turn into closed at rate A
        # proportion of open channels is n and its inverse, closed, 1-n
        #   dn/dt = -A * n (faster the decay the more n or A)

        # Open(n) <- B - Closed(1-n) 
        # closed channels turn into open at rate B
        #   dn/dt = B * (1-n) (1-n is the proportion of closed channels)

        # Open(n) <- A,B -> Closed(1-n) 
        # bidirectional, channels go from open to closed and vice versa
        #   dn/dt = B * (1-n) - A * n

        # A and B (rate constants) are not constant, they vary with the
            #voltage 

    # Adding the sodium NA channel -- it has 2 gating particles m and h 
        # m is activation particle, opens at depolarization 
        # n is inactivation particle, closes at depolarization 
        # => m opens faster than n closes which gives it the transient 
        #                       nature


import matplotlib.pyplot as plt
import numpy as np
import math

def B_n(v):
    v = v*1000
    return 0.01 * (-v-55)/( math.exp((-v-55)/10.0) -1) * 1000

def A_n(v):
    v = v*1000
    return 0.125*math.exp((-v-65)/80.0) * 1000

def B_m(v):
    v = v*1000
    return 0.1 * (-v-40)/(math.exp((-v-40)/10.0) -1) * 1000

def A_m(v):
    v = v*1000
    return 4 * math.exp((-v-65)/18.0) * 1000

def B_h(v):
    v = v*1000
    return 0.07 * math.exp((-v-65)/20.0) * 1000

def A_h(v):
    v = v*1000
    return 1/(math.exp((-v-35)/10.0) +1)* 1000


dt = 10E-6

C = 100E-12
V_initial = -70E-3 

n = B_n(V_initial)/(B_n(V_initial)+A_n(V_initial))
m = B_m(V_initial)/(B_m(V_initial)+A_m(V_initial))
h = B_h(V_initial)/(B_h(V_initial)+A_h(V_initial))

G_max_k = 1E-6
G_max_na = 7E-6
Gleak = 5E-9

Ek = -80E-3
Ena = 40E-3
Eleak = -70E-3

current_magnitude = 200E-12

i_injected = np.concatenate( (np.zeros([round(0.2/dt), 1]),
                              current_magnitude*np.ones([round(0.3/dt), 1]),
                              np.zeros([round(0.5/dt), 1])))

Volt = np.zeros(np.size(i_injected))

for t in range(np.size(Volt)):
    if t == 1:
        Volt[t]=V_initial
    else:
        dn = (B_n(Volt[t-1]) * (1-n) - A_n(Volt[t-1]) * n) * dt
        n = n + dn 

        dm = (B_m(Volt[t-1]) * (1-m) - A_m(Volt[t-1]) * m) * dt
        m = m + dm 

        dh = (B_h(Volt[t-1]) * (1-h) - A_h(Volt[t-1]) * h) * dt
        h = h + dh 

        Gk = G_max_k * n * n * n * n
        i_k = Gk*(Volt[t-1] - Ek)

        Gna = G_max_na * m * m * m * h
        i_na = Gna*(Volt[t-1] - Ena)

        i_leak = Gleak * (Volt[t-1] - Eleak)
        i_capacitance = i_injected[t] - i_k - i_na - i_leak
        
        dv=i_capacitance/C*dt
        Volt[t] = Volt[t-1] + dv

t_vector = np.linspace(0, dt*np.size(Volt), np.size(Volt))
plt.plot(t_vector, Volt)
plt.xlabel('Time(s)')
plt.ylabel('Membrance Potential (V)')
plt.show()
