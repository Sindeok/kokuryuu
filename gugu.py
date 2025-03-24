try:
    # 사용자로부터 단 수 입력받기
    dan = int(input("출력할 구구단의 단 수를 입력하세요: "))
    
    # 구구단 출력
    print(f"===== {dan}단 =====")
    for i in range(1, 10):
        print(f"{dan} x {i} = {dan * i}")
except ValueError:
    print("숫자만 입력해주세요.")
