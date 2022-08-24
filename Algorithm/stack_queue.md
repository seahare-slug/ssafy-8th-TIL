#### Stack

- 가장 마지막에 넣은 값을 제일 빨리 꺼내는 구조 (LIFO)
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

#

#### Queue

- 가장 처음 넣은 값을 먼저 꺼내는 구조 (FIFO)
- 버퍼, 콜센터 업무 등에 사용
- stack은 뒤에 붙인 걸 바로 때는 형식이라 괜찮지만 queue는 뒤에 붙이고 앞에 것을 그냥 pop(0)으로 빼내게 되면 뒷부분이 한 칸씩 앞으로 당겨지기 때문에 비효율 적임
- front, rear 변수를 이용해서 관리

  ```python
  memory = [0] * 10
  front = rear = -1

  def is_empty():
    return front == rear

  def is_full():
    return rear == len(memory) - 1

  def en_queue(memory, value):
    global rear
    rear += 1
    memory[rear] = value

  def de_queue(memory):
    global front
    front += 1
    return memory[front]
  ```

#

#### Circlar Queue

- 일반적인 queue에서는 de_queue를 이용하면 front로 index 값만 옮겨주기 때문에 원래 배열의 앞부분 그대로 유지되며 공간을 차지하게 됨
- 따라서 de_queue 값으로 빠진 공간에 상관없이 공간이 없다고 판단할 수 있음
- 이러한 문제를 해결하기 위해 Queue를 원형으로 순환시켜 빠진 부분에 들어온 값을 넣을 수 있게 해줌
- queue의 길이를 이용해서 순환

  ```python
  memory = [0] * 10
  front = rear = 0

  def is_empty():
    return front == rear

  def is_full():
    return (rear + 1) % len(memory) == front

  def en_queue(memory, value):
    global rear
    if is_full():
      print("MEMORY IS FULL")
    else:
      rear = (rear + 1) % len(memory)
      memory[rear] = value

  def de_queue(memory):
    global front
    if is_empty():
      print("MEMORY IS EMPTY")
    else:
      front = (front + 1) % len(memory)
      return memory[front]
  ```
