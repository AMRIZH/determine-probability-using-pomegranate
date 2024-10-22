from pomegranate import Node, DiscreteDistribution, ConditionalProbabilityTable, BayesianNetwork

# Internet node has no parents
internet = Node(DiscreteDistribution({
    "good": 0.6,
    "poor": 0.4
}), name="internet")

# Platform node is conditional on Internet
platform = Node(ConditionalProbabilityTable([
    ["good", "stable", 0.4],
    ["good", "unstable", 0.6],
    ["poor", "stable", 0.2],
    ["poor", "unstable", 0.8]
], [internet.distribution]), name="platform")

# device node is conditional on internet and platform
device = Node(ConditionalProbabilityTable([
    ["good", "stable", "works", 0.8],
    ["good", "stable", "fails", 0.2],
    ["good", "unstable", "works", 0.9],
    ["good", "unstable", "fails", 0.1],
    ["poor", "stable", "works", 0.6],
    ["poor", "stable", "fails", 0.4],
    ["poor", "unstable", "works", 0.7],
    ["poor", "unstable", "fails", 0.3]
], [internet.distribution, platform.distribution]), name="device")

# exam node is conditional on device
exam = Node(ConditionalProbabilityTable([
    ["works", "participate", 0.9],
    ["works", "miss", 0.1],
    ["fails", "participate", 0.6],
    ["fails", "miss", 0.4]
], [device.distribution]), name="exam")

# Create a Bayesian Network and add states
model = BayesianNetwork()
model.add_states(internet, platform, device, exam)

# Add edges connecting nodes
model.add_edge(internet, platform)
model.add_edge(internet, device)
model.add_edge(platform, device)
model.add_edge(device, exam)

# Finalize model
model.bake()
