//2017 카카오 코드 예선
/*
도시 중심가의 지도는 m × n 크기의 격자 모양 배열 city_map으로 주어진다.
자동차는 오른쪽 또는 아래 방향으로 한 칸씩 이동 가능하다.

city_map[i][j]에는 도로의 상황을 나타내는 값이 저장되어 있다.

0인 경우에는 자동차가 자유롭게 지나갈 수 있다.
1인 경우에는 자동차 통행이 금지되어 지나갈 수 없다.
2인 경우는 보행자 안전을 위해 좌회전이나 우회전이 금지된다.
(왼쪽에서 오던 차는 오른쪽으로만, 위에서 오던 차는 아래쪽으로만 진행 가능하다)

도시의 도로 상태가 입력으로 주어졌을 때,
왼쪽 위의 출발점에서 오른쪽 아래 도착점까지 자동차로 이동 가능한 전체 가능한 경로 수를 출력하는 프로그램을 작성하라.
이때 가능한 경로의 수는 컴퓨터가 표현할 수 있는 정수의 범위를 넘어설 수 있으므로, 
가능한 경로 수를 20170805로 나눈 나머지 값을 출력하라.
*/

//입출력
/*
입력은 도시의 크기를 나타내는 m과 n, 그리고 지도를 나타내는 2차원 배열 city_map으로 주어진다.
제한조건은 아래와 같다.

1 <= m, n <= 500
city_map의 크기는 m × n이다.
배열의 모든 원소의 값은 0, 1, 2 중 하나이다.
출발점의 좌표는 (0, 0), 도착점의 좌표는 (m - 1, n - 1)이다.
출발점과 도착점의 city_map[i][j] 값은 0이다.
*/

// dfs ( 시간초과 )
class Solution {
    int MOD = 20170805;
    int answer = 0;

    public int solution(int i, int j, int [][] cityMap){
        solutionRec(i-1,j-1,cityMap,0);
        return answer%MOD;
    }

    public void solutionRec(int i, int j, int[][] cityMap,int where){ // 처음 i j는 2,5, where 1은 오른쪽, 2는 아래에서온
        // 출발점 도착 out
        if ( i == 0 && j == 0) {
            answer++;
            return;
        }

        if ( i < 0 || j < 0 ) return; // 막다른길 out

        if ( cityMap[i][j] != 1 ){ // 현재 자리가 통행금지가 아닐때
            if (  cityMap[i][j] == 2 ){ // 좌,우회전 금지
                if ( where == 1 )
                    solutionRec(i,j-1,cityMap,1);
                else if ( where == 2 )
                    solutionRec(i-1,j,cityMap,2);
            }
            else{ // 통행가능
                solutionRec(i,j-1,cityMap,1);
                solutionRec(i-1,j,cityMap,2);
            }
        }
        return;
    }
}