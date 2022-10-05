# SQL(Structed Query Language)

- RDBMS의 데이터를 관리하게 위해 설계된 언어
  - _RDBMS_: 관계형 데이터베이스를 만들고 관리하는데 사용하는 프로그램
    - SQLite, MySQL, Oracle DB...
    - _RDB_: 관계형 데이터베이스, 구조화된 데이터
- 하나의 명령 단위는 세미콜론으로 끝내야함
- 명령어는 대소문자를 구분하지 않음
- 코드를 실행할 때 그냥 실행하면 작성된 모든 SQL이 다 실행되기 때문에 원하는 명령문을 커서로 선택하여 실행

- sqlite3 사용하기

```cli
1. 시작하기
$ sqlite3

2. DB 파일 열기
sqlite> .open file_name.sqlite3
or
$ sqlite3 file_name.sqlite3

3. 종료하기
sqlite> .exit
```

- csv 파일을 SQLite 테이블로 가져오기

```SQL
-- 1. 원하는 파일에 테이블 생성하기
CREATE TABLE table_name (
	...
)
```

```cli
2. DB 파일 열기
$ sqlite3 file_name.sqlite3

3. 모드를 csv로 설정
sqlite> .mode csv

4. .import 명령어를 통해 csv를 테이블로 가져오기
sqlite> .import file_name.csv table_name
```

#

### SQL의 종류

