from gendiff.finding_difference import determining_file_format,\
    finding_difference


def generate_diff(file_path1, file_path2):
    file1 = determining_file_format(file_path1)
    file2 = determining_file_format(file_path2)
    return finding_difference(file1, file2)
