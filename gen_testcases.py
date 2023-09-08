from more_itertools import chunked


def get_clean_lines(raw_str: str) -> list[str]:
    ans = []
    for line in raw_str.splitlines():
        s = line.strip()
        if s:
            ans.append(s)
    return ans


if __name__ == '__main__':
    # Copy LeetCode testcases source and paste here.
    # Extra empty lines or double-end-spaces are allowed.
    cases = get_clean_lines('''
2
3
4
-6
-4
-6
0
1
-3
8
    ''')

    # Provide the expected answers here, 1 line for 1 answer.
    # Extra empty lines or double-end-spaces are allowed.
    answers = get_clean_lines('''
5
-2
-10
1
5
    ''')

    x, y = len(cases), len(answers)
    assert x % y == 0, f'numbers of lines of testcases and answers mismatch: {(x, y)}'
    arg_cnt = x // y

    for args, want in zip(chunked(cases, arg_cnt, strict=True), answers):
        print('((', end='')
        print(', '.join(args), end='' if not args else ',')
        print('), {}, ', end='')
        print(want, end='')
        print('),')
