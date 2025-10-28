import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
data = {'Milk': [0, 0, 1, 0, 1],
'Bread': [1, 1, 1, 1, 0],
'Butter': [1, 1, 1, 0, 0],
'Eggs': [1, 0, 0, 0, 0],
'Coke': [0, 0, 0, 1, 1], }
df = pd.DataFrame(data)
frequent_itemsets = apriori(df, min_support=0.3, use_colnames=True)
rules = association_rules(frequent_itemsets,
metric="confidence",min_threshold=0.3)
print("Frequent Itemsets:\n", frequent_itemsets)
print("\nAssociation Rules:\n", rules[['antecedents',
'consequents','support', 'confidence']])