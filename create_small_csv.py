Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import pandas as pd
... 
... # Load your full CSV (the 45 MB file)
... df = pd.read_csv("C:/Users/SK/OneDrive/ドキュメント/ecommerce_project/E-COMMERCE.csv")
... 
... # Take a smaller sample (e.g., 20,000 rows)
... df_small = df.sample(20000, random_state=42)
... 
... # Save the smaller CSV (overwrite or new file)
... df_small.to_csv("C:/Users/SK/OneDrive/ドキュメント/ecommerce_project/E-COMMERCE.csv", index=False)
... 
... print("Smaller CSV created successfully!")
>>> [DEBUG ON]
>>> [DEBUG OFF]
