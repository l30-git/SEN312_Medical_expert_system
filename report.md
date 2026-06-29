
---


Save as `report.md`

```md
# LAB REPORT

## Introduction

This project implements a rule-based medical expert system for diagnosing tropical diseases using forward chaining. The system uses patient symptoms as facts and applies production rules to determine possible diseases and provide medical advice.

## System Design

The expert system contains:
- Knowledge Base
- Working Memory
- Inference Engine
- Explanation Facility

The knowledge base stores diseases, symptoms, weights, thresholds, and medical advice.

The inference engine evaluates all rules using forward chaining and generates conclusions based on confidence scores.

## Diseases Implemented

The system diagnoses:
- Malaria
- Typhoid
- COVID-19
- Pneumonia
- Dengue Fever

## Limitations

The system has several limitations:
- It depends entirely on manually created rules.
- It cannot learn from new medical data automatically.
- It may produce incorrect results if symptoms overlap.
- Confidence scores are simplified and not medically exact.
- The system cannot replace professional medical diagnosis.

## Extension with Machine Learning

Machine learning could improve the system by:
- Learning patterns from large hospital datasets.
- Predicting diseases more accurately.
- Handling uncertainty better.
- Updating knowledge automatically.

A hybrid architecture could combine neural networks with expert system rules. The ML model could predict possible diseases while the expert system explains the reasoning and provides recommendations.

## Conclusion

The project demonstrates the practical implementation of an expert system using forward chaining. It shows how AI techniques can support medical diagnosis and decision-making.