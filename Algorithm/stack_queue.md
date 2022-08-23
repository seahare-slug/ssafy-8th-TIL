#### Stack

- 가장 마지막에 넣은 것을 제일 빨리 꺼내는 구조 (LIFO)
- DFS, 후위표기법 변환 등에 사용

  - DFS
    ```python
    crossroads = []
    # 현재 위치의 경로가 두개 이상이면 갈림길이므로 스택에 저장
    if len(dict[current]) >= 2:
    	crossroads.append(current)
    ```
  - 중위 -> 후위 표기법 변환

    ```python
    ipc = {"+": 1, "-": 1, "*": 2, "/": 2}
    infix = input()
    postfix = ""
    calculation = []
    for ele in infix:
    	# 숫자는 바로 넣기
    	if "1" <= ele <= "9":
    		postfix += ele
    	# 연산자일 때
    	else:
    		# 연산자 스택이 차 있고 이미 있는 연산자가 우선 순위가 더 높으면 pop
    		# 나중에 오는 연산자가 우선 순위가 높으면 이미 있는 연산자가 지연됨
    		if calculation and ipc[calculation[-1]] >= ipc[ele]:
    			postfix += calculation.pop()
    		# ele 뒤에 어떤 연산자가 올 지는 모르기 때문에 일단은 스택에 저장
    		calculation.append(ele)
    ```
