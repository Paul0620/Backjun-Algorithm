"""
문제 설명
앞에서부터 읽을 때와 뒤에서부터 읽을 때 똑같은 단어를 팰린드롬(palindrome)이라고 합니다. 예를들어서 racecar, 10201은 팰린드롬 입니다.

두 자연수 n, m이 매개변수로 주어질 때, n 이상 m 이하의 자연수 중 팰린드롬인 숫자의 개수를 return 하도록 solution 함수를 완성해 주세요.

제한사항
m은 500,000이하의 자연수이며, n은 m 이하의 자연수입니다.

입출력 예
n	m	result
1	100	18
100	300	20

입출력 예 설명
입출력 예 #1
1 이상 100 이하의 팰린드롬은 다음과 같이 18개가 있습니다.
1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99

입출력 예 #2
100 이상 300 이하의 팰린드롬은 다음과 같이 20개가 있습니다.
101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, 212, 222, 232, 242, 252, 262, 272, 282, 292
"""

"""
java
class Solution {
    public int solution(int n, int m) {
        int answer = 0;

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        System.out.println("Hello Java");

        return answer;
    }
}
"""


def solution(n, m):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in range(n, m + 1):
        sNum = str(i)
        check = True
        for j in range(len(sNum) // 2):
            if sNum[j] != sNum[-1 - j]:
                check = False

        if check:
            answer += 1

    return answer
