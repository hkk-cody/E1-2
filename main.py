import sys
from quizgame import QuizGame

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("사용법: python main.py [state_file.json]")
    elif len(sys.argv) == 2:
        QuizGame(state_file=sys.argv[1]).run()
    else:
        QuizGame().run()