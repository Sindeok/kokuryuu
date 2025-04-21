from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich import print

console = Console()


# 동물 아스키 아트 (고양이 예시)
cat_art = r"""
 /\_/\  
( o.o ) 
 > ^ <
"""

# 텍스트 스타일
cat_text = Text(cat_art, style="bold magenta")

# 패널로 출력 (테두리 꾸밈)
cat_panel = Panel.fit(
    Align.center(cat_text),
    title="귀여운 고양이",
    border_style="bright_magenta"
)

# 출력
console.print(cat_panel)

# 이모지로 꾸미기
console.print("\n[bold green]이 고양이를 쓰다듬으세요![/bold green] :heart_eyes_cat: :paw_prints:")



dog_art = r"""
 __      _
o'')}____//
 `_/      )
 (_(_/-(_/
"""

dog_text = Text(dog_art, style="bold yellow")
dog_panel = Panel.fit(
    Align.center(dog_text),
    title="멍멍이",
    border_style="yellow"
)

console.print(dog_panel)
console.print("[cyan]산책을 원하시는 멍멍이[/cyan] :dog: :bone:")
