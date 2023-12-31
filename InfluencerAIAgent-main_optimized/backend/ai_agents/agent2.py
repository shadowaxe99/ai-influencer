class Agent2:
    def __init__(self, db: MongoDB):
        self.db = db
    
    def generate_recommendations(self, user_id: str) -> list:
        user_data = self.db.find_one("users", {"user_id": user_id})
        recommendations = self._generate_recommendations(user_data)
        return recommendations
    
    def perform_analysis(self, user_id: str) -> dict:
        user_data = self.db.find_one("users", {"user_id": user_id})
        analysis_results = self._perform_analysis(user_data)
        return analysis_results
