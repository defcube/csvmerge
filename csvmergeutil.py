def _find_common_item(list_of_lists):
    for item in list_of_lists[0]:
        if all([item in x for x in list_of_lists]):
            return item
    raise KeyError()


def find_common_header(first_rows, args):
    if not args.merge_field_name:
        try:
            return _find_common_item(first_rows)
        except KeyError:
            exit("Can not find a common CSV header")
    else:
        if not all([args.merge_field_name in x for x in first_rows]):
            exit("Can not find merge_field_name in all CSV files")
        return args.merge_field_name


def find_common_header_indexes(first_rows, common_header):
    return [x.index(common_header) for x in first_rows]


def find_and_pop_rows_to_merge(common_item_value, csv_file_data_sets,
                              common_header_indexes, first_rows):
    res = []
    for data_set_index, csv_file_data_set in enumerate(csv_file_data_sets):
        matching_rows = filter(
            lambda x: x[1][common_header_indexes[data_set_index]] ==
                             common_item_value,
                    enumerate(csv_file_data_set))
        if not matching_rows:
            matching_rows = [(None, ["" for x in \
                                      first_rows[data_set_index]])]
        if len(matching_rows) > 1:
            raise RuntimeError("Found too many rows for {0}".format(
                common_item_value))
        matching_rows[0][1].pop(common_header_indexes[data_set_index])
        res.append(matching_rows[0][1])
        if matching_rows[0][0] is not None:
            csv_file_data_set.pop(matching_rows[0][0])
    return res



def clean_data_sets(csv_file_data_sets):
    output_sets = []
    for csv_file_data in csv_file_data_sets:
        output_sets.append([x for x in csv_file_data if x])
    return output_sets
