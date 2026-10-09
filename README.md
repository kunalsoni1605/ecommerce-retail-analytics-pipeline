\# E-Commerce Retail Sales Analytics



Customer segmentation and sales analytics pipeline using the Online Retail II dataset, built with Python, Databricks (PySpark), and Power BI.



\*\*Author:\*\* Kunal Radhanpara

\*\*Email:\*\* kunalsoni01616@gmail.com

\*\*LinkedIn:\*\* \[linkedin.com/in/kunalradhanpara](https://linkedin.com/in/kunalradhanpara)



\---



\## Project Overview



An end-to-end retail analytics pipeline analyzing 1M+ real e-commerce transactions (UK-based online retailer, 2009-2011). Demonstrates data cleaning, RFM customer segmentation, product/geographic analysis, and BI dashboard design — core skills for Data Analyst/BI Developer roles.



This project complements my \[Stock Market Analytics Pipeline](https://github.com/kunalsoni1605/stock-market-analytics-pipeline) (time-series/technical analysis) by focusing on business/customer analytics instead.



\---



\## Tech Stack



| Category | Technology |

|---|---|

| Data Cleaning | Python, Pandas |

| Data Processing | Databricks Community Edition, PySpark |

| Storage | Delta Lake Tables |

| Visualization | Power BI Desktop |

| Version Control | Git, GitHub |



\---



\## Dataset



\*\*Source:\*\* \[Online Retail II (UCI Machine Learning Repository)](https://archive.ics.uci.edu/dataset/502/online+retail+ii)



\- 1,067,371 transactions, Dec 2009 - Dec 2011

\- UK-based online retailer selling gift-ware

\- 5,942 unique customers, 5,305 products, 43 countries



\---



\## Progress



\### ✅Data Acquisition + Cleaning (Complete)

\- \[x] Explored raw dataset, identified quality issues

\- \[x] Built cleaning pipeline (removed returns, bad prices, missing customer IDs)

\- \[x] Retained 805,549 clean rows (75.5%) for analysis

\- \[x] Uploaded clean + full datasets to Databricks



\### ✅RFM Segmentation + Metrics (Complete)

\- \[x] Calculated Recency, Frequency, Monetary scores per customer

\- \[x] Segmented customers (Champions, Loyal, At Risk, Lost, etc.)

\- \[x] Built product performance metrics

\- \[x] Built country-level sales breakdown

\- \[x] Built monthly sales trend table



\### 📅Advanced Analytics (Planned)

\- \[ ] Cohort retention analysis

\- \[ ] Returns/cancellation analysis

\- \[ ] Export final tables for Power BI



\### 📅Dashboard + Documentation (Planned)

\- \[ ] Power BI dashboard (Executive Summary, Customer Segmentation, Product Performance, Geographic view)

\- \[ ] Final documentation, screenshots

\- \[ ] LinkedIn post, resume update



\---



\## Key Tables (Databricks)



| Table | Description |

|---|---|

| `transactions\_clean` | Valid sales transactions, ready for analysis |

| `transactions\_full` | All transactions (incl. returns/cancellations, flagged) |

| `customer\_rfm\_segments` | RFM scores and segment labels per customer |

| `product\_performance` | Revenue, units sold, order count per product |

| `country\_sales` | Revenue and customer counts by country |

| `monthly\_sales` | Revenue, orders, customers by month |



\---



\## Project Structure

ecommerce-retail-analytics/

├── data/

│ ├── raw/ # Original Excel file (gitignored)

│ └── processed/ # Cleaned CSVs (gitignored)

├── scripts/

│ ├── explore\_data.py

│ └── clean\_data.py

├── notebooks/

│ └── 02\_rfm\_segmentation.py

├── powerbi/ # Dashboard file (Week 4)

├── images/ # Screenshots (Week 4)

├── .gitignore

├── requirements.txt

└── README.md



\---



\## How to Run



1\. Download the \[Online Retail II dataset](https://archive.ics.uci.edu/dataset/502/online+retail+ii)

2\. Place in `data/raw/`

3\. Run `scripts/explore\_data.py` to review data quality

4\. Run `scripts/clean\_data.py` to produce cleaned CSVs

5\. Upload CSVs to Databricks, run `notebooks/02\_rfm\_segmentation.py`

6\. Open Power BI dashboard (once Week 4 is complete)



\---

