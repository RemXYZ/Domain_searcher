import whois
# pip install python-whois
# more info:
# https://www.thepythoncode.com/article/extracting-domain-name-information-in-python
print(whois)

def is_registered():
    """
    A function that returns a boolean indicating
    whether a `domain_name` is registered
    """
    input()
    try:
        w = whois.whois("google.com")
        print(w)
    except Exception:
        print("NO")
        return False
    else:
        print("hello.com")
is_registered()
input()
exit()