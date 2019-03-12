from math import pi, sqrt, e


true = [pi, pi, pi, pi, sqrt(2), e]
est = [3, 3.05, 3.14, 3.1416, 1.414, 2.718]

for i , (t, e) in enumerate(zip(true, est)):
    print("({}): 絶対誤差{}, 相対誤差{}".format(i+1, abs(t-e), abs((t-e)/t)))
