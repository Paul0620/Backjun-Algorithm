"""
문제 설명
4, 13, 413, 134와 같이 숫자가 13과 4를 이용해서 만들 수 있는 수를 불행한 수(Unlucky Number)라고 정의하겠습니다. 그리고 불행한 수가 오름차순으로 나열된 수열을 불행한 수열이라고 하겠습니다. 예를 들면 불행한 수열은 다음과 같이 나열될 수 있습니다.

S = {4, 13, 44, 134, 413, 444, 1313…. }

n이 매개변수로 주어질 때, 불행한 수열에서 n번째 불행한 수를 return 하도록 solution 함수를 완성해주세요.

제한 사항
n은 5,000 이하의 자연수입니다.

입출력 예
n	result
1	4
2	13
3	44

입출력 예 설명
문제 설명에 있는 수열을 참고해 주세요.
"""
"""
java
class Solution {
    public long solution(int n) {
        long answer = 0;
        return answer;
    }
}
"""

import itertools


def solution(n):
    a = ["4", "13"]
    s = []

    for j in range(1, n + 1):
        s += [int("".join(i)) for i in itertools.product(a, repeat=j)]

        print(len(s))

        if len(s) > 5000:
            break

    s = sorted(s)

    answer = s[n - 1]

    return answer


print(solution(5000))
