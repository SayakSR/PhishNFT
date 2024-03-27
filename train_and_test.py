import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_validate
import matplotlib.pyplot as plt
import numpy as np
import os
import joblib  

data = pd.read_csv('data/groundtruth.csv')  # Groundtruth data

# Feature set
X = data[['matches_official_slug_url', 'If_official_contract_address', 'No_of_ether_addresses', 'Twitter_link', 'if_twitter_active', 'Twitter_match', 'Followers', 'Age', 'Opensea_match', 'eth_tracker']]

# 1=malicious, 0=benign
y = data['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)

# perform 10-fold cross validation
cv_results = cross_validate(clf, X_train, y_train, cv=10, scoring=['accuracy', 'precision', 'recall', 'f1', 'roc_auc'])

# Metrics
print("Precision: ", cv_results['test_precision'].mean())
print("Recall: ", cv_results['test_recall'].mean())
print("F1 Score: ", cv_results['test_f1'].mean())
print("AUC: ", cv_results['test_roc_auc'].mean())

# train the model on the training data
clf.fit(X_train, y_train)

# Generate feature importance
importances = clf.feature_importances_

importance_dict = dict(zip(X.columns, importances))
print(importance_dict)

# Create feature importance plot
features = ['matches_official_slug_url', 'If_official_contract_address', 'No_of_ether_addresses', 'Twitter_link', 'if_twitter_active', 'Twitter_match', 'Followers', 'Age', 'Opensea_match', 'eth_tracker']
indices = np.argsort(importances)[::-1]
names = [features[i] for i in indices]

plt.figure(figsize=(12, 8))

plt.barh(range(len(features)), importances, color='#0343DF', edgecolor='black', hatch='/')
plt.yticks(range(len(features)), features)

plt.xlabel('Importance')
plt.ylabel('Features')

plt.gca().invert_yaxis()

plt.tight_layout()

plt.savefig('feature_importance.png', bbox_inches='tight')

# Check if 'model' directory exists
if not os.path.exists('model'):
    os.makedirs('model')

# Save the model
joblib.dump(clf, 'model/model.joblib')

