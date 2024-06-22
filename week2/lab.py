## Question 1
# A) We want to see that the classifier/hypothesis generalizes to data that the model hasn't seen before.
# B) eval_classifier(h, D_test). It measures performance on the test set! Range would still be 0 to 1
# C) This allows us to see how the model generalizes.
# D) It would probably have a lower score.

## Question 2
# A) This would not produce the same classifier!
# B) The train and test sets may be very disjoint, so the hypothesis might not perform well on the test set
# C) This method is better? This will give you a better sense on how the model will generalize
# D) Would be better to do k fold cross validation, since you train multiple times and data is less fixed to that specific training set
# E) Above?

## Question 3
# You could do k fold validation, where you train on everything but a k fold. This allows for more generalizability while repurposing data.