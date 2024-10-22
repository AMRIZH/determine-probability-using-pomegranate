from model import model

# Calculate probability for a given observation
probability = model.probability([["poor", "unstable", "fails", "miss"]])

print(probability, "\n")

# Possible states for each node
internet_states = ["good", "poor"]
platform_states = ["stable", "unstable"]
device_states = ["works", "fails"]
exam_states = ["participate", "miss"]

# Calculate and print probabilities for all combinations
for internet_state in internet_states:
    for platform_state in platform_states:
        for device_state in device_states:
            for exam_state in exam_states:
                probability = model.probability(
                    [[internet_state, platform_state, device_state, exam_state]])
                print(
                    f"Probability of [{internet_state}, {platform_state}, {device_state}, {exam_state}]: {probability:.4f}")
