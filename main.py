import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv('data.csv')


data['tail'] = data['tail'].map({'Yes': 1, 'No': 0})

X = data[['message', 'fingers', 'tail']]
y = data['species']

tfidf = TfidfVectorizer(max_features=100)
X_text = tfidf.fit_transform(X['message'])


X_combined = pd.concat(
    [pd.DataFrame(X_text.toarray()), X[['fingers', 'tail']].reset_index(drop=True)],
    axis=1
)


X_combined.columns = X_combined.columns.astype(str)


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_combined, y)


test_data = pd.read_csv('test.csv')

test_data['tail'] = test_data['tail'].map({'Yes': 1, 'No': 0})


X_test_text = tfidf.transform(test_data['message'])
X_test_combined = pd.concat(
    [pd.DataFrame(X_test_text.toarray()), test_data[['fingers', 'tail']].reset_index(drop=True)],
    axis=1
)


X_test_combined.columns = X_test_combined.columns.astype(str)


test_predictions = model.predict(X_test_combined)


result = pd.DataFrame({'Species': test_predictions})
result.to_csv('result.csv', index=False)
