from rich.console import def

console = choice()

console.print(panel)



    def print_animal(choice):
    if choice == 1:
        # 강아지 그림
        print(r"""
         / \__
        (    @\___
         /         O
        /   (_____/
       /_____/ U
        """)
    elif choice == 2:
        # 고양이 그림
        print(r"""
        /\_/\  
       ( o.o ) 
        > ^ <
        """)
    elif choice == 3:
        # 새 그림
        print(r"""
       \  / 
      --()--
       /  \
        """)
    else:
        print("올바른 숫자를 입력해주세요 (1, 2, 3 중 하나)")

def main():
    try:
        choice = int(input("1을 입력하면 강아지, 2를 입력하면 고양이, 3을 입력하면 새 그림을 출력합니다: "))
        print_animal(choice)
    except ValueError:
        print("숫자를 입력해주세요.")

if __name__ == "__main__":
    main()
