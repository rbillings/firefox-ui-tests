# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from firefox_ui_harness.testcase import FirefoxTestCase

from marionette_driver import By


class TestGoButton(FirefoxTestCase):
    """ This replaces
    This replaces http://hg.mozilla.org/qa/mozmill-tests/file/default/firefox/tests/functional/testAwesomeBar/testGoButton.js
    Check a go button displays after text has been added to the awesome bar, takes user to correct results.
    """

    def setUp(self):
        FirefoxTestCase.setUp(self)

    def test_gobutton(self):
        # no input, go button should not display
        go_button = self.browser.navbar.go_button
        self.assertFalse(go_button.is_displayed())

        # add input, go button displays, click go button
        input_text = 'mozilla.org/'
        locationbar = self.browser.navbar.locationbar
        locationbar.urlbar.send_keys(input_text)
        go_button = self.marionette.find_element(By.ID, 'gobutton')
        go_button.click()

        # landing page matches input, go button no longer displays
        self.assertEqual(locationbar.value, 'mozilla.org/')
        self.assertFalse(go_button.is_displayed())

    def tearDown(self):
        FirefoxTestCase.tearDown(self)
