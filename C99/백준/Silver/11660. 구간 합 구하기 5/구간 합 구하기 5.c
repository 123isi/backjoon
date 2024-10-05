#include <stdio.h>
int arr[1025][1025];
int li[1025][1025];
int main() {
    int n, m;
    scanf("%d %d", &n, &m);
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            scanf("%d", &arr[i][j]);
            li[i][j] = arr[i][j] + li[i-1][j] + li[i][j-1] - li[i-1][j-1];
        }
    }
    for (int i = 0; i < m; i++) {
        int x1, y1, x2, y2;
        scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
        int result = li[x2][y2]- li[x1-1][y2]- li[x2][y1-1]+ li[x1-1][y1-1];
        printf("%d\n", result);
    }
    
    return 0;
}
