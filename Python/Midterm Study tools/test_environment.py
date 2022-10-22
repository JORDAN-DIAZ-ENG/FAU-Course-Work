import csv

def sort_float_ranges(filein:str, fileout:str):
    # list with tuples (range_size, [row_min, row_max]), one for each row:
    rows_lst = []
    with open(filein, "r") as fin:
        with open(fileout, "w") as fout:
            csv_rdr = csv.reader(fin)
            csv_writer = csv.writer(fout)
            for row in csv_rdr:
                if len(row) > 0:
                    row_floats = [float(x) for x in row]
                    row_min = min(row_floats)
                    row_max = max(row_floats)
                    range_size = row_max - row_min
                    rows_lst.append((range_size, row_floats))

            sorted_rows_lst = sorted(rows_lst, reverse=True)
            for (row_range_size, floats_row) in sorted_rows_lst:
                csv_writer.writerow(floats_row)

sort_float_ranges("data.csv", "out.csv")
