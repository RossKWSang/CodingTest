package org.example.algorithm_champion.al_01_bruteforce.bj_4673;

public class Main {

    static int[] selfNumberIndex = new int[10001];

    private static void constructor(int inputInteger) {
        int sumOfDigits = 0;
        int originalNumber = inputInteger;

        // 각 자리수의 합을 구하는 과정
        while (inputInteger > 0) {
            sumOfDigits += inputInteger % 10;
            inputInteger /= 10;
        }

        sumOfDigits += originalNumber;

        if (sumOfDigits <= 10000) {
            selfNumberIndex[sumOfDigits] = 1;
        }
    }

    public static void main(String[] args) {
        for (int i=0; i < 10001; i++) {
            constructor(i);
        }

        for (int i=0; i < 10001; i++) {
            if (selfNumberIndex[i] != 1) {
                System.out.println(i);
            }
        }
    }
}
