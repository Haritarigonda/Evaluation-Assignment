class DataStream:
    def __init__(self):
        self.data_dict = {}

    def should_output_data_str(self, timestamp: int, data_string: str) -> bool:
        if data_string not in self.data_dict or timestamp - self.data_dict[data_string] >= 5:
            self.data_dict[data_string] = timestamp
            return True
        else:
            return False

data_stream = DataStream()
output = [
    data_stream.should_output_data_str(timestamp=0, data_string="hello"),
    data_stream.should_output_data_str(timestamp=1, data_string="world"),
    data_stream.should_output_data_str(timestamp=6, data_string="hello"),
    data_stream.should_output_data_str(timestamp=7, data_string="hello"),
    data_stream.should_output_data_str(timestamp=8, data_string="world")
]
print(output)  # Output: [True, True, True, False, True]