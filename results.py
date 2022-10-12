inp = input("Enter score between 0.0 and 1.0:")
score = float(inp)

if score >= 0.9 and score <= 1.0:
    print("A")
if score >= 0.8 and score < 0.9:
    print("B")
if score >= 0.7 and score < 0.8:
    print("C")
if score >= 0.6 and score < 0.7:
    print("D")
if score >= 0.0 and score <0.6:
    print("F")
elif score > 1.0:
    print("Error, please enter score between 0.0 and 1.0")
    quit()