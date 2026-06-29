from dataclasses import dataclass
from typing import List, Dict

KNOWLEDGE_BASE = {
    'Malaria': {
        'symptoms': ['fever', 'chills', 'sweating', 'headache', 'muscle_pain'],
        'weights': [0.30, 0.25, 0.20, 0.15, 0.10],
        'threshold': 0.55,
        'advice': 'Seek medical attention and begin antimalarial treatment.'
    },

    'Typhoid': {
        'symptoms': ['sustained_fever', 'abdominal_pain', 'diarrhea', 'weakness', 'rash'],
        'weights': [0.30, 0.25, 0.20, 0.15, 0.10],
        'threshold': 0.55,
        'advice': 'Consult a doctor and stay hydrated.'
    },

    'COVID-19': {
        'symptoms': ['fever', 'cough', 'loss_of_taste', 'shortness_of_breath', 'fatigue'],
        'weights': [0.20, 0.25, 0.30, 0.15, 0.10],
        'threshold': 0.50,
        'advice': 'Isolate immediately and take a COVID test.'
    },

    'Pneumonia': {
        'symptoms': ['cough', 'fever', 'fatigue', 'shortness_of_breath'],
        'weights': [0.30, 0.30, 0.20, 0.20],
        'threshold': 0.50,
        'advice': 'Seek urgent medical evaluation.'
    },

    'Dengue Fever': {
        'symptoms': ['fever', 'headache', 'rash', 'muscle_pain'],
        'weights': [0.30, 0.25, 0.20, 0.25],
        'threshold': 0.50,
        'advice': 'Increase fluid intake and consult a healthcare provider.'
    }
}

class DiagnosticExpertSystem:

    def __init__(self):
        self.working_memory = {}
        self.conclusions = []

    def add_fact(self, symptom, present):
        self.working_memory[symptom] = present

    def run_inference(self):

        self.conclusions = []

        for disease, data in KNOWLEDGE_BASE.items():

            score = sum(
                weight for sym, weight in zip(data['symptoms'], data['weights'])
                if self.working_memory.get(sym, False)
            )

            if score >= data['threshold']:

                self.conclusions.append({
                    'disease': disease,
                    'confidence': round(score * 100, 1),
                    'advice': data['advice']
                })

        self.conclusions.sort(
            key=lambda x: x['confidence'],
            reverse=True
        )

    def explain(self):

        if not self.conclusions:
            return "No disease confidently detected."

        report = "\n=== DIAGNOSTIC REPORT ===\n"

        for result in self.conclusions:

            report += f"\nDisease: {result['disease']}"
            report += f"\nConfidence: {result['confidence']}%"
            report += f"\nAdvice: {result['advice']}\n"

        return report


def run_consultation():

    system = DiagnosticExpertSystem()

    print("=== MEDICAL EXPERT SYSTEM ===")

    all_symptoms = set(
        s for d in KNOWLEDGE_BASE.values()
        for s in d['symptoms']
    )

    for symptom in sorted(all_symptoms):

        answer = input(
            f"Does the patient have {symptom.replace('_', ' ')}? (y/n): "
        ).lower()

        system.add_fact(symptom, answer == 'y')

    system.run_inference()

    print(system.explain())


if __name__ == "__main__":
    run_consultation()