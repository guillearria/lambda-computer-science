'''
Input: an integer
Returns: an integer
'''


def eating_cookies(n):
    def cookies(cookies_eaten, total_cookies):
        # "how many ways" tells me I can use recursion, its a combination problem
        # base cases:
        if cookies_eaten > total_cookies:
            return 0
        if cookies_eaten == total_cookies:
            return 1
        return cookies(cookies_eaten+1, total_cookies) + cookies(cookies_eaten+2, total_cookies) + cookies(cookies_eaten+3, total_cookies)

    return cookies(0, n)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
