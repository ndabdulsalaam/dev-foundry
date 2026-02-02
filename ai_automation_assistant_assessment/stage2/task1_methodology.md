# Task 1: Step-by-Step Methodology

## Objective
Analyze e-commerce transactions to assign customer engagement tiers and calculate revenue contributions.

---

## Step 1: Understanding the Problem

**What we need to do:**
1. For each transaction, determine how many purchases that customer had already made **before** that transaction
2. Assign an engagement tier based on that count:
   - **New**: First purchase (0 previous purchases)
   - **Active**: 1-4 previous purchases
   - **Power User**: 5+ previous purchases
3. Calculate total revenue contributed by each tier
4. Create two visualizations

---

## Step 2: Load and Explore the Data

```python
import pandas as pd

# Load the CSV data
df = pd.read_csv('Ecom Q4 Dataset - Public - Dummy_E-commerce_Transactions.csv')

# Convert Transaction Date to datetime
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])
```

**Key observations:**
- Dataset contains 500 transactions from Jan 2022 to Dec 2024
- Columns: Customer ID, Transaction Date, Transaction Amount, Category, Region
- 147+ unique customers with varying purchase frequencies

---

## Step 3: Sort Data Chronologically by Customer

**Why this matters:** To correctly count "previous purchases," we need transactions ordered by time *within each customer's history*.

```python
# Sort by Customer ID and Transaction Date
df = df.sort_values(['Customer ID', 'Transaction Date']).reset_index(drop=True)
```

---

## Step 4: Calculate Previous Purchases

**Method:** Use `cumcount()` which assigns a sequential number (0, 1, 2, ...) to each row within a group.

```python
# For each transaction, count how many came before it for that customer
df['Previous Purchases'] = df.groupby('Customer ID').cumcount()
```

**Example:**
| Customer ID | Transaction Date | Previous Purchases |
|-------------|------------------|-------------------|
| CUST001     | 2022-11-12       | 0                 |
| CUST001     | 2022-12-22       | 1                 |
| CUST001     | 2023-08-03       | 2                 |
| CUST001     | 2024-03-09       | 3                 |
| CUST001     | 2024-08-17       | 4                 |
| CUST001     | 2024-09-27       | 5                 |

---

## Step 5: Assign Engagement Tiers

**Tier Logic:**
```python
def assign_tier(previous_purchases):
    if previous_purchases == 0:
        return 'New'  # First purchase
    elif previous_purchases <= 4:
        return 'Active'  # 1-4 previous purchases
    else:
        return 'Power User'  # 5+ previous purchases

df['Engagement Tier'] = df['Previous Purchases'].apply(assign_tier)
```

**Important insight:** A customer can have transactions in multiple tiers over time. For example:
- First purchase → "New"
- 2nd through 5th purchase → "Active" 
- 6th purchase onward → "Power User"

---

## Step 6: Calculate Revenue by Tier

```python
revenue_by_tier = df.groupby('Engagement Tier')['Transaction Amount'].sum().round(2)
```

---

## Final Results

### 📊 Total Revenue by Engagement Tier:

| Tier | Revenue | Transaction Count |
|------|---------|-------------------|
| **New** | $70,954.36 | 147 |
| **Active** | $161,816.89 | 315 |
| **Power User** | $19,016.86 | 38 |

**Total Revenue: $251,788.11**

---

## Visualizations Created

### Chart 1: Monthly Revenue Trends by Region (Jan 2022 - Dec 2024)
- Multi-line chart showing revenue trends for North, South, East, and West regions
- X-axis: Month-Year format (Jan 2022, Feb 2022, ... Dec 2024)
- Each region has a distinct colored line

### Chart 2: Revenue by Category (2024 Only)
- Bar chart comparing revenue across categories
- Only includes transactions from 2024
- Shows total revenue for each product category

---

## Key Insights

1. **Active customers generate the most revenue** ($161,816.89) - representing 64.3% of total revenue
2. **New customers contribute significantly** ($70,954.36) - 28.2% of total revenue
3. **Power Users are few but valuable** - Only 38 transactions but represent dedicated, loyal customers
4. The tier assignment is **transaction-level**, meaning a single customer can contribute to different tiers as they progress in their purchase journey
