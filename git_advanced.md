# git

## git Undoing

- git 작업 되돌리기
  1.  Working Directory 작업 단계
      - Working Directory에서 수정한 파일 내용을 이전의 커밋 상태로 되돌리기
      - [`git restore`](#git-restore)
  2.  Staging Area 작업 단계
      - Staging Area에 반영된 파일을 Working Directory로 되돌리기
      - [`git rm --cached`](#git-rm---cached)
      - [`git restore --staged`](#git-restore---staged)
  3.  Repository 작업 단계
      - 커밋을 완료한 파일을 Staging Area로 되돌리기
      - [`git commit --amend`](#git-commit---amend)

##### git restore

- Working Directory에서 수정한 파일 내용을 이전의 커밋 상태로 되돌리기
- 이미 버전관리가 되고 있는 파일만 되돌리기 가능
- 이 명령어를 통해 되돌리면 내용 복구는 불가능
- `git restore {file name}`

##### git rm --cached

- push를 하고 원하는 복구 기간부터 commit을 사용하지 않은 경우에 사용(commited가 비어있는 경우)
- `git rm --cached {file name}`

##### git restore --staged

- push 이후로 한 번 이상의 commit을 사용한 경우
- `git restore --staged {file name}`

##### git commit --amend

- 커밋을 완료한 파일을 Staging Area로 되돌리기
- 그냥 commit을 하면 다음 버전으로 기록 되지만 amend 옵션을 주면 앞의 버전 commit을 덮어써버리는 것(대체하는 것)
- staging Area에 새로 올라온 내용이 없다면, 직접 커밋의 메시지만 수정
- staging Area에 새로 올라온 내용이 있다면, 직전 커밋을 덮어쓰기
- 이전 커밋을 완전히 고쳐서 새 커밋으로 변경하지만 이전 커밋 아이디가 남기 때문에 복구는 가능함

#

## git reset

- 프로젝트를 특정 버전 상태로 되돌림
- 특정 커밋(버전)으로 되돌리면 그 커밋 이후로의 원래 버전들은 사라짐
- `git reset [옵션] {커밋 ID}`
  - 옵션은 soft, mixed, hard
  - 커밋ID는 되돌리고 싶은 커밋버전

##### `--soft`

- 해당 커밋으로 되돌아간 후 그 커밋 이후의 파일들은 Staging Area로 돌려놓음

##### `--mixed`

- 해당 커밋으로 되돌아간 후 그 이후 파일들은 Working Directory로 돌아감
- git reset의 기본 값

##### `--hard`

- 해당 커밋으로 되돌아간 후 그 이후 파일들은 Working Directory에서 삭제
- 기존의 Untracked 파일은 사라지지 않고 Untracked로 남아있음

## git revert

- 과거를 없었던 일로 만드는 행위로, 이전 커밋을 취소한 다음 새로운 커밋을 생성함
- `git revert {커밋ID}`
  - 커밋 ID는 취소하고 싶은 커밋의 ID를 작성
- reset은 커밋 내역을 삭제하는 반면, revert는 새로운 커밋을 생성함(커밋이 취소 되었다는 내용의 새로운 커밋을 생성함)
- 협업시 커밋 내역의 차이로 인한 충돌을 방지 가능

#

## git branch & merge

**branch**

- 나뭇가지라는 뜻으로, 작업 공간을 여러개로 나누어 독립적으로 작업할 수 있도록 도와주는 git의 도구
- 체게적인 개발과 원본에 대한 안정성을 강화

`git branch`: 로컬 저장소의 branch 목록 확인
`git branch -r`: 원격 저장소의 branch 목록 확인
`git branch {branch-name}`: 새로운 branch 생성
`git branch {branch-name} {커밋 ID}`: 특정 커밋 기준으로 branch 생성
`git branch -d {branch-name}`: 병합이 완료된 branch 삭제
`git branch -D {branch-name}`: 강제 삭제

`git switch {branch-name}`: 다른 branch로 이동
`git switch -c {branch-name}`: branch 새로 생성하고 이동
`git switch -c {branch-name} {커밋ID}`: 특정 커밋 기준으로 branch 생성 및 이동

- switch 하기 전에 해당 branch의 변경 사항을 반드시 커밋 완료하고 해야함
- 그렇지 않으면 switch를 통해서 이동 했음에도 원래 위치에 파일이 남아있음

`git log/ cat.git/HEAD`: 현재 HEAD가 어떤 branch를 가리키고 있는지 확인

#

**git merge**

- 분기된 branch들을 하나로 합치는 과정
- 주로 main에 병함
- `git merge {합쳐질 barnch들 이름}`
  - main branch에서 switch로 이동 후 merge
  - `Fast-Forward`
    - branch가 가리키는 커밋을 앞으로 이동하는 방법
    - 이전 버전과 다음 버전의 병함
  - `3-way Merge`
    - 각 branch의 커밋 두개와 공통 조상 하나를 사용하여 병합하는 방법
    - 각기 다른 현재 버전의 병합
  - `Merge Conflict`
    - 두 branch에서 같은 부분을 수정하면 병합시 충돌 발생

## git workflow

- Branch와 원격저장소를 이용해 협업을 하는 두가지 방법
  - 원격 저장소 소유권이 있는 경우 `Shared repository model`
  - 원격 저장소 소유권이 없는 경우 `Fork & Pull model`

##### shared repository model

- 원격 저장소의 주인이거나 collaborator로 등록 되어 있는 경우
- main branch에 직접 개발하는 것이 아니라 기능별로 branch를 따로 만들어 개발
- Pull request를 사용하여 팀원 간 변경 내용에 대한 소통 진행

##### fork & pull model

- 오픈소스 프로젝트와 같이, 자신의 소유가 아닌 원격 저장소인 경우
- 원본 원격 저장소를 그대로 내 원격 저장소에 복제
- 수정 후 복제한 내 원격 저장소에 Push
- 이후 pull request를 통해 원본 원격 저장소에 반영될 수 있도록 요청

#

#### git-flow

- `master`: 제품으로 출시될 수 있는 branch
- `develop`: 다음 출시 버전을 개발하는 branch
- `feature`: 기능을 개발하는 branch
- `release`: 이번 출시 버전을 준비하는 branch
- `hotfix`: 출시 버전에 발생한 버그를 수정하는 branch
