class QuizGame:
    def __init__(self, state_file="state.json"):
        """게임 상태를 관리하는 클래스"""
        self.quizzes = []
        self.best_score = 0
        self.state_file = state_file
        self.load_state()