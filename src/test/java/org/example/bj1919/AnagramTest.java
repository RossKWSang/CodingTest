package org.example.bj1919;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import java.util.Arrays;
import java.util.List;
import java.util.function.BiFunction;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

import static org.assertj.core.api.AssertionsForClassTypes.assertThat;

public class AnagramTest {
    @Test
    @DisplayName(value="인코딩 함수(문자열 -> 벡터) 동작 테스트")
    void makeAlphabetCountVectorForSingleStringTest() {
        Function<String, List<Integer>> stringEncoder = Anagram::makeAlphabetCountVectorForSingleString;
        assertThat(stringEncoder.apply("aabbcc"))
                .isEqualTo(
                        Stream.concat(
                                Stream.of(Arrays.asList(2, 2, 2)).flatMap(List::stream),
                                IntStream.generate(() -> 0).limit(23).boxed()
                        )
                                .collect(Collectors.toList())
                );
    }

    @Test
    @DisplayName(value="두 벡터의 차이 절대값의 합을 구하는 테스트 ")
    void absoluteSumForSubtractionOfTwoVectors() {
        BiFunction<List<Integer>, List<Integer>, Integer> distanceMeasurer = Anagram::absoluteSumForSubtractionOfTwoVectors;
        assertThat(distanceMeasurer.apply(
                Arrays.asList(2, 2, 2),
                Arrays.asList(2, 3, 1)
                )
        )
                .isEqualTo(2);
    }
}
