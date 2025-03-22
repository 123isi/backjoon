#include <stdio.h>

// 재귀적으로 파스칼의 삼각형의 C(n, k) 값을 계산하는 함수
int pascal(int n, int k) {
    // 기저 조건: C(n, 0) = 1 또는 C(n, n) = 1
    if (k == 0 || k == n) {
        return 1;
    }
    // 재귀 호출: C(n, k) = C(n-1, k-1) + C(n-1, k)
    return pascal(n - 1, k - 1) + pascal(n - 1, k);
}

int main() {
    int n, k;

    // 줄 번호(n)와 위치 번호(k) 입력 받기
    scanf("%d %d", &n, &k);

    // 파스칼의 삼각형의 값 계산 및 출력
    printf("%d\n", pascal(n - 1, k - 1));

    return 0;
}
