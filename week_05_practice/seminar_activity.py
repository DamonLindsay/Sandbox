"""
WakaTIme
"""

name_to_score = {"Derek": 7, "Xavier": 80, "Bob": 612, "Chantanelle": 9}


def main():
    """Test"""
    max_value_length = len(str(max(name_to_score.values())))
    max_key_length = max((len(name) for name in name_to_score.keys()))

    for name, score in sorted(name_to_score.items(), key=lambda x: x[1], reverse=True):
        print(f"{name:{max_key_length}} = {score:{max_value_length}}")


main()
