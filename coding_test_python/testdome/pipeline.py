def create_pipeline(*functions):
    def pipeline(input_data):
        result = input_data
        for func in functions:
            result = func(result)
        return result

    return pipeline


pipeline = create_pipeline(
    lambda x: x * 3,
    lambda x: x + 1,
    lambda x: x / 2
)

print(pipeline(3))