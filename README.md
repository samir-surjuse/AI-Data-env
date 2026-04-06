\# AI Data Analytics Environment (OpenEnv)



\## Overview

This project simulates a real-world data analytics task where an AI agent performs analysis on a retail dataset.



\## Tasks

1\. Total Sales Calculation

2\. Top Category Identification

3\. Lowest Profit Category Detection



\## Environment Design

\- reset() → returns a random task

\- step(action) → checks answer and gives reward (0 or 1)

\- state() → returns current task



\## Reward System

\- Correct Answer → +1

\- Wrong Answer → 0



\## Dataset

Retail sales dataset (CSV format)



\## How to Run



```bash

python inference.py

