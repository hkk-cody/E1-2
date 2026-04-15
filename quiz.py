class Quiz:
    def __init__(self, question, choices, answer, hint=""):
        """
        Args:
            question (str): 문제
            choices (list): 기본 4개 
            answer (int): 정답 (1~4)
            hint (str): 힌트.
        """
        self.question = question
        self.choices = choices
        self.answer = answer
        self.hint = hint

    def display(self):
      """문제와 선택지를 출력하는 메서드"""
      print(self.question)
      print(("(힌트: 0 입력)" if self.hint else "(힌트 없음)") + "\n")
      for idx, choice in enumerate(self.choices, start=1):
        print(f"{idx}. {choice}")

    def is_correct(self, user_answer):
        """사용자의 답이 정답인지 확인하는 메서드"""
        return user_answer == self.answer

if __name__ == "__main__":
    print("quiz.py는 퀴즈 문제를 정의하는 모듈입니다.")
    qu1 = Quiz("What is the capital of France?", ["1. Berlin", "2. Madrid", "3. Paris", "4. Rome"], 3)
    qu2 = Quiz("What is the largest planet in our solar system?", ["1. Earth", "2. Jupiter", "3. Mars", "4. Venus"], 2, "It's known for its Great Red Spot.")

    qu1.display()

    if qu1.is_correct(3):
        print("Correct!")
    else:        
        print("Wrong!")

    qu2.display()
    if qu2.is_correct(1):
        print("Correct!")
    else:        
        print("Wrong!")