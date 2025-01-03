from brian2 import *

# Set preferences for code generation
prefs.codegen.target = 'numpy'  # Explicitly use numpy backend

# Simulation parameters
tau = 10*ms
eqs = '''
dv/dt = (1-v)/tau : 1
'''

# Set up the neuron group
G = NeuronGroup(1, eqs)
G.v = 0  # Set initial condition explicitly

# Run simulation
print('Before v = %s' % G.v[0])
run(100*ms)
print('After v = %s' % G.v[0])