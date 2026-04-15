from quiz import Quiz
from storage import load_state, save_state

class QuizGame:
    def __init__(self, state_file="state.json"):
        """게임 상태를 관리하는 클래스"""
        self.quizzes = []
        self.best_score = 0
        self.state_file = state_file
        self.load_state()

    def load_state(self):
        """게임 상태를 파일에서 불러오는 메서드"""
        self.quizzes, self.best_score = load_state(self.state_file)

    def save_state(self):
        """게임 상태를 파일에 저장하는 메서드"""
        save_state(self.state_file, self.quizzes, self.best_score)

    def play_quiz(self):
        """
				퀴즈를 플레이하는 메서드
				- 각 퀴즈를 순서대로 보여주고 사용자 입력을 받음
				- 힌트 요청 시 힌트를 보여주고 다시 입력 받음
				- 정답 여부에 따라 점수를 계산하고 최종 점수와 최고 점수를 비교
				"""
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요.")
            return
        print(f"퀴즈를 시작합니다! 총 {len(self.quizzes)}문제가 있습니다.")
        print("=" * 50)
        score = 0
        for idx, quiz in enumerate(self.quizzes, start=1):
            print(f"[문제 {idx}]")
            quiz.display()
            while True:
                try:
                    user_input = input("정답을 입력하세요 (1-4, 힌트: 0): ").strip()
                    if not user_input:
                        print("빈 입력입니다. 다시 입력해주세요.")
                        continue
                    user_answer = int(user_input)
                    if user_answer == 0:
                        if quiz.hint:
                            print(f"힌트: {quiz.hint}")
                        else:
                            print("힌트가 없습니다.")
                        continue
                    if 1 > user_answer or user_answer > 4:
                        print("1에서 4 사이의 숫자를 입력해주세요.")
                        continue
                    break
                except ValueError:
                    print("유효한 숫자를 입력해주세요.")
            if quiz.is_correct(user_answer):
                print("정답입니다!")
                score += 1
            else:
                print(f"틀렸습니다! 정답은 {quiz.answer}번입니다.")
        score_percentage = (score / len(self.quizzes)) * 100
        if score_percentage > self.best_score:
            self.best_score = score_percentage
            print(f"축하합니다! 새로운 최고 점수입니다: {self.best_score:.2f}%")
        else:
            print(f"당신의 점수: {score_percentage:.2f}%. 최고 점수는 {self.best_score:.2f}%입니다.")

    def add_quiz(self):
        print("새 퀴즈를 추가합니다.\n")
        question = input("문제를 입력하세요:").strip()
        if not question:
            print("문제는 빈 칸일 수 없습니다. 퀴즈 추가를 취소합니다.")
            return
        choices = []
        for i in range(4):
            choice = input(f"선택지 {i+1}을 입력하세요:").strip()
            if not choice:
                print("선택지는 빈 칸일 수 없습니다. 퀴즈 추가를 취소합니다.")
                return
            choices.append(choice)
        hint = input("힌트를 입력하세요 (선택 사항, 빈 칸 가능):").strip()

        while True:
            try:
                ans = input("정답을 입력하세요 (1-4): ").strip()
                if not ans:
                    print("빈 입력입니다. 다시 입력해주세요.")
                    continue
                answer = int(ans)
                if 1 > answer or answer > 4:
                    print("1에서 4 사이의 숫자를 입력해주세요.")
                    continue
                break
            except ValueError:
                print("유효한 숫자를 입력해주세요.")
        new_quiz = Quiz(question, choices, answer, hint=hint)
        self.quizzes.append(new_quiz)
        print("퀴즈가 성공적으로 추가되었습니다.")
        self.save_state()

    def display_quizzes(self):
        """등록된 퀴즈 목록을 출력하는 메서드"""
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return
        print(f"등록된 퀴즈 수 : {len(self.quizzes)}")
        print("=" * 50)
        for idx, quiz in enumerate(self.quizzes, start=1):
            print(f"{idx}. {quiz.question}")
        print("=" * 50)

    def display_best_score(self):
        """최고 점수를 출력하는 메서드"""
        # TODO: 이후에 개선 필요
        print(f"최고 점수: {self.best_score}")

    def display_menu(self):
        """메인 메뉴를 출력하는 메서드"""
        print("=" * 50)
        print("🎯 나만의 퀴즈 게임 🎯")
        print("=" * 50)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 50)

    def get_menu_choice(self):
        """
        사용자로부터 메뉴 선택을 받는 메서드
        input 시 앞뒤 공백 제거, 빈 입력 처리, 숫자 변환 시 범위 밖 예외 처리 포함
        """
        while True:
            try:
                choice = input("메뉴를 선택하세요 (1-5): ").strip()
                if not choice:
                    print("빈 입력입니다. 다시 입력해주세요.")
                    continue
                choice = int(choice)
                if 1 > choice or choice > 5:
                    print("1에서 5 사이의 숫자를 입력해주세요.")
                    continue
                return choice
            except ValueError:
                print("유효한 숫자를 입력해주세요.")

    def run(self):
        """게임의 메인 루프를 실행하는 메서드"""
        try:
            while True:
                self.display_menu()
                choice = self.get_menu_choice()
                if choice == 1:
                    self.play_quiz()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.display_quizzes()
                elif choice == 4:
                    self.display_best_score()
                elif choice == 5:
                    print("게임을 종료합니다.")
                    break
        except KeyboardInterrupt:
            print("\n\n입력 종료 감지 (Ctrl+C) - 안전하게 종료합니다.")
        except EOFError:
            print("\n\n입력 스트림 종료 감지 - 안전하게 종료합니다.")
        except Exception as e:
            print(f"\n예상치 못한 오류: {e}")
        finally:
            print("데이터를 저장 중...")
            self.save_state()
            print("종료되었습니다.")
