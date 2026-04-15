import json
from quiz import Quiz

def _default_quiz_data():
    """기본 퀴즈 데이터를 반환하는 함수"""
    return [
        {
            "question": "Python의 창시자는?",
            "choices": ["Guido van Rossum", "Linus Torvalds", "Bjarne Stroustrup", "James Gosling"],
            "answer": 1,
            "hint": "네덜란드 출신 개발자로, 이름 첫 글자는 G입니다.",
        },
        {
            "question": "Python이 처음 발표된 연도는?",
            "choices": ["1989", "1991", "1993", "1995"],
            "answer": 2,
            "hint": "1990년대 초반입니다.",
        },
        {
            "question": "Python의 버전 관리 시스템은?",
            "choices": ["SVN", "Mercurial", "Git", "Perforce"],
            "answer": 3,
            "hint": "현재 대부분의 오픈소스 프로젝트가 사용하는 도구입니다.",
        },
        {
            "question": "'Hello, World!'를 출력하는 Python 명령은?",
            "choices": ["print('Hello, World!')", "cout << 'Hello, World!'", "System.out.println('Hello, World!')", "echo 'Hello, World!'"],
            "answer": 1,
            "hint": "파이썬의 기본 출력 함수 이름은 print입니다.",
        },
        {
            "question": "Python에서 리스트의 마지막 요소에 접근하는 인덱스는?",
            "choices": ["0", "1", "-1", "None"],
            "answer": 3,
            "hint": "파이썬은 음수 인덱스를 지원합니다.",
        },
    ]

def default_quizzes():
    """기본 퀴즈 데이터를 Quiz 객체 리스트로 반환하는 함수"""
    quiz_data = _default_quiz_data()
    return [Quiz(q["question"], q["choices"], q["answer"], q.get("hint", "")) for q in quiz_data]

def load_state(state_file):
    try:
        with open(state_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        quizzes = [Quiz(q["question"], q["choices"], q["answer"], q.get("hint", "")) for q in data["quizzes"]]
        best_score = data.get("best_score", 0)
        return quizzes, best_score

    except FileNotFoundError:
        print(f"{state_file} 파일이 존재하지 않습니다. 기본 퀴즈 데이터를 로드합니다.")
        return default_quizzes(), 0
    except json.JSONDecodeError:
        print(f"{state_file} 파일이 올바른 JSON 형식이 아닙니다. 기본 퀴즈 데이터를 로드합니다.")
        return default_quizzes(), 0
    except Exception as e:
        print(f"퀴즈 데이터를 불러오는 중 오류가 발생했습니다: {e}")
        return default_quizzes(), 0

def save_state(state_file, quizzes, best_score):
    data = {
        "quizzes": [
            {
                "question": quiz.question,
                "choices": quiz.choices,
                "answer": quiz.answer,
                "hint": quiz.hint
            }
            for quiz in quizzes
        ],
        "best_score": best_score
    }
    try:
        with open(state_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"퀴즈 데이터를 저장하는 중 오류가 발생했습니다: {e}")

if __name__ == "__main__":
    print("storage.py는 퀴즈 데이터를 저장하고 불러오는 기능을 담당하는 모듈입니다.")
    quizzes, best_score = load_state("state.json")
    print(f"퀴즈 {len(quizzes)}개와 최고 점수 {best_score}가 로드되었습니다.")
    save_state("state1.json", quizzes, best_score)