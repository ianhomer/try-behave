from behave import *


@given("we have behave installed")
def when_we_have_installed(_context):
    pass


@when("we implement a test")
def we_implement_a_test(_context):
    assert True is not False


@then("behave will test it for us!")
def behave_will_test_it(context):
    assert context.failed is False
