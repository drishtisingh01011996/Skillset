import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Number of samples
n_samples = 200

# Generate data
data = {
    # Numerical: Gene A expression (log-normal distribution, typical for gene expression)
    "gene_expression": np.random.lognormal(mean=2, sigma=0.5, size=n_samples),
    
    # Categorical: Sample type (60% Tumor, 40% Normal)
    "sample_type": np.random.choice(["Tumor", "Normal"], size=n_samples, p=[0.6, 0.4]),
    
    # Numerical: Patient age (normal distribution, mean=55, sd=10)
    "patient_age": np.random.normal(loc=55, scale=10, size=n_samples).astype(int),
    
    # Datetime: Collection date (random dates in 2023-2024)
    "collection_date": [datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 730)) 
                        for _ in range(n_samples)],
    
    # Numerical: Gene B expression (correlated with Gene A for realism)
    "gene_b_expression": np.random.lognormal(mean=2, sigma=0.5, size=n_samples) * 0.7 + 
                         np.random.lognormal(mean=2, sigma=0.5, size=n_samples) * 0.3,
    
    # Categorical: Tumor stage (only for Tumor samples, Normal for others)
    "tumor_stage": ["Normal"] * n_samples
}

# Assign tumor stages to Tumor samples
tumor_indices = np.where(data["sample_type"] == "Tumor")[0]
data["tumor_stage"] = np.array(data["tumor_stage"])
data["tumor_stage"][tumor_indices] = np.random.choice(
    ["Stage I", "Stage II", "Stage III"], size=len(tumor_indices), p=[0.4, 0.4, 0.2]
)

# Create DataFrame
df = pd.DataFrame(data)

# Adjust gene expression for realism (e.g., higher in Tumor samples)
df.loc[df["sample_type"] == "Tumor", "gene_expression"] *= 1.5
df.loc[df["sample_type"] == "Tumor", "gene_b_expression"] *= 1.3

# Save to CSV in a data folder
df.to_csv("data/gene_expression_cancer.csv", index=False)

# Preview
print(df.head())
print(df.dtypes)
