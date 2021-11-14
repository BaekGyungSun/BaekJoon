# 알파벳 소문자로만 이루어진 단어 S가 주어진다.
# 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

S = input()

num = list(range(97, 123)) # 아스키 값으로 선정하여 받기, 소문자만 받을 수 있음

for ascii_num in num:
    print(S.find(chr(ascii_num)))