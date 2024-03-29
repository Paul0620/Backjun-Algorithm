"""
문제 설명
n개의 블록이 일렬로 나열되어 있습니다. 같은 색깔의 블록이 두 개 이상 인접해 있으면, 그 블록들은 하나의 블록 덩어리가 됩니다.

예를 들어, 다음 그림은 2개, 3개, 3개, 2개짜리 블록 덩어리로 구성되어 있습니다.

collapse_img.png

이때, 한 블록을 클릭하면 그 블록이 속한 덩어리가 모두 없어지면서, 블록의 수의 제곱만큼의 점수를 얻게 됩니다. 물론 한 개짜리 덩어리도 클릭해서 없앨 수 있습니다. 우리는 모든 블록을 없애서 얻을 수 있는 최대 점수를 알고 싶습니다.

그런데, 블록들을 클릭하는 순서에 따라 얻을 수 있는 점수가 다를 수 있습니다. 위 그림의 예에서, 왼쪽 덩어리부터 하나씩 없애가면 얻을 수 있는 점수는 4 + 9 + 9 + 4 = 26점이지만, 빨간색 덩어리와 초록색 덩어리를 없앤 후 합쳐진 노란색 덩어리를 없애면 4 + 9 + 25 = 38점입니다.

블록의 수 n과 각 블록의 색깔을 나타내는 배열 colors가 매개변수로 주어질 때, 모든 블록을 없애서 얻을 수 있는 최대 점수를 return 하도록 solution 함수를 완성해주세요.

제한사항
n은 200 이하의 자연수입니다.
배열 colors의 각 원소는 1 이상 n 이하의 자연수로 표현됩니다.

입출력 예
n	    colors	            answer
10	[1,1,2,2,2,3,3,3,2,2]	38

입출력 예 설명
입출력 예 #1
위의 예시와 같습니다.
"""
"""
java
class Solution {
    public int solution(int n, int[] colors) {
        int answer = 0;
        return answer;
    }
}
"""
