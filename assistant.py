# assistant.py
import re

class SafetySupportAssistant:
    def __init__(self):
        self.scam_keywords = {
            "loan": [
                "instant loan", "quick approval", "no credit check loan",
                "low interest loan", "urgent loan", "loan offer", "guaranteed loan"
            ],
            "scam": [
                "win prize", "lottery winner", "unclaimed funds", "verify account",
                "click link", "urgent action required", "congratulations you have won"
            ],
            "fraud": [
                "fraud alert", "suspicious activity", "unauthorized transaction",
                "account suspended", "verify your details"
            ],
            "phishing": [
                "update your payment info", "security breach", "login credentials",
                "reset password link", "click here to avoid suspension"
            ]
        }

        self.helplines_and_ngos = {
            "181 Women Helpline": "https://www.nhp.gov.in/helpline-181-women-helpline_pg",
            "Sakhi One-Stop Centers": "https://wcd.nic.in/schemes/sakhi-one-stop-centre-scheme",
            "Snehalaya": "https://snehalaya.org/",
            "Breakthrough India": "https://inbreakthrough.org/"
        }

        self.scam_logs = {
            "total_checked": 0,
            "warnings_detected": 0,
            "category_counts": {}
        }

    def analyze_message_for_scam(self, message: str) -> dict:
        self.scam_logs["total_checked"] += 1

        message_clean = re.sub(r'[\W_]+', ' ', message.lower())

        warnings = []
        detected_types = set()

        for category, keywords in self.scam_keywords.items():
            for keyword in keywords:
                if keyword in message_clean:
                    warnings.append(f"{category.upper()} keyword detected: '{keyword}'")
                    detected_types.add(category)

        if warnings:
            self.scam_logs["warnings_detected"] += 1
            for cat in detected_types:
                self.scam_logs["category_counts"][cat] = self.scam_logs["category_counts"].get(cat, 0) + 1

            return {
                "status": "warning",
                "message": "⚠️ This message may contain scam, fraud or loan trap keywords.",
                "details": warnings,
                "detected_categories": list(detected_types)
            }

        return {
            "status": "safe",
            "message": "✅ No immediate scam or loan warning detected.",
            "detected_categories": []
        }

    def get_ngo_helpline_info(self) -> dict:
        return {
            "status": "success",
            "message": "Here are some verified NGOs and women's helplines:",
            "data": self.helplines_and_ngos
        }

    def get_scam_analytics(self) -> dict:
        return self.scam_logs
