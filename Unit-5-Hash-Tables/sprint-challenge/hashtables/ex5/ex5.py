# Your code here



def finder(files, queries):
    """
    Accepts a list of file paths and list of queries, or file names. Return paths
        for those files that exist in the system.
    """
    path_table = {}
    for path in files:
        file_name = path.split("/")[-1]
        if file_name in path_table:
            path_table[file_name].append(path)
        else:
            path_table[file_name] = [path]
    
    results = []
    for query in queries:
        if query in path_table:
            results.extend(path_table[query])

    return results


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
