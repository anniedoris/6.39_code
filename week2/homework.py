import numpy as np

## Question 1
print("QUESTION 1")
# I answered question 1 by evaluating the below perceptron implementation in various ways
def perceptron_algorithm(data, ys, num_its):
    theta = np.array([[1, 1]]).T
    count_mistake = 0
    for i in range(num_its):
        all_correct = True
        for j in range(data.shape[0]):
            x_i = data[j:j+1, :]
            y_i = ys[j:j+1, :]
            if y_i*(x_i@theta) <= 0:
                print("new theta")
                theta = theta + (y_i*x_i).T
                print(theta)
                count_mistake += 1
                all_correct = False
        if all_correct:
            return theta, count_mistake, i
    return theta, count_mistake, i

data = np.array([[1, -1], [0, 1], [-1.5, -1]])
ys = np.array([[1], [-1], [1]])

th, mistake, it = perceptron_algorithm(data, ys, 10)
print(f"Mistakes: {mistake}")
print(f"Iterations: {it}")

## Question 2
print("QUESTION 2")
# 2.1: initializing with larger values means it takes longer to converge, since relative corrections have smaller impaces
# 2.2: TODO how would you find these in a non trial and error way?

## Question 3
print("QUESTION 3")
# I answered question 1 by evaluating the below perceptron implementation in various ways
def perceptron_not_through_origin_algorithm(data, ys, num_its):
    theta = np.array([[0, 0]]).T
    theta_0 = np.array([[0]])
    count_mistake = 0
    for i in range(num_its):
        all_correct = True
        for j in range(data.shape[0]):
            x_i = data[j:j+1, :]
            y_i = ys[j:j+1, :]
            if y_i*(x_i@theta + theta_0) <= 0:
                print("new theta")
                theta = theta + (y_i*x_i).T
                theta_0 = theta_0 + y_i
                print(theta)
                count_mistake += 1
                all_correct = False
        if all_correct:
            return theta, theta_0, count_mistake, i
    return theta, theta_0, count_mistake, i

data = np.array([[-3, 2], [-1, 1], [-1, -1], [2, 2], [1, -1]])
ys = np.array([[1], [-1], [-1], [-1], [-1]])

th, th0, mistake, it = perceptron_not_through_origin_algorithm(data, ys, 10)
print(f"Mistakes: {mistake}")
print(f"Iterations: {it}")
print(f"Final thetas: {th}")
print(f"Final theta 0: {th0}")

## Question 4
print("QUESTION 4")
# I answered question 1 by evaluating the below perceptron implementation in various ways
def perceptron_algorithm(data, ys, num_its):
    theta = np.array([[0, 0, 0]]).T
    count_mistake = 0
    for i in range(num_its):
        all_correct = True
        for j in range(data.shape[0]):
            x_i = data[j:j+1, :]
            y_i = ys[j:j+1, :]
            if y_i*(x_i@theta) <= 0:
                print("new theta")
                theta = theta + (y_i*x_i).T
                print(theta)
                count_mistake += 1
                all_correct = False
        if all_correct:
            return theta, count_mistake, i
    return theta, count_mistake, i

data = np.array([[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]])
ys = np.array([[-1], [-1], [-1], [-1], [-1], [-1], [-1], [1]])
th, mistake, it = perceptron_algorithm(data, ys, 100)
print(f"Mistakes: {mistake}")
print(f"Iterations: {it}")
print(f"Final thetas: {th}")

def perceptron_not_through_origin_algorithm(data, ys, num_its):
    theta = np.array([[0, 0, 0]]).T
    theta_0 = np.array([[0]])
    count_mistake = 0
    for i in range(num_its):
        all_correct = True
        for j in range(data.shape[0]):
            x_i = data[j:j+1, :]
            y_i = ys[j:j+1, :]
            if y_i*(x_i@theta + theta_0) <= 0:
                print("new theta")
                theta = theta + (y_i*x_i).T
                theta_0 = theta_0 + y_i
                print(theta)
                count_mistake += 1
                all_correct = False
        if all_correct:
            return theta, theta_0, count_mistake, i
    return theta, theta_0, count_mistake, i

th, th0, mistake, it = perceptron_not_through_origin_algorithm(data, ys, 100)
print(f"Mistakes: {mistake}")
print(f"Iterations: {it}")
print(f"Final thetas: {th}")
print(f"Final theta 0: {th0}")