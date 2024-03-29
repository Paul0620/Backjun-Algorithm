"""
문제 설명
주식회사 xx소프트는 신사옥을 짓기로 했습니다. 건물의 모양은 위에서 바라보았을 때 'ㄷ'(디귿)자가 되도록 짓기로 했습니다. 건물을 짓기 위해서는 우선 땅이 필요했기 때문에 부지 매입을 위해 높이는 나중에 결정하기로 하고 어느 면적으로 지을지 먼저 정하기로 했습니다. 그 후 'ㄷ' 모양을 이루는 3개의 기다란 부분의 두께는 1로 결정을 했지만 길이는 정하지 못했습니다. 그러나 위에서 바라보았을 때 최대한 면적이 넓도록 짓고 싶었고 우선 건물을 지을 부지를 알아본 후에 다시 논의하기로 했습니다.
xx소프트는 오랜 조사 끝에 N x M 크기의 부지를 찾았습니다. 그런데 문제는 이 부지는 N x M 개의 1 x 1 크기의 정사각형 모양의 작은 땅(이후 셀이라고 부르겠습니다)으로 나누어져 있는데 각각 셀 단위로 매매가 이루어져 왔기 때문에 셀 단위로 소유자가 다를 수도 있다는 것이었습니다. 특정 셀의 소유자는 대문자 알파벳으로 표현됩니다. 즉, 최대 26명의 소유자가 존재합니다. 한 명의 소유자는 여러 개의 셀의 땅을 소유할 수 있으며 한 셀의 땅은 반드시 한 명의 소유자에게 소유됩니다.
xx소프트는 한 명의 소유자가 소유한 셀들만 매입하려고 합니다. 또한 위에서 말했던 것처럼 xx소프트는 최대한 넓은 'ㄷ'자 모양의 건물을 짓고 싶고, 건물을 짓는 데에 필요하지 않은 부지에 자금을 낭비하고 싶지 않기 때문에 딱 건물을 짓는 데에 필요한 부지만 매입하고 싶습니다. 'ㄷ'자 모양의 부지의 정확한 정의는 아래와 같습니다.


위의 그림에 관해 설명하면, 'A'라는 한 명의 소유자가 소유한 땅이면서 이어져 있고, 마주 보는 두 부분의 길이가 같고 길이는 2 이상이며, 마주 보는 두 부분을 제외한 부분의 길이는 3 이상이어야 합니다. 또한, 두께는 1입니다.

아래는 4 x 3 크기의 부지에 존재하는 'ㄷ'자 모양인 부지들의 예시입니다.




마찬가지로 아래는 가로 4 x 3 크기의 부지에서 'ㄷ'자 모양의 부지가 아닌 예시입니다.


알파벳 대문자로 이루어진 N x M 크기의 부지에 대한 정보인 cells 가 주어질 때 건물을 짓기 위한 가장 넓은 'ㄷ'자 모양의 부지의 넓이를 return 하도록 solution 함수를 완성해주세요. (단, 'ㄷ'자 모양의 부지가 존재하지 않는다면 -1을 return 합니다)

제한사항
cells 는 부지의 정보가 담긴 1차원 문자열 배열입니다.
cells 의 세로 길이(N)와 가로 길이(M)는 1이상 100이하의 정수입니다.

입출력 예
cells	                    result
["AAA", "AAA", "AAA", "AAA"]	9
["BAA", "ABB", "ABB", "AAA"]	-1


입출력 예 설명
입출력 예 #1
가장 넓이가 큰 'ㄷ'자 모양 부지 중 하나는 아래와 같습니다. (선택되지 않은 칸은 _ 로 표시합니다.)
A_A
A_A
A_A
AAA

입출력 예 #2
주어진 격자 내에 'ㄷ'자 모양의 부지가 존재하지 않습니다.
"""
"""
java
class Solution {
    public int solution(String[] cells) {
        int answer = 0;
        return answer;
    }
}
"""
