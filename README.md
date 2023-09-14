# Python-Demo-browserstack

[Python](https://www.browserstack.com/automate/python) Integration with BrowserStack

![BrowserStack Logo](https://d98b8t1nnulk5.cloudfront.net/production/images/layout/logo-header.png?1469004780)

## Prerequisites

* [Brew](https://docs.brew.sh/Installation) (Optional)
* Python3 (Installation notes [here](https://gist.github.com/RathilVasani/0ab70692688b3632d447ced5c277a9be))(Recommended Python version 3.6 & 3.7)
* [BrowserStack Automate](https://www.browserstack.com/automate) account with at least 4 parallel tests. Signup for a free trial [here](https://www.browserstack.com/users/sign_up).

## Setup

* Clone the repo
* Install dependencies `pip3 install -r requirements.txt`
* Export the environment variables for the Username and Access Key of your BrowserStack account

  ```
  export BROWSERSTACK_USERNAME=<browserstack-username> &&
  export BROWSERSTACK_ACCESS_KEY=<browserstack-access-key>
  ```

* To start Local server execute `python -m http.server 8000` in the demo folder within terminal 

## Running your tests
* To run a single test, run `paver run single`
* To run local tests, run `paver run local`
* To run parallel tests, run `paver run parallel`
* To run Appium tests for IOS, run `paver run appium-android`
* To run Appium tests for Android, run `paver run appium-ios`
* To run Espresso tests,run `paver run espresso`
* To run XcuiTest tests,run `paver run xcuitest`
* To run Earlgrey tests,run `paver run earlgrey`

## Notes
* You can view your test results on the [BrowserStack Automate dashboard](https://www.browserstack.com/automate)
* To test on a different set of browsers, check out our [platform configurator](https://www.browserstack.com/automate/python#setting-os-and-browser)

## Additional Resources
* [Documentation for writing Automate test scripts in Python](https://www.browserstack.com/automate/python)
* [Customizing your tests on BrowserStack](https://www.browserstack.com/automate/capabilities)
* [Browsers & mobile devices for selenium testing on BrowserStack](https://www.browserstack.com/list-of-browsers-and-platforms?product=automate)
* [Using REST API to access information about your tests via the command-line interface](https://www.browserstack.com/automate/rest-api)

