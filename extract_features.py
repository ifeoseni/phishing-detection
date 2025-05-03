import pandas as pd

# Example placeholder for your actual logic
data = pd.read_csv("data/phishing_urls.csv")
# ... perform feature extraction ...
data['feature_1'] = data['url'].apply(lambda x: len(x))  # Example feature

# Save to output
data.to_csv("output/extracted_features.csv", index=False)
