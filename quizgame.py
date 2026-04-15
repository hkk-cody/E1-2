class QuizGame:
    def __init__(self, state_file="state.json"):
        """게임 상태를 관리하는 클래스"""
        self.quizzes = []
        self.best_score = 0
        self.state_file = state_file
        self.load_state()




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
