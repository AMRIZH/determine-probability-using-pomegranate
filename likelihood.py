from model import model

# Calculate probability for a given observation
probability = model.probability([["heavy", "no", "delayed","attend"]])

print(probability)