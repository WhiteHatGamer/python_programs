from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.figure as plt

# using aer's Simulator
simulator = AerSimulator()

# creating Quantum circuit acting on the Q register
circuit = QuantumCircuit(2,2)

# Add H gate on qubit 0
circuit.h(0)

# add cx (CNOT) gate on control qubit 0 and target qubit 1
circuit.cx(0,1)

# Map the quantum measure to clasical bits
circuit.measure([0,1],[0,1])

#Compile the cicuit to support the instuction set  (basis gates)
# and topology (coupling map) of the backend
compiled_circuit = transpile(circuit, simulator)

# excecute the simulator on the aer simulator
job = simulator.run(compiled_circuit, shots = 1000)

# get result from the job
result = job.result()

# print counts
counts = result.get_counts(compiled_circuit)
print("\n Total counts for 00 and 11 are: ",counts)

# draw the circuit
circuit.draw("mpl").savefig("circuit.png", dpi=300)

#plot histogram
plot_histogram(counts).savefig("histogram.png", dpi=300)
