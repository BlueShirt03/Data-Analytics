import pandas as pd
import numpy as np
from scipy import stats

# Sample data
np.random.seed(42)
data = {
    'Strategy': ['A'] * 1000 + ['B'] * 1000,
    'ClickThrough': np.concatenate([
        np.random.normal(0.05, 0.02, 1000),  # Strategy A
        np.random.normal(0.06, 0.02, 1000)   # Strategy B
    ])
}

df = pd.DataFrame(data)

# Separate the data for each strategy
strategy_a = df[df['Strategy'] == 'A']['ClickThrough']
strategy_b = df[df['Strategy'] == 'B']['ClickThrough']

# Perform t-test
t_statistic, p_value = stats.ttest_ind(strategy_a, strategy_b)

print(f"T-statistic: {t_statistic}")
print(f"P-value: {p_value}")

# Interpret the results
alpha = 0.05
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference between the two strategies.")
else:    
    print("Fail to reject the null hypothesis: There is no significant difference between the two strategies.")