def main():
    while True:
        print("\n===== 프롬프트 관리 프로그램 =====")
        print("1. 프롬프트 추가")
        print("2. 프롬프트 목록 보기")
        print("3. 프롬프트 검색")
        print("4. 프롬프트 수정")
        print("5. 프롬프트 삭제")
        print("0. 종료")
        
        choice = input("\n메뉴를 선택하세요: ")
        
        if choice == "1":
            print("추가 기능 준비중")
        elif choice == "2":
            print("목록 기능 준비중")
        elif choice == "3":
            print("검색 기능 준비중")
        elif choice == "4":
            print("수정 기능 준비중")
        elif choice == "5":
            print("삭제 기능 준비중")
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")

main()