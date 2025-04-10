while True:
    n = int(input())
    if n == 0:
        break

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    dist_a = dist_b = 0
    overtaking = 0
    prev_diff = 0  # 이전의 차이 (a - b)

    for i in range(n):
        dist_a += a[i]
        dist_b += b[i]
        diff = dist_a - dist_b

        # 부호가 바뀐 경우 (즉, 뒤에 있던 사람이 앞으로 간 경우)
        if prev_diff * diff < 0:
            overtaking += 1

        # 같은 위치일 경우, 방향을 잃었으므로 0으로 리셋
        if diff != 0:
            prev_diff = diff

    print(overtaking)
