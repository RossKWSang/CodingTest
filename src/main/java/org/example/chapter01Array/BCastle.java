package org.example.chapter01Array;

/*
모든 행과 열에 경비원이 최소 한 명씩 있어야할 때 추가로 필요한 경비원의 최소 수
 */

import java.util.Scanner;

public class BCastle {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int M = sc.nextInt();
        char[][] map = new char[N][M];
        for (int i = 0; i < N; i++) {
            map[i] = sc.next().toCharArray();
        }
    }

}
