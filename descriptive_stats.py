"""
================================================
  Basic Descriptive Statistics — Iris Dataset
  Tools: Python, Pandas, Seaborn
================================================
"""

import pandas as pd
from sklearn.datasets  import load_iris

# ── 1. Load Dataset ──────────────────────────────────────────────
print("\n" + "=" * 55)
print("       BASIC DESCRIPTIVE STATISTICS — IRIS DATASET")
print("=" * 55)

iris = load_iris(as_frame=True)
df = iris.frame
df["species"] = df["target"].map({0: "setosa", 1: "versicolor", 2: "virginica"})
df = df.drop(columns="target")
df.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]

print(f"\n📦 Dataset loaded successfully!")
print(f"   Shape : {df.shape[0]} rows × {df.shape[1]} columns")
print(f"   Columns: {list(df.columns)}\n")

# ── 2. First look ────────────────────────────────────────────────
print("─" * 55)
print("🔍 First 5 Rows (df.head())")
print("─" * 55)
print(df.head().to_string(index=False))

# ── 3. Pandas describe() — Full Summary ─────────────────────────
print("\n" + "─" * 55)
print("📊 Full Summary — df.describe()")
print("─" * 55)
print(df.describe().round(2).to_string())

# ── 4. Manual Calculations — Numeric Columns Only ────────────────
numeric_cols = df.select_dtypes(include="number").columns

print("\n" + "─" * 55)
print("🧮 Manual Calculations per Column")
print("─" * 55)

stats = pd.DataFrame({
    "Mean"   : df[numeric_cols].mean(),
    "Median" : df[numeric_cols].median(),
    "Std Dev": df[numeric_cols].std(),
    "Min"    : df[numeric_cols].min(),
    "Max"    : df[numeric_cols].max(),
}).round(3)

print(stats.to_string())

# ── 5. Species-wise Breakdown ────────────────────────────────────
print("\n" + "─" * 55)
print("🌸 Mean per Species (groupby)")
print("─" * 55)
print(df.groupby("species")[numeric_cols].mean().round(2).to_string())

# ── 6. Key Observations ─────────────────────────────────────────
print("\n" + "─" * 55)
print("💡 Key Observations")
print("─" * 55)

for col in numeric_cols:
    mean = df[col].mean()
    std  = df[col].std()
    mn   = df[col].min()
    mx   = df[col].max()
    print(f"  {col:<20} | mean={mean:.2f}, std={std:.2f}, range=[{mn}, {mx}]")

print("\n" + "=" * 55)
print("  ✅ Analysis Complete!")
print("=" * 55 + "\n")
