def flatten(input_list:list[list]) -> list:
    output_list = []
    for i in input_list:
        for j in i:
            output_list.append(j)
    return output_list

def flat_to_int(input_list:list[int]) -> int:
    str_list = [str(i) for i in input_list]
    return int(f"0b{''.join(str_list)}", base=0)
