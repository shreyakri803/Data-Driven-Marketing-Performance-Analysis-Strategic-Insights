# Data-Driven-Marketing-Performance-Analysis-Strategic-Insights
A data-driven marketing analytics project that evaluates customer journeys, social engagement, and product reviews to uncover performance trends and deliver strategic insights for improving conversion rates, customer satisfaction, and overall marketing ROI.

# 📊 Data-Driven Marketing Performance Analysis & Strategic Insights  
Using SQL • Python (NLTK Sentiment) • Power BI | End-to-End BI Project  

![Power BI](https://img.shields.io/badge/Power%20BI-BI%20Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Python](https://img.shields.io/badge/Python-Sentiment%20Analysis-3670A0?style=for-the-badge&logo=python&logoColor=yellow)
![SQL](https://img.shields.io/badge/SQL-Data%20Engineering-336791?style=for-the-badge&logo=mysql&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-Sentiment%20Scoring-85C1E9?style=for-the-badge)
![GitHub](https://img.shields.io/badge/Domain-Ecommerce%20Marketing-8A2BE2?style=for-the-badge)

This project analyzes marketing performance for an online retail business, **ShopEasy**, by combining  
✅ SQL-based data modeling  
✅ Python-powered sentiment analysis  
✅ Power BI dashboards  

Key focus: **Improving conversions, user engagement, customer sentiment & marketing ROI**

This is a **real-world simulation** of a data analyst / BI consultant problem statement.

## 📚 Table of Contents
1. Project Overview  
2. Business Problem  
3. Objectives  
4. Data Sources  
5. Tech Stack  
6. Architecture  
7. Data Engineering (SQL)  
8. Sentiment Analysis (Python)  
9. Power BI Dashboards  
10. Insights & Recommendations  
11. How to Run  
12. Files in Repository  
13. Conclusion  
14. Author  

## 📝 Project Overview
The goal of this project is to evaluate marketing funnel performance, digital engagement, and  
customer sentiment to support **data-driven marketing strategy & decision-making**.

We analyze:
- Website conversion trends
- Social media interaction data (views, clicks, likes)
- Customer reviews + NLP sentiment analysis
- Product-level performance trends

Output: **Interactive Power BI dashboards + Sentiment-enhanced tables + Insights playbook**

## 🧩 Business Problem
Despite investing in digital campaigns, ShopEasy noticed:
- Declining customer engagement
- Fluctuating conversion rates
- Mixed customer sentiment & reviews
- Low ROI from marketing spending

### 🎯 Objective
Use data analysis & BI to:
- Understand marketing performance drivers
- Improve customer experience & campaign impact
- Boost conversions, repeat purchases & brand loyalty

## 📂 Data Sources
| Dataset | Description |
|---|---|
Customer Journey | Views → Clicks → Add-to-Cart → Purchase flow  
Customer Reviews | Rating, review text, dates, text sentiment  
Engagement Data | Views, clicks, likes by content type  
Products Data | Product & category metadata  

## 🛠 Tech Stack
- **SQL Server** – Data cleaning, modeling, feature engineering  
- **Python + NLTK** – Sentiment analysis on review text  
- **Power BI** – DAX, Data modeling, dashboards  
- **Excel/CSV** – Raw data storage

## 🏗️ Architecture

Raw Data → SQL Cleaning & Modeling → Python Sentiment Scoring → Power BI → Insights


## 🧠 Data Engineering (SQL)

### Key Transformations
✔ Cleaned review text & normalized columns  
✔ Removed duplicates using ROW_NUMBER  
✔ Converted content type & dates  
✔ Calculated journey durations  
✔ Enriched product categories & price tiers

### Example SQL Logic
- fact_customer_journey.sql → cleans steps, calculates durations  
- fact_customer_reviews.sql → prepares review base table  
- fact_engagement_data.sql → extracts views/click split from combined text

All scripts available in `/sql/` folder.

## 🤖 Sentiment Analysis with Python (NLTK)

### What it does
- Pulls reviews from SQL Server
- Cleans text
- Uses **VADER** sentiment analyzer
- Assigns:
  - Compound sentiment score
  - Sentiment label (Positive / Neutral / Negative)
  - Mixed sentiment categories (Mixed Positive / Mixed Negative)

### Output
`fact_customer_reviews_with_sentiment.csv` → used in Power BI

### Run steps
```bash
pip install pandas nltk pyodbc
python customer_review_sentiments.py


---

## ✅ **PART 9 — Power BI Dashboards**

```md
## 📊 Power BI Interactive Dashboards

### 1️⃣ Overview Dashboard
- Conversion, CTR, Avg Rating in one view

### 2️⃣ Conversion Analysis
- Monthly conversion trend
- Product conversion ranking
- Funnel behavior breakdown

### 3️⃣ Customer Sentiment & Ratings
- Sentiment distribution
- Average rating over time
- Scatter of review volume vs ratings

### 4️⃣ Social Media Engagement
- Views, clicks, likes trend
- Platform performance comparison

![coversion_details](https://github.com/user-attachments/assets/c86fe53e-4623-4c86-8a03-51b6f92e0263)

## 🧠 Insights

| Area | Key Insight |
|---|---|
Conversion | Dip → rebound to **11.4%**, funnel optimization needed  
Engagement | CTR strong, but views declining → content visibility issue  
Sentiment | ~3.7 avg rating, negative clusters in few products  
Product | Top performers: Hockey, Ski boots, Gloves etc.  

## 🎯 Recommendations
- Improve journey clarity & retargeting
- Increase frequency & platform-specific social content
- Fix low-rated product issues (quality, delivery, packaging)
- Build customer feedback loop & monthly scorecards

## ▶️ How to Run

### Step 1: Execute SQL scripts in sequence
### Step 2: Run Python sentiment script
### Step 3: Load CSV + SQL data in Power BI
### Step 4: Refresh & explore dashboards

## 📦 Repo Structure
📂 sql/                → Data modeling scripts  
📂 python/             → Sentiment analysis  
📂 powerbi/            → PBIX + exported PNGs  
📂 data/               → Output sentiment file  
📄 README.md           → Project guide  

## ✅ Conclusion
This project demonstrates an end-to-end real-world marketing analytics workflow:
- ETL & data quality in SQL
- NLP-based sentiment scoring
- BI storytelling via Power BI

Insight-driven dashboards help identify:
📍 Conversion trends  
📍 Content performance gaps  
📍 Customer sentiment issues  
📍 Product improvement areas  

This enables **data-driven marketing decisions & customer-centric growth.**

## 👤 Author

**Shreya Kumari**  
Data / BI Analyst | SQL • Power BI • Python  
📍 India  
🔗 LinkedIn: linkedin.com/in/shreya-k-986a8321b  


