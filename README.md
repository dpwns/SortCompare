# 정렬간 속도 비교

## 개요
퀵 정렬(피봇의 선택 방식에 따른 총 3가지 방식)과 힙 정렬 간의 시간, 비교 횟수, 교환 횟수를 비교하여 어느 방식이 효율적인지 알아보고자 함.

### 퀵 정렬
1. 현재 배열의 가장 앞에 있는 값을 피봇으로 설정   
2. 배열에서 무작위 값을 택하여 피봇으로 설정   
3. 배열의 가장 앞에 있는 값, 중간에 있는 값, 가장 뒤에 있는 값 중 중앙값을 선택하여 피봇으로 설정   

### 힙 정렬
내장된 heapq 모듈을 사용하지 않고, 직접 구현한 힙을 바탕으로 구현함

### 결과
무작위로 재배열된 배열을 정렬하는 각 테스트에 대한 실행 결과는 배열의 길이에 따라서 N100~N5000 폴더에 csv 파일로 저장됨   
분석된 결과는 시간, 비교 횟수, 교환 횟수, 평균, 표준편차가 각각 Analyze 폴더의 Time, Compare, Swap, Average, StandardDeviation에 저장됨

## 사용법
1. Algo.py 실행   
2. Analyze.py 실행   

## 결과 예시
![](https://github.com/dpwns/SortCompare/blob/main/Analyze/Time/Time_N5000.png)   
![](https://github.com/dpwns/SortCompare/blob/main/Analyze/Average/N5000Average.png)

## 사용 언어
Python
