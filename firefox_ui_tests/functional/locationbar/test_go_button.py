# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from firefox_ui_harness.testcase import FirefoxTestCase

from marionette_driver import By, Wait


class TestGoButton(FirefoxTestCase):

    def setUp(self):
        FirefoxTestCase.setUp(self)
        self.url = self.marionette.absolute_url('layout/mozilla.html')

    def test_gobutton(self):
        # no input, go button should not display
        go_button = self.browser.locationbar.go_button
        self.assertEqual(go_button.element.get_attribute('state'), 'disabled')

        # add input, go button displays, click go button
        url = self.marionette.absolute_url('layout/mozilla.html')
        urlbar.send_keys(url)
        self.assertEqual(go_button.element.get_attribute('state'), 'active')
        go_button.click()

        # landing page matches input, go button no longer displays
        target_url = self.browser.get_final_url(url)
        Wait(self.marionette).until(lambda mn: mn.get_url() == target_url)
        self.assertEqual(self.marionette.get_url(), self.url)
        self.assertFalse(go_button.is_displayed())