- [DDL(Data Definition Language)](#ddl)
  - **데이터베이스 구조**(테이블, 스키마)를 정의하기 위한 명령어
  - `CREATE`, `DROP`, `ALTER`
- [DML(Data Manipulation Language)](#dml)
  - **데이터를 조작**(추가, 조회, 변경, 삭제)하기 위한 명령어
  - `INSERT`, `SELECT`, `UPDATE`, `DELETE`
- DCL(Data Control Language)
  - 데이터의 보안, 권한 등을 관리하기 위한 명령어
  - `GRANT`, `REVOKE`, `COMMIT`, `ROLLBACK`
  - SQLite는 파일로 관리되는 DB이기 때문에 운영체제 자체의 파일 접근 권한으로만 제어 가능해서 DCL은 지원하지 않음

### DDL

- **Create Table statement**
  - id 칼럼은 직접 기본 키 역할을 정의하지 않으면 자동으로 `rowid`라는 칼럼이 만들어짐
    - `INTEGER PRIMARY KEY`로 칼럼을 직접 만들게 되면 이 칼럼은 rowid 칼럼의 별칭(alias)이 됨. 즉, rowid와 새로운 별칭 두 가지로 접근이 가능
  - **Data Type**
    - 기본적으로 타입은 선언해주지 않아도 어느정도 자동으로 지정이 됨
    - _NULL, INTEGER, REAL, TEXT, BLOB_
    - Boolean 값은 0과 1로 저장됨
    - 날짜와 시간은 `Date And Time Functions`를 이용해서 TEXT, REAL 또는 INTEGER 타입으로 저장할 수 있음
  - **Constraints**
    - 데이터베이스 내의 정확성, 일관성을 보장하기 위한 방법
    - 무결성을 보장
    - _NOT NULL, UNIQUE, PRIMARY KEY, AUTOINCREAMENT..._

**CREATE TABLE**

```SQL
-- 테이블 만드는 형식
CREATE TABLE table_name (
	column_1 data_type constraints,
	column_2 data_type constraints,
	column_3 data_type constraints,
);
```

```SQL
-- 예시
CREATE TABLE contacts (
	name TEXT NOT NULL,
	age INTEGER NOT NULL,
	email TEXT NOT NULL UNIQUE
);
```

#

**ALTER TABLE**

```SQL
-- 1. Rename a table
ALTER TABLE table_name RENAME TO new_table_name;

-- 2. Rename a column
ALTER TABLE table_name RENAME COLUMN column_name TO new_column_name;

-- 3. Add a new column to a table
-- 칼럼이 새로 생기면 기존 있던 데이터들의 새로운 칼럼 값이 NULL이 됨
-- 이때 만약 새로 생긴 칼럼의 조건에 NOT NULL이 있으면 오류 발생
-- 컬럼을 추가할 때 "DEFAULT"를 지정해주면 해결 가능
ALTER TABLE table_name ADD COLUMN column_definition;

-- 4. Delete a column
-- 칼럼이 다른 부분에서 참조되고 있으면 삭제 불가능
ALTER TABLE table_name DROP COLUMN column_name;

```

#

**DROP TABLE**

```SQL
-- 데이터베이스에서 테이블을 제거
-- 실행 취소나 복구가 불가능
DROP TABLE table_name;
```

#

### DML

- **SELECT statement**
  - 특정 테이블에서 데이터를 조회하기 위해 사용
  - 다양한 절과 같이 사용가능
    - `ORDER BY, DISTINCT, WHERE, LIKE, GROUP BY`

```SQL
-- rowid는 기본적으로 조회 가능
SELECT rowid, column1 FROM table_name;

-- target_column에 대해서 오름차순으로 조회, 같을 시 target_column2 기준으로 내림차순 조회
-- NULL 값은 가장 작은 값으로 인식
SELECT column1 FROM table_name ORDER BY target_column ASC(기본값), taget_column2 DESC;
```

#

- **Filtering Data**
  - 데이터를 중복 제거, 조건 설정 등으로 제어
  - Clause
    - SELECT DISTINCT
    - WHERE
    - LIMIT
  - Operator
    - LIKE
    - IN
    - BETWEEN

```SQL
-- DISTINCT 중복제거
-- 연속해서 중복 제거를 하면 column1, 2를 각각 제거하는 것이 아니라 하나의 집합으로 보고 같은 쌍만을 제거
-- NULL도 중복으로 취급
SELECT DISTINCT column1, column2 FROM table_name;

-- LIKE 패턴 일치 여부
-- WHERE 절에서 사용
-- 기본적으로 대소문자 구분은 안 함
-- %는 0개 이상의 자리를 의미, _는 1개의 자리를 의미
SELECT ... FROM ...
WHERE column LIKE "%호_";

-- IN 값이 속해 있는지 여부 확인
-- location이 경기도나 강원도인 데이터 조회
SELECT ... FROM ...
WHERE location IN ("경기도", "강원도");

-- location이 경기도 또는 강원도인 데이터 조회
WHERE location = "경기도" OR location = "강원도";

-- location이 경기도나 강원도가 아닌 데이터 조회
WHERE location NOT IN ("경기도", "강원도");

-- BETWEEN 사잇값 조회
-- NOT BETWEEN 사잇값이 아닌 데이터 조회
SELECT ... FROM ...
WHERE column NOT BETWEEN 20 AND 30;

-- OR을 통해 동일한 결과 도출 가능
WHERE column < 20 OR column > 30;

-- LIMIT 조회되는 데이터 수 제한(SELECT 절)
SELECT column FROM table_name LIMIT number;
-- (ORDER BY 절)
SELECT ... FROM ...
ORDER BY ... LIMIT number;

-- OFFSET 특정한 위치부터 데이터 조회 (LIMIT와 함께 사용)
-- 11번째 ~ 20번째 데이터 조회
SELECT ... FROM ...
LIMIT 10 OFFSET 10;
```

#

- **Grouping Data**

  1.  Aggregate function(집계함수)

  - `AVG(), COUNT(), MAX(), MIN(), SUM()`

  ```SQL
  	-- 전체 행 수 조회하기
  	SELECT COUNT(*) FROM table_name;

  	-- 평균 조회하기
  	SELECT AVG(column) FROM table_name;

  ```

  2.  Group by

  ```SQL
  -- column의 데이터 별로 묶여짐
  SELECT column FROM table_name GROUP BY column;

  -- 보통 집계함수와 같이 사용
  -- 묶여진 각 column 데이터안의 수를 조회
  SELECT COUNT(*) FROM table_name GROUP BY column;
  -- 묶여진 개수 조회
  SELECT COUNT(column) FROM table_name GROUP BY column;
  ```

#

- **Changing Data**

  - 데이터를 삽입, 수정, 삭제하기

  1.  INSERT

  - 새로운 데이터(행)을 테이블에 삽입

    ```SQL
    -- 단일 행 삽입하기
    INSERT INTO table_name (column1, column2, column3)
    VALUES (data1, data2, data3)
    -- or
    INSERT INTO table_name
    VALUES (data1, data2, data3)

    -- 여러 행 삽입하기
    INSERT INTO table_name
    VALUES
    	(data1, data2, data3),
    	(data11, data22, data33),
    	(data111, data222, data333),
    ```

  2.  UPDATE

  - 기존 데이터를 변경

  ```SQL
  -- table에서 조건에 해당하는 데이터 행의 column1,2를 data1,2로 수정
  UPDATE table_name
  SET column1=date1,
  		column2=date2
  WHERE ...
  ```

  3. DELETE

  - 기존 행을 제거
  - `ORDER BY, LIMIT`을 이용해서 삭제할 행 수 지정 가능

  ```SQL
  DELETE FROM table_name
  WHERE ...
  ```
