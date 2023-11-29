package org.example.bj1919;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Anagram {

    public static List<Integer> makeAlphabetCountVectorForSingleString(String input) {
        List<Integer> result = IntStream.generate(() -> 0).limit(26).boxed().collect(Collectors.toList());
        input.chars()
                .forEach(ch -> {
                    if (Character.isAlphabetic(ch)) {
                        result.set(ch - 'a', result.get(ch - 'a') + 1);
                    }
                });
        return result;
    }

    public static int absoluteSumForSubtractionOfTwoVectors(List<Integer> vec1, List<Integer> vec2) {

        return IntStream
                .range(0, Math.min(vec1.size(), vec2.size()))
                .mapToObj(i -> Math.abs(vec1.get(i) - vec2.get(i)))
                .mapToInt(Integer::intValue)
                .sum();
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String word1 = br.readLine();
        String word2 = br.readLine();
        System.out.println(absoluteSumForSubtractionOfTwoVectors
                (
                        makeAlphabetCountVectorForSingleString(word1),
                        makeAlphabetCountVectorForSingleString(word2)
                )
        );
    }
}
