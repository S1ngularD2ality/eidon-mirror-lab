def threshold_gate(energy, threshold=50):
    if energy >= threshold:
        return "Enter"
    else:
        return "Wait"

# Test
print(threshold_gate(75))          # Enter
print(threshold_gate(49))          # Wait
print(threshold_gate(50))          # Enter
print(threshold_gate(33, 30))      # Enter
print(threshold_gate(33, 40))      # Wait
