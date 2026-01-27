# 🧠 PsyHunter: Behavioral Threat Intelligence Tool

> *"Cybersecurity isn't just about code; it's about the human mind."*

## 🚀 Overview
**PsyHunter** is a **Behavioral Threat Intelligence** tool designed to bridge the gap between Psychology and Cybersecurity. Unlike traditional vulnerability scanners that look for software bugs, MindHunter analyzes the **"Human Element"**.

By simulating an OSINT (Open Source Intelligence) analysis on social media footprints, it creates a psychological profile of a target to predict their susceptibility to **Social Engineering** attacks.

## 🎯 Problem Statement
Statistically, **90% of cyber attacks** start with a human error (Phishing). Traditional firewalls cannot protect against a user's emotional state.
* **Question:** Can we predict *when* a user is most likely to click a malicious link?
* **Solution:** Yes. A user experiencing "Financial Anxiety" is vulnerable to fake invoices. A user with "Burnout" is prone to attention errors.

## ⚡ Key Features
* **Sentiment Analysis (NLP):** Uses Natural Language Processing (TextBlob) to calculate an "Emotional Baseline Score" (Positive/Negative/Stressed).
* **Trigger Detection:** Automatically identifies psychological keywords (e.g., "Urgent," "Bills," "Angry") that indicate a vulnerability.
* **Predictive Risk Scoring:** Generates a **Human Vulnerability Score (0-100)** to assist Red Teaming and Security Awareness teams.

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **NLP Engine:** TextBlob
* **Interface:** Command Line Interface (CLI) with Colorama for visualization.
* **Data Source:** JSON (Simulating OSINT Data Extraction)

## 💻 Installation & Usage

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/MindHunter-Intelligence.git](https://github.com/YOUR_USERNAME/MindHunter-Intelligence.git)
    cd MindHunter-Intelligence
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Analysis**
    ```bash
    python main.py
    ```

## 📊 Sample Output
```text
🧠 MINDHUNTER: BEHAVIORAL THREAT INTELLIGENCE
👤 TARGET IDENTITY: Sarah Jenkins
============================================================

📊 EMOTIONAL BASELINE SCORE: -0.45
Detected Mood State: NEGATIVE / STRESSED 😡

🎯 DETECTED PSYCHOLOGICAL VULNERABILITIES:
   - [CRITICAL] Financial Anxiety
   - [CRITICAL] High Anger / Frustration

🛡️ PREDICTED PHISHING VECTORS (RISK ANALYSIS):
⚠️ ALERT: Target is highly vulnerable to 'Payroll', 'Bonus', or 'Invoice' scams.
⚠️ ALERT: Target is likely to click on 'Complaint Resolution' links.

>>> TOTAL HUMAN VULNERABILITY SCORE: 85/100