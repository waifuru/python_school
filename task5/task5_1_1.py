import requests


class RestApiTasks:

    headers = {'User-Agent': 'Python Learning Requests'}

    @staticmethod
    def task_1():
        path_prefix = 'https://nghttp2.org/httpbin'
        json_response = requests.get('https://nghttp2.org/httpbin/spec.json', headers=RestApiTasks.headers).json()
        path_dict = json_response["paths"]
        result_dict = {}
        for path in path_dict:
            methods_dict = path_dict[path]
            for http_method in methods_dict:
                for response_code in methods_dict[http_method]['responses']:
                    if response_code != '200':
                        result_dict[path_prefix + path] = response_code
        return result_dict

    @staticmethod
    def task_2(post_request_body, headers):
        json_response = requests.post("http://httpbin.org/post", data=post_request_body, headers=headers).json()
        form_dict = json_response['form']
        headers_dict = json_response['headers']
        return form_dict, headers_dict

    @staticmethod
    def task_3_1():
        json_response = requests.get("https://restcountries.com/v3.1/all", headers=RestApiTasks.headers).json()
        language_codes = []
        for country in json_response:
            languages = {}
            try:
                languages = country['languages']
            except KeyError:
                print("Languages are missing")
            for language_code in languages:
                if not language_codes.__contains__(language_code):
                    language_codes.append(language_code)
        return language_codes

    @staticmethod
    def task_3_2(language_codes):
        population_by_lang_code = {}
        for lang_code in language_codes:
            countries = requests.get("https://restcountries.com/v3.1/lang/" + lang_code, headers=RestApiTasks.headers).json()
            total_population = 0
            for country in countries:
                total_population += country["population"]
            population_by_lang_code[lang_code] = total_population
        return population_by_lang_code


if __name__ == '__main__':
    print("TASK 1")
    result1 = RestApiTasks.task_1()
    print(result1)
    print("----------------------------------------------------------\n")

    print("TASK 2")
    form_data = {
        'custname': 'Sasha',
        'custtel': '+380785674312',
        'custemail': 'Sasha@gmail.com',
        'size': 'small',
        'topping': 'bacon',
        'delivery': '12:15',
        'comments': 'Deliver it faster!',
    }
    result2 = RestApiTasks.task_2(form_data, RestApiTasks.headers)
    print("Response Form data:")
    print(result2[0])
    print("Response headers:")
    print(result2[1])
    print("----------------------------------------------------------\n")

    print("TASK 3.1")
    result3_1 = RestApiTasks.task_3_1()
    print(result3_1)
    print(len(result3_1))
    print("----------------------------------------------------------\n")

    print("TASK 3.2")
    result3_2 = RestApiTasks.task_3_2(['nld', 'pap'])
    print(result3_2)
    print("----------------------------------------------------------\n")
