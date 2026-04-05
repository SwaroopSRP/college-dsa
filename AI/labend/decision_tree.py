from sklearn.tree import DecisionTreeClassifier

# Features: [has_link, has_offer_words, unknown_sender]
X = [
    [1, 1, 1],
    [1, 0, 1],
    [0, 1, 1],
    [0, 0, 0],
    [1, 1, 0],
    [0, 0, 0]
]

# Labels: 1 = Spam, 0 = Not Spam
y = [1, 1, 1, 0, 1, 0]

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# New email: no link, no offer words, known sender
new_email = [[0, 0, 0]]

prediction = model.predict(new_email)

print("Prediction:", prediction[0])
print("Spam" if prediction[0] == 1 else "Not Spam")

"""
1. import
2. model create
3. fit(X, y)
4. predict()
"""
