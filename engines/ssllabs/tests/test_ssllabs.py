from PatrowlEnginesUtils.PatrowlEngineTest import PatrowlEngineTest

# Define the engine instance
pet = PatrowlEngineTest(engine_name="ssllabs", base_url="http://127.0.0.1:5004/engines/ssllabs")

# generic tests
def test_generic_features():
    pet.do_generic_tests()

## custom tests
def test_ssllabs_check_google():
    pet.custom_test(
        test_name="ssllabs_check_google",
        assets=[{
            "id": '1',
            "value": 'https://www.google.com',
            "criticity": 'high',
            "datatype": 'url'
        }],
        scan_policy={},
        is_valid=True
    )


if __name__ == '__main__':
    test_generic_features()
    test_ssllabs_check_google()
