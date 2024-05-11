package org.example.algorithm_champion.al_09_dynamic_programming.bj_11726;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static long[] intCache = new long[1001];


    private static long countTile(int size) {
        if (size <= 2) {
            return intCache[size];
        }
        if (intCache[size] > 0) {
            return intCache[size];
        }
        intCache[size] = (countTile(size - 1) + countTile(size - 2)) % 10007;
        return intCache[size];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tile_size = Integer.parseInt(br.readLine());

        intCache[1] = 1;
        intCache[2] = 2;

        System.out.println(countTile(tile_size));
    }
}
