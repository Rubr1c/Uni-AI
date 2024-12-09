class MedicalExpertSystem:
    """
    Attributes:
        rules (list): A list of dictionaries representing the diagnostic rules.
            Each rule contains:
                - symptoms (set): A set of symptoms defining the condition.
                - diagnosis (str): The name of the condition.
                - recommendation (str): Advice based on the diagnosis.
                - probability (float): Confidence level of the diagnosis.
    """

    def __init__(self):
        """
        Initializes the expert system with a set of predefined diagnostic rules.
        """
        self.rules = [
            {
                "symptoms": {"fever", "cough", "fatigue"},
                "diagnosis": "Flu",
                "recommendation": "Rest, stay hydrated, and consult a doctor if symptoms worsen.",
                "probability": 0.8,
            },
            {
                "symptoms": {"fever", "rash", "red eyes"},
                "diagnosis": "Measles",
                "recommendation": "Isolate, avoid contact with others, and seek medical advice immediately.",
                "probability": 0.9,
            },
            {
                "symptoms": {"headache", "nausea", "sensitivity to light"},
                "diagnosis": "Migraine",
                "recommendation": "Rest in a dark, quiet room and consider over-the-counter pain relief.",
                "probability": 0.7,
            },
            {
                "symptoms": {"chest pain", "shortness of breath", "dizziness"},
                "diagnosis": "Heart Attack",
                "recommendation": "Call emergency services immediately.",
                "probability": 0.95,
            },
            {
                "symptoms": {"fever", "chills", "difficulty breathing"},
                "diagnosis": "Pneumonia",
                "recommendation": "Seek medical care and take prescribed antibiotics.",
                "probability": 0.85,
            },
        ]

    def infer_diagnosis(self, user_symptoms):
        """

        Args:
            user_symptoms (set): A set of symptoms provided by the user.

        Returns:
            dict: A dictionary containing:
                - diagnosis (str): The inferred condition or a fallback message.
                - recommendation (str): Advice based on the diagnosis.
                - probability (float): Confidence level of the diagnosis (if applicable).
        """
        matches = []
        for rule in self.rules:
            matching_symptoms = rule["symptoms"].intersection(user_symptoms)
            match_percentage = len(matching_symptoms) / len(rule["symptoms"])
            if match_percentage > 0.5:  # Threshold for probable diagnosis
                matches.append((rule, match_percentage))

        if not matches:
            return {
                "diagnosis": "No diagnosis could be made based on the provided symptoms.",
                "recommendation": "Consult a healthcare professional for further evaluation.",
            }

        # Sort by match percentage and probability
        matches.sort(key=lambda x: (x[1], x[0]["probability"]), reverse=True)
        best_match = matches[0][0]

        return {
            "diagnosis": best_match["diagnosis"],
            "recommendation": best_match["recommendation"],
            "probability": best_match["probability"],
        }


if __name__ == "__main__":
    system = MedicalExpertSystem()
    user_symptoms = {"fever", "cough", "fatigue", "headache"}
    result = system.infer_diagnosis(user_symptoms)

    print(f"Diagnosis: {result['diagnosis']}")
    print(f"Recommendation: {result['recommendation']}")
    if "probability" in result:
        print(f"Probability: {result['probability'] * 100:.2f}%")
