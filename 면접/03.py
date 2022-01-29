"""
문제 설명
n 개의 '(' 와 m 개의 ')' 를 이용해 문자열을 만들려고 합니다. 이때, 완성된 문자열이 반드시 올바른 괄호 문자열일 필요는 없으며, 반드시 모든 문자를 사용해야 합니다. '(' 의 개수 n과 ')'의 개수 m이 매개변수로 주어질 때, n개의 '('와 m개의 ')'를 모두 사용해서 만들 수 있는 문자열의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
n은 1이상 16이하의 자연수입니다.
m은 1이상 16이하의 자연수입니다.
정답은 231 - 1 이하의 자연수입니다.

입출력 예
n	m	result
1	1	2
1	2	3

입출력 예 설명
입출력 예 #1
"()", ")(" 의 2가지 문자열을 만들 수 있습니다.

입출력 예 #2
"())", ")()", "))(" 의 3가지 문자열을 만들 수 있습니다.
"""
"""
class Solution {
    public int solution(int n, int m) {
        int answer = 0;
        return answer;
    }
}
"""
import itertools

n = 4
m = 5


def solution(n, m):
    answer = 0
    # 1로 이루어진 2차원 배열 생성
    a_list = [[1 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(len(a_list)):
        for j in range(len(a_list[i])):
            # x, y의 이전 값의 합값으로 바꿔주기
            if i >= 1 and j >= 1:
                a_list[i][j] = a_list[i][j - 1] + a_list[i - 1][j]

    for h in a_list:
        print(h)

    answer = a_list[n][m]

    print("answer", answer)

    return answer


solution(n, m)
