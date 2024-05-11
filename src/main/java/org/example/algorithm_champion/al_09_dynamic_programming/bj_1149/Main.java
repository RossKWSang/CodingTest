package org.example.algorithm_champion.al_09_dynamic_programming.bj_1149;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    private static int[][] minimumCost = new int[3][1001];
    private static int[] costInput;
    private static int result = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int houseNumber = Integer.parseInt(br.readLine());

        costInput = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        for (int i=0; i<3; i++) {
            minimumCost[i][1] = costInput[i];
        }

        for (int i=2; i<=houseNumber; i++) {
            costInput = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();

            minimumCost[0][i] = (minimumCost[1][i - 1] < minimumCost[2][i - 1])
                    ? minimumCost[1][i - 1] + costInput[0] : minimumCost[2][i - 1] + costInput[0];

            minimumCost[1][i] = (minimumCost[0][i - 1] < minimumCost[2][i - 1])
                    ? minimumCost[0][i - 1] + costInput[1] : minimumCost[2][i - 1] + costInput[1];

            minimumCost[2][i] = (minimumCost[0][i - 1] < minimumCost[1][i - 1])
                    ? minimumCost[0][i - 1] + costInput[2] : minimumCost[1][i - 1] + costInput[2];
        }

        for(int i=0; i<3; i++) {
            if(result >= minimumCost[i][houseNumber]) {
                result = minimumCost[i][houseNumber];
            }
        }

        System.out.print(result);

    }
}
