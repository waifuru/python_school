import requests


def task_1():
    path_prefix = 'https://nghttp2.org/httpbin'
    headers = {'User-Agent': 'Python Learning Requests'}
    json_response = requests.get('https://nghttp2.org/httpbin/spec.json', headers=headers).json()
    path_dict = json_response["paths"]
    result_dict = {}
    for path in path_dict:
        print(path)
        methods_dict = path_dict[path]
        for http_method in methods_dict:
            print("    " + http_method)
            for response_code in methods_dict[http_method]['responses']:
                print("        " + response_code)
                if response_code != '200':
                    result_dict[path_prefix + path] = response_code
    return result_dict


if __name__ == '__main__':
    print(task_1())

    r = requests.get('https://httpbin.org/get')
    print(r)

    r = requests.put("http://httpbin.org/put")
    print(r)

    r = requests.delete("http://httpbin.org/delete")
    print(r)

    r = requests.head("http://httpbin.org/get")
    print(r)

    r = requests.options("http://httpbin.org/get")
    print(r)

    payload = {'key1': 'value1', 'key2': 'value2'} #kek.com/pass?key1=value1&key2=value2
    r = requests.get("http://httpbin.org/get", params=payload)
    print(r)

    payload = {'key1': 'value1', 'key2[]': ['value2', 'value3']}
    r = requests.get("http://httpbin.org/get", params=payload)
    print(r.text)

    r = requests.get('https://httpbin.org/links/0/1')
    print(r.text)

    url = 'https://httpbin.org/get'
    headers = {'user-agent': 'my-app/0.0.1'}
    r = requests.get(url, headers=headers)
    print(r.headers)

    post_data = {'key1': 'value1', 'key2': 'value2'}
    headers = {'user-agent': 'rtfm/0.0.1'}
    r = requests.post("http://httpbin.org/post", data=post_data, headers=headers)
    print(r.text)

    r = requests.get('https://httpbin.org/get')
    print(r.json())

    url = 'https://httpbin.org/basic-auth/user/passwd'
    r = requests.get(url, auth=('user', 'passwd'))
    print(r.json())

    try:
        response = requests.get('https://httpbin.org/status/500')
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print('Oops. HTTP Error occured')
        print('Response is: {content}'.format(content=err.response.reason))

    try:
        response = requests.get('http://urldoesnotexistforsure.bom')
    except requests.exceptions.ConnectionError:
        print('Seems like dns lookup failed..')

    try:
        response = requests.get('https://httpbin.org/user-agent', timeout=(0.00001, 10))
    except requests.exceptions.ConnectTimeout:
        print('Oops. Connection timeout occured!')

    try:
        response = requests.get('https://httpbin.org/user-agent', timeout=(10, 0.0001))
    except requests.exceptions.ReadTimeout:
        print('Oops. Read timeout occured')
    except requests.exceptions.ConnectTimeout:
        print('Oops. Connection timeout occured!')

