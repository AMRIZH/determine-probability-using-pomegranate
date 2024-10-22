from model import model

# Calculate probability for a given observation
probability = model.probability([["poor", "unstable", "fails", "miss"]])

print(probability)
