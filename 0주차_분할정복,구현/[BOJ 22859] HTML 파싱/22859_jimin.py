import re

string = input()

cursor = 6
answer = ""

while cursor < len(string):
    if string[cursor:cursor+len("</main>")] == "</main>": break

    # div 태그 입장
    if string[cursor:cursor+len("<div")] == "<div":
        # 제목 추가
        if len(answer)>0: answer += "\n"
        answer += "title : "
        cursor += len("<div title=\"")
        while string[cursor] != "\"":
            answer += string[cursor]
            cursor += 1
        cursor += 2
        
        # p 태그 내용 추가
        p_stack = []
        while string[cursor:cursor+len("</div>")] != "</div>":
            if string[cursor:cursor+len("<p>")] == "<p>":
                answer += "\n"
                cursor += len("<p>")
            elif string[cursor:cursor+len("</p>")] == "</p>":
                cursor += len("</p>")
                continue

            if string[cursor] == "<":         # p 태그 내부 다른 태그 존재
                p_stack.append("<")
            elif string[cursor] == ">":
                p_stack.pop()
                cursor += 1
                continue

            if len(p_stack) == 0:
                answer += string[cursor]
            cursor += 1
        cursor += len("</div>")
                
# 공백 제거
ans_arr = list(answer.split("\n"))
for i in range(len(ans_arr)):
    ans_arr[i] = ans_arr[i].strip()
    # 연속 두개 공백을 하나의 공백으로
    ans_arr[i] = re.sub(r'\s+', ' ', ans_arr[i])

print('\n'.join(ans_arr))