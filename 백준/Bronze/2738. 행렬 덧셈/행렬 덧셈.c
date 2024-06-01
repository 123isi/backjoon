#include <stdio.h>
#include <stdlib.h>

int main(void){
    int x, y;
    int *arr1;
    int *arr2;

    // 배열의 크기 입력 받기
    scanf("%d %d", &x, &y);

    // 입력 크기에 따라 동적으로 배열 할당
    arr1 = (int*)malloc(x * y * sizeof(int));
    arr2 = (int*)malloc(x * y * sizeof(int));

    if (arr1 == NULL || arr2 == NULL) {
        printf("메모리 할당 실패\n");
        return 1;
    }

    // arr1에 요소 입력 받기
    for (int i = 0; i < x * y; i++) {
        scanf("%d", &arr1[i]);
    }

    // arr2에 요소 입력 받기
    for (int i = 0; i < x * y; i++) {
        scanf("%d", &arr2[i]);
    }

    // 각 요소의 합을 출력
    for (int i = 0; i < x; i++) {
        for (int j = 0; j < y; j++) {
            printf("%d ", arr1[i * y + j] + arr2[i * y + j]);
        }
        printf("\n");
    }

    // 동적 할당된 메모리 해제
    free(arr1);
    free(arr2);

    return 0;
}
