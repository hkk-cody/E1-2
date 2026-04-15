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
