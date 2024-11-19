def factorial_mod(N, M):
    # 조기 종료: N이 M 이상이면 나머지는 0
    if N >= M:
        return 0

    # 모듈러 연산으로 팩토리얼 계산
    result = 1
    for i in range(2, N + 1):
        result = (result * i) % M
        # 추가 최적화: 결과가 이미 0이면 더 이상 계산할 필요 없음
        if result == 0:
            break

    return result

# 입력 처리
N, M = map(int, input().split())

# 출력
print(factorial_mod(N, M))
