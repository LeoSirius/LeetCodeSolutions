class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        res_dirs = []
        for dirent in dirs:
            if dirent == '..':
                res_dirs = res_dirs[:-1]
            elif dirent == '.' or dirent == '':
                continue
            else:
                res_dirs.append(dirent)
        
        res = ''
        for dirent in res_dirs:
            res += '/' + dirent
        return '/' if not res else res


def test(test_name, path, expected):
    res = Solution().simplifyPath(path)
    if res == expected:
        print(test_name + ' success.')
    else:
        print(test_name + ' failed.')


if __name__ == "__main__":
    path1 = "/home/";
    expected1 = "/home";
    test("test1", path1, expected1);

    path2 = "/../";
    expected2 = "/";
    test("test2", path2, expected2);

    path3 = "/home//foo/";
    expected3 = "/home/foo";
    test("test3", path3, expected3);

    path4 = "/a/./b/../../c/";
    expected4 = "/c";
    test("test4", path4, expected4);

    path5 = "/a/../../b/../c//.//";
    expected5 = "/c";
    test("test5", path5, expected5);

    path6 = "/a//b////c/d//././/..";
    expected6 = "/a/b/c";
    test("test6", path6, expected6);

    path7 = "/../"
    expected7 = '/'
    test('test7', path7, expected7)
