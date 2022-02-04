import unittest
from task5.task5_1_1 import RestApiTasks


class TestRestApiTasks(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_task_1(self):
        result_map = RestApiTasks.task_1()
        self.assertNotEqual(None, result_map, 'Result should not be None')
        self.assertNotEqual(0, len(result_map), "Result should not be Empty")
        for value in result_map.values():
            self.assertNotEqual(200, value, "Result dictionary value should not be equal to 200")

    def test_task_2(self):
        form_data = {
            'custname': 'Sasha',
            'custtel': '+380785674312',
            'custemail': 'Sasha@gmail.com',
            'size': 'small',
            'topping': 'bacon',
            'delivery': '12:15',
            'comments': 'Deliver it faster!',
        }
        result = RestApiTasks.task_2(form_data, RestApiTasks.headers)
        response_form_data = result[0]
        response_headers = result[1]

        self.assertNotEqual(None, response_form_data, 'Result form data should not be None')
        self.assertNotEqual(None, response_headers, 'Result headers should not be None')

        self.assertEqual(len(form_data), len(response_form_data), "Response form data len should be as request body len")

        self.assertEqual(form_data.keys(), response_form_data.keys(), "Keys should be identical")

        required_response_headers = ["Accept", "Accept-Encoding", "Content-Length", "Host"]
        actual_response_headers = response_headers.keys()
        for header in required_response_headers:
            self.assertTrue(actual_response_headers.__contains__(header), "Response does not contain required header")

    def test_task_3_1(self):
        language_codes = RestApiTasks.task_3_1()
        self.assertNotEqual(None, language_codes, 'Result should not be None')
        self.assertNotEqual(0, len(language_codes), "Result should not be Empty")
        self.assertEqual(153, len(language_codes), "There must be present 153 language codes")
        for value in language_codes:
            self.assertFalse(len(value) == 0, "Language code must not be empty")

    def test_task_3_2(self):
        codes_population_dict = RestApiTasks.task_3_2(['nld', 'pap'])
        self.assertNotEqual(None, codes_population_dict, 'Result should not be None')
        self.assertNotEqual(0, len(codes_population_dict), "Result should not be Empty")
        self.assertEqual(2, len(codes_population_dict), "There must be present 2 entries")
        self.assertTrue(codes_population_dict.keys().__contains__('nld'), "'nld' lang must be present")
        self.assertTrue(codes_population_dict.keys().__contains__('pap'), "'pap' lang must be present")
        self.assertEqual(29127009, codes_population_dict['nld'], "nld population must be 29127009")
        self.assertEqual(287767, codes_population_dict['pap'], "pap population must be 287767")


if __name__ == '__main__':
    unittest.main()
