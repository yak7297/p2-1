CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]

# 초기 프롬프트 데이터
prompts = [
    {
        "id": 1,
        "title": "블로그 글 작성 도우미",
        "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요.",
        "category": "텍스트 생성",
        "favorite": True
    },
    {
        "id": 2,
        "title": "제품 썸네일 생성",
        "content": "다음 제품의 매력적인 썸네일 이미지를 생성하기 위한 미드저니 프롬프트를 작성해주세요.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "id": 3,
        "title": "파이썬 코드 리팩토링",
        "content": "제공된 파이썬 코드를 PEP 8 스타일 가이드에 맞추어 가독성과 성능을 개선하고 주석을 달아주세요.",
        "category": "자동화",
        "favorite": True
    }
]

def display_menu():
    print("\n" + "=" * 35)
    print("      나만의 프롬프트 관리자")
    print("=" * 35)
    print("1. 프롬프트 추가")
    print("2. 프롬프트 전체 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 토글 (등록/해제)")
    print("7. 즐겨찾기 목록")
    print("0. 종료")
    print("=" * 35)

def add_prompt():
    print("\n--- 프롬프트 추가 ---")
    title = input("제목: ").strip()
    if not title:
        print("제목은 필수 입력 사항입니다.")
        return
    content = input("내용: ").strip()
    
    print("\n[카테고리 선택]")
    for idx, cat in enumerate(CATEGORIES, 1):
        print(f"{idx}. {cat}")
    try:
        cat_idx = int(input("카테고리 번호: ")) - 1
        category = CATEGORIES[cat_idx] if 0 <= cat_idx < len(CATEGORIES) else "기타"
    except ValueError:
        category = "기타"

    new_id = max([p["id"] for p in prompts], default=0) + 1
    prompts.append({
        "id": new_id,
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    })
    print(f"✓ '{title}' 프롬프트가 추가되었습니다. (ID: {new_id})")

def list_prompts():
    print("\n--- 프롬프트 전체 목록 ---")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return
    for p in prompts:
        fav_mark = "★" if p["favorite"] else "☆"
        print(f"[{p['id']}] {fav_mark} {p['title']} ({p['category']})")

def view_by_category():
    print("\n--- 카테고리별 조회 ---")
    for idx, cat in enumerate(CATEGORIES, 1):
        print(f"{idx}. {cat}")
    try:
        cat_idx = int(input("조회할 카테고리 번호: ")) - 1
        selected_cat = CATEGORIES[cat_idx]
    except (ValueError, IndexError):
        print("올바른 번호를 입력하세요.")
        return

    filtered = [p for p in prompts if p["category"] == selected_cat]
    print(f"\n[{selected_cat}] 카테고리 결과 ({len(filtered)}건):")
    for p in filtered:
        fav_mark = "★" if p["favorite"] else "☆"
        print(f"[{p['id']}] {fav_mark} {p['title']}")

def search_prompts():
    print("\n--- 프롬프트 검색 ---")
    keyword = input("검색할 키워드 (제목/내용): ").strip().lower()
    if not keyword:
        return
    results = [p for p in prompts if keyword in p["title"].lower() or keyword in p["content"].lower()]
    print(f"\n검색 결과 ({len(results)}건):")
    for p in results:
        fav_mark = "★" if p["favorite"] else "☆"
        print(f"[{p['id']}] {fav_mark} {p['title']} ({p['category']})")

def view_prompt_detail():
    print("\n--- 프롬프트 상세 보기 ---")
    try:
        pid = int(input("조회할 프롬프트 ID: "))
    except ValueError:
        print("숫자를 입력해주세요.")
        return
    prompt = next((p for p in prompts if p["id"] == pid), None)
    if not prompt:
        print("해당 ID의 프롬프트를 찾을 수 없습니다.")
        return
    fav_str = "등록됨" if prompt["favorite"] else "해제됨"
    print(f"\nID: {prompt['id']}")
    print(f"제목: {prompt['title']}")
    print(f"카테고리: {prompt['category']}")
    print(f"즐겨찾기: {fav_str}")
    print(f"내용:\n{prompt['content']}")

def toggle_favorite():
    print("\n--- 즐겨찾기 토글 ---")
    try:
        pid = int(input("즐겨찾기 상태를 변경할 프롬프트 ID: "))
    except ValueError:
        print("숫자를 입력해주세요.")
        return
    prompt = next((p for p in prompts if p["id"] == pid), None)
    if not prompt:
        print("해당 ID의 프롬프트를 찾을 수 없습니다.")
        return
    prompt["favorite"] = not prompt["favorite"]
    status = "등록" if prompt["favorite"] else "해제"
    print(f"✓ [{prompt['title']}] 프롬프트의 즐겨찾기가 {status}되었습니다.")

def list_favorites():
    print("\n--- 즐겨찾기 목록 ---")
    favs = [p for p in prompts if p["favorite"]]
    if not favs:
        print("즐겨찾기에 등록된 프롬프트가 없습니다.")
        return
    for p in favs:
        print(f"[{p['id']}] ★ {p['title']} ({p['category']})")

def main():
    while True:
        display_menu()
        choice = input("메뉴 선택: ").strip()
        if choice == "1":
            add_prompt()
        elif choice == "2":
            list_prompts()
        elif choice == "3":
            view_by_category()
        elif choice == "4":
            search_prompts()
        elif choice == "5":
            view_prompt_detail()
        elif choice == "6":
            toggle_favorite()
        elif choice == "7":
            list_favorites()
        elif choice == "0":
            print("\n나만의 프롬프트 관리자를 종료합니다. 이용해 주셔서 감사합니다!")
            break
        else:
            print("잘못된 입력입니다. 0~7 사이의 숫자를 입력해주세요.")

if __name__ == "__main__":
    main()