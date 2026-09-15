# Linear_Algebra_1

# 선형대수학 1 실습

선형대수학 1 수업 실습 코드 및 자료를 정리하는 레포지토리입니다.

## 소개

선형대수학 1 수업에서 다루는 전반적인 내용을 실습을 통해 정리합니다. 구체적인 주제는 수업 진도에 맞춰 점차 채워나갈 예정입니다.

## 커밋 메시지 컨벤션

`타입: 내용` 형식으로 작성합니다.

- `feat`: 새로운 기능 추가
- `fix`: 버그 수정
- `docs`: 문서 수정 (README 등)
- `style`: 코드 스타일 수정 (포맷팅, 세미콜론 등 로직 변경 없음)
- `refactor`: 코드 리팩토링
- `chore`: 빌드 설정, 패키지 매니저 설정 등 (코드 로직 변경 없음)

## 실행 방법

### Python

```bash
python3 week2/실습week2_1.py
python3 week2/실습week2_2.py
python3 week3/실습week3_1.py
python3 week3/실습week3_2.py
python3 week3/과제week3.py
```

### C/C++

C++ 컴파일러는 `clang++`를 사용합니다.

```bash
clang++ week2/실습week2_3.cpp -o 실습week2_3
./실습week2_3
```

컴파일러 설치 여부는 아래 명령어로 확인할 수 있습니다.

```bash
clang++ --version
```

## 진행 상황

- [x] 레포 생성
- [x] 2주차 과제
  - [x] 최소제곱법으로 공통해 계산 (Python)
  - [x] 연립방정식 시각화 (Python)
  - [x] 크래머 공식으로 해 계산 및 검증 (C)
- [x] 3주차 과제
  - [x] 정방행렬 덧셈 구현 (Python)
  - [x] 행렬 곱셈 구현 (Python)
  - [x] 행렬 대각합 계산: 순수 Python 및 numpy 비교 (Python)
