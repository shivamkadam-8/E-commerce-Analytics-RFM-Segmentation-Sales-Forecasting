import pandas as pd

# Load your full CSV
df = pd.read_csv("C:/Users/SK/OneDrive/ドキュメント/ecommerce_project/E-COMMERCE.csv")

# Take a smaller sample (20,000 rows)
df_small = df.sample(20000, random_state=42)

# Save it as a new CSV
df_small.to_csv("C:/Users/SK/OneDrive/ドキュメント/ecommerce_project/E-COMMERCE_SMALL.csv", index=False)

print("Smaller CSV created successfully!")
