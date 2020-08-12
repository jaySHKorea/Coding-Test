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

// 점화식 찾기
/*
    cityMap[1][1] = cityMap[1][0] + cityMap[0][1] ( 둘다 갈 수 있을 때) 
    즉, cityMap[1][1] = 왼쪽에서 올때 + 위쪽에서 올때
*/

//DP
class Solution {
    int MOD = 20170805;
    int answer = 0;

    // where 0,1을 따르는 배열 만들기
    public int solution(int m, int n, int [][] cityMap){

        int[][] right = null; // 길 경로 개수 저장 배열  
        int[][] down = null;

        right = new int[501][]; //dp는 항상 한칸 더
        down = new int[501][];
        for ( int i = 0 ; i <= 500 ; i++ )
            right[i] = new int[501];
        for ( int i = 0 ; i <= 500 ; i++ )
            down[i] = new int[501];

        for (int i = 0 ; i <= 500 ; i++)
            for (int j = 0 ; j <= 500 ; j++){
                right[i][j] = 0;
                down[i][j] = 0;
            }

        right[1][1] = 1;
        down[1][1] = 1;

        // road 배열 채우기
        for ( int i = 1 ; i <= m ; i++ ){
            for ( int j = 1 ; j <= n ; j++ ){
                // 현재 자리가 0, 통행금지 자리일 때
                if ( cityMap[i-1][j-1] == 1){
                    right[i][j] = 0;
                    down[i][j] = 0;
                }
                // 현재 자리가 0, 통행가능 자리일 때 : 위+왼
                else if ( cityMap[i-1][j-1] == 0){
                    right[i][j] += (right[i][j-1] + down[i-1][j])%MOD;
                    down[i][j] += (right[i][j-1] + down[i-1][j])%MOD;
                }
                // 현재 자리가 2, 좌/우회전이 불가능한 자리일 때 ( 같은방향으로만 이동 가능 )
                else{
                    right[i][j] = right[i][j-1]; // 왼쪽에서 오른쪽으로 내려오는 경우
                    down[i][j] = down[i-1][j]; // 위에서 아래로 내려오는 경우
                }   
            }
        }
        return down[m][n]%MOD;
    }
}