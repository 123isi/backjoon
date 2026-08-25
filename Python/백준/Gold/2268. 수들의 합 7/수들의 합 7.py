import sys
input=sys.stdin.readline
output=sys.stdout

n, m = map(int, input().split())


def merge(left, right):
    return left + right  # max(left, right), gcd(left, right) ...


default = 0  # default
segment_tree = [0] * n * 4  # 세그먼트 트리의 크기는 데이터의 개수 * 4


def build(arr, node, start, end):
    # arr : 데이터 배열
    # node : 몇번째 노드
    # start, end : 데이터 배열에서의 start, end 범위

    if start == end:  # 만약 범위가 1이라면 리프노드이므로, 세그먼트 트리의 해당 노드에 해당 데이터를 저장
        segment_tree[node] = arr[start]
        return segment_tree[node]  # 리프 노드를 반환

    mid = (start + end) // 2  # 세그먼트 트리는 이진 트리이기 때문에 왼쪽 반과 오른쪽 반을 나눔
    segment_tree[node] = merge(build(arr, node * 2, start, mid), build(arr, node * 2 + 1, mid + 1, end))
    return segment_tree[node]
# 만약 리프노드가 아니라면 자식 노드 두개를 Merge 한 것을 부모노드에 저장


def query(left, right, node, start, end):
    # left, right : 쿼리의 범위
    if left > end or right < start:  # start가 right보다 오른쪽이거나 end가 left 보다 왼쪽이라면 범위를 완전히 벗어난 것이므로 default 값을 반환
        return default
    if left <= start and end <= right:  # 범위에 완전히 포함될 경우 그 노드 값을 반환
        return segment_tree[node]

    mid = (start + end) // 2
    return merge(query(left, right, node * 2, start, mid), query(left, right, node * 2 + 1, mid + 1, end))


def update(index, value, node, start, end):
    # left, right : 쿼리의 범위
    if index < start or index > end:  # start가 right보다 오른쪽이거나 end가 left 보다 왼쪽이라면 범위를 완전히 벗어난 것이므로 default 값을 반환
        return segment_tree[node]  # 업데이트가 일어나지 않기 때문에 그대로의 값을 반환
    if start == end:
        segment_tree[node] = value
        return segment_tree[node]

    mid = (start + end) // 2
    segment_tree[node] = merge(update(index, value, node * 2, start, mid),
                               update(index, value, node * 2 + 1, mid + 1, end))
    return segment_tree[node]

build([0 for _ in range(n)], 1, 0, n - 1)
for i in range(m):
    a, b, c = map(int, input().split())

    if a == 0:
        if b < c:
            print(query(b-1, c-1, 1, 0, n - 1))
        else:
            print(query(c - 1, b - 1, 1, 0, n - 1))
    else:
        update(b-1, c, 1, 0, n - 1)