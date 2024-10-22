from model import model

# Calculate predictions
predictions = model.predict_proba({
    "device": "works",
    "internet": "poor"
})

# Print predictions for each node
for node, prediction in zip(model.states, predictions):
    if isinstance(prediction, str):
        print(f"{node.name}: {prediction}")
    else:
        print(f"{node.name}")
        for value, probability in prediction.parameters[0].items():
            print(f"    {value}: {probability:.4f}")

print("=================\n")
# Calculate other predictions with 3 facts
predictions = model.predict_proba({
    "device": "fails",
    "internet": "good",
    "platform": "stable"
})

# Print predictions for each node
for node, prediction in zip(model.states, predictions):
    if isinstance(prediction, str):
        print(f"{node.name}: {prediction}")
    else:
        print(f"{node.name}")
        for value, probability in prediction.parameters[0].items():
            print(f"    {value}: {probability:.4f}")
