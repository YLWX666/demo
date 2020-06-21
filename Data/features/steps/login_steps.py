from behave import *


@given('go to login page again')
def step_impl(context):
    context.dr.get('http://www.maiziedu.com/')


@when('login with {username} and {password}')
def step_impl(context,username,password):
    db = context.dr.find_element_by_link_text('登录')
    db.click()
    context.dr.find_element_by_id('id_account_l').send_keys(username)
    context.dr.find_element_by_id('id_password_l').sned_keys(password)
    context.dr.find_element_by_id('login_btn').click()


@then('should display error {message}')
def step_impl(context,message):
    dis = context.dr.find_element_by_id('login-form-tips').text
    assert dis == message