#Feature: Login
#
#  Scenario: Success
#    Given: go to login page
#    When: login with admin admin
#    Then: redirect to dashboard page
#
#  Scenario Outline: Failed
#    Given: go to login page
#    When: login with <username> and <password>
#    Then: should display error <message>
#
#    Examples: data
#      | username     | password   | message
#      | admin        |incorrect   | 错误: admin 的密码不正确
#      | empty        | admin      | 错误: 用户名一栏为空
Feature: Login

  @success
  Scenario: Success
  Given go to login page
  When login with admin admin
  Then redirect to dashboard page

  @failed
  Scenario Outline: Failed
    Given go to login page again
    When let us login with incorrect <username> and incorrect <password>
    Then should display error <message>

	Examples: data
	| username         | password         | message  								|
	| admin 		   | incorrect        | 错误：admin 的密码不正确。忘记密码了？  |
	| empty 		   | admin        	  | 错误：用户名一栏为空。  				|
	| admin 		   | empty        	  | 错误：密码一栏为空。