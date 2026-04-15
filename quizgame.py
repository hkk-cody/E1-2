class QuizGame:
    def __init__(self, state_file="state.json"):
        """게임 상태를 관리하는 클래스"""
        self.quizzes = []
        self.best_score = 0
        self.state_file = state_file
        self.load_state()






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
