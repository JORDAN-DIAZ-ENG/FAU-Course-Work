import matplotlib.pyplot as plt

c1x = [1, 3, 2]
c1y = [1, 2, 3]

plt.scatter(c1x, c1y, label="Class 1", marker="s")

c2x = [1, 2, 2]
c2y = [2, 2, 1]

plt.scatter(c2x, c2y, label="Class 2")

plt.title("Problem 2")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.legend()
plt.show()

for i in range(0, 3):

    thx = float(input("Please enter threshold x: "))
    thy = float(input("please enter threshold y: "))

    # In this problem assume that for any data point if x > thx and y > thy the data sample belongs to Class C1
    c1 = (1, 1), (3, 2), (2, 3)
    c2 = (1, 2), (2, 2), (2, 1)
    points = (1, 1), (3, 2), (2, 3), (1, 2), (2, 2), (2, 1)
    correct = 0

    for xy in points:
        if xy[0] > thx and xy[1] > thy and xy in c1:
            correct += 1
        elif xy[0] <= thx and xy[1] <= thy and xy in c2:
            correct += 1

    print("The Classification Accuracy is: ", correct / len(points))
