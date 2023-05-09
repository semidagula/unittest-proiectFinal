import unittest

import HtmlTestRunner

from ProiectUnittestShein.login_tests import TestLoginPage
from ProiectUnittestShein.cautare_prod_test import TestCautareProduse



class MyTestSuites(unittest.TestCase):

    # se ruleaza testele si se vor crea rapoarte
    def test_suite(self):
        smoketest = unittest.TestSuite()
        smoketest.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestLoginPage),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestCautareProduse),


        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            report_title='Report', report_name='smoke Test', combine_reports=True
        )
        runner.run(smoketest)
