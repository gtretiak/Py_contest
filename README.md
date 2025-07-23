# Py_contest
This repository contains Pyhton-based programs solving various real-world problems.
    
How to run the programs:
   ```
   # Example
   python3 council.py OR python3 council.py < input.txt
   ```
Below is a detailed breakdown of each program 👇
## 1. council.py
This program filters reliable workers and aggregates their task responses.

    Reliable Annotation Aggregator
    Practical Use Cases:
    1. Content Moderation (e.g., YouTube or TikTok)
    Several human reviewers flag content. Only responses from reliable reviewers are aggregated to decide whether to remove or keep content.
    2. Medical Image Labeling
    Radiologists or technicians annotate X-rays or MRIs. The system filters based on past accuracy and combines answers for AI training.
    3. Survey Quality Control
    In large-scale surveys (e.g., political polling), filter out low-effort or inconsistent respondents and aggregate reliable responses per question.
    4. Product Review Tagging
    Workers label reviews with sentiments or features. This script ensures only reliable workers influence the final tags.
    5. Self-driving Car Datasets
    Annotators tag traffic objects (pedestrians, lights, signs). This algorithm ensures faulty annotators don't skew the labels that will train driving models.
