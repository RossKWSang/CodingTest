package org.example.bj16713;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.stream.IntStream;

public class Main {

    private static int[] initialInputArray;

    private static int[] numberArray;

    private static int[] indexArray;

    private static int getQueryResult(int startIndex, int endIndex) {
        int[] rangedArray = Arrays.copyOfRange(numberArray, startIndex-1, endIndex);
        if (rangedArray.length == 1) {
            return rangedArray[0];
        }
        return IntStream.of(rangedArray).boxed().reduce((x, y) -> x ^ y).get();
    }

    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        initialInputArray = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        numberArray = Arrays.stream(br.readLine().split(" "))
                .mapToInt(Integer::parseInt)
                .toArray();

        int result = -999999999;
        for (int i=0; i<initialInputArray[1]; i++) {
            indexArray = Arrays.stream(br.readLine().split(" "))
                    .mapToInt(Integer::parseInt)
                    .toArray();
            if (result == -999999999) {
                result = getQueryResult(indexArray[0], indexArray[1]);
                continue;
            }
            result ^= getQueryResult(indexArray[0], indexArray[1]);
        }
        bw.write(String.valueOf(result));
        bw.flush();
    }
}
