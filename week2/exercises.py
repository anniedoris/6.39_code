import numpy as np

## Question 1
print("QUESTION 1")
theta = np.array([[1, -1, 2, -3]]).T
option1 = np.array([[1, -1, 2, -3]])
option2 = np.array([[1, 2, 3, 4]])
option3 = np.array([[-1, -1, -1, -1]])
option4 = np.array([[1, 1, 1, 1]])

print(option1@theta)
print(option2@theta)
print(option3@theta)
print(option4@theta)

## Answer: 1 and 3

## Question 2
## Answer 2a: yes, it is the same hyperplane, because a hyperplane is defined as theta dot x = 0. If you have a multiple, it is the same hyperplane
## Answer 2b: no, it is not the SAME classifier

## Question 3
# Linear separable means that there exists a theta where the training error will be zero, but that is NOT true for the test set

## Question 4
# Points that are not linear separable through the origin but are linear separable include those on the positive x axis with differnt labels