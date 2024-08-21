def my_languages(results):
    clean_dict = {key: value for key,value in results.items() if value >= 60}
    sorted_by_values = sorted(clean_dict.items(), key=lambda item: item[1], reverse = True)
    return [array[0] for array in sorted_by_values]