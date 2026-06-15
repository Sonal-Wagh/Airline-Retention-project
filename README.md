# Airline Loyalty Retention Intelligence Platform

## Overview

This project was developed as a solution to the **"Unlocking Behavioral Intelligence in Airline Loyalty Programs"** business analytics challenge. The objective was to help airline marketing teams proactively identify customers at risk of disengagement, understand behavioral customer segments, and design targeted retention strategies.

The project combines **customer segmentation**, **behavioral churn prediction**, and **actionable retention recommendations** into a unified analytics framework and interactive Streamlit application.

---

## Business Problem

Traditional airline loyalty programs often rely on points and rewards while failing to detect early signs of customer disengagement. High-value customers may gradually reduce activity long before formally leaving the program, resulting in delayed interventions and lost revenue opportunities.

This project addresses three key questions:

* Which customers are most likely to disengage?
* Which customer segments create the most value?
* What specific retention actions should be taken for each segment?

---

## Solution Approach

### 1. Behavioral Churn Prediction

A time-aware churn prediction framework was developed using historical customer activity.

* Training Window: First Half of 2018 (H1)
* Prediction Window: Second Half of 2018 (H2)
* Churn Definition: Customers making two or fewer flights during H2

An **XGBoost classifier** was trained using customer behavioral, loyalty, and demographic features.

#### Model Performance

| Metric    | Score |
| --------- | ----- |
| Accuracy  | 93.0% |
| ROC-AUC   | 0.94  |
| Precision | 93%   |
| Recall    | 65%   |
| F1 Score  | 77%   |

---

### 2. Customer Segmentation

K-Means clustering was applied to identify distinct customer behavior patterns.

Segments include:

* Silent VIPs
* Road Warriors
* Frequent Travelers
* Reward Seekers
* Dormant Members

The segmentation framework enables targeted business actions rather than one-size-fits-all retention programs.

---

### 3. Smart Retention Framework

Each customer segment is mapped to a specific retention strategy:

| Segment            | Recommended Action                            |
| ------------------ | --------------------------------------------- |
| Silent VIPs        | Premium retention and exclusive rewards       |
| Road Warriors      | Loyalty reinforcement and tier progression    |
| Frequent Travelers | Upgrade incentives and route expansion offers |
| Reward Seekers     | Bonus redemption and engagement campaigns     |
| Dormant Members    | Immediate win-back campaigns                  |

---

## Interactive Prototype

The Streamlit application allows marketing teams to:

* View key customer and portfolio KPIs
* Search individual customers
* Assess churn risk and customer value
* Generate segment-specific retention campaigns
* Prioritize high-risk customers for intervention

The prototype was designed for non-technical users and focuses on turning model outputs into actionable business decisions.

The link for the Streamlit app : https://airline-retention-project-t952spvjwnfvqegjvlkgyj.streamlit.app/
