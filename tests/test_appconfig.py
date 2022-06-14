import logging
import logging.config
import pathlib
import unittest


from appconfig import AppConfig
from appconfig import app_config # global variable, singleton


class Test_AppConfig(unittest.TestCase):

    def setUp(self):
        self._appConfig = app_config
        pass

    def tearDown(self):
        pass

    def test_always_pass(self):
        self.assertTrue(True)

    def test_init_logging_FileNotFound(self):
        with self.assertRaises(FileNotFoundError):
            self._appConfig.init(root_path="nonsense")
        with self.assertRaises(FileNotFoundError):
            self._appConfig.init(logger_config_file='nonsense.logging.conf')
        with self.assertRaises(FileNotFoundError):
            self._appConfig.init(logger_config_file='config/nonsense.logging.conf')
        with self.assertRaises(FileNotFoundError):
            self._appConfig.init(logger_config_file='nonsense/test.logging.conf')
        
        # this should not raise exception, if there is a default config
        # appconfig = AppConfig(logger_config_file='config/test.logging.conf')

    def test_config_FileNotFound(self):
        with self.assertRaises(FileNotFoundError):
            self._appConfig.init(logger_config_file='config/test.logging.conf', config_file='nonsense/test.configdef.json')


    def test_correct_settings(self):
        self._appConfig.init(logger_config_file='config/test.logging.conf', config_file='config/test.configdef.json')
        logger = self._appConfig.logger
        logger.debug("Logger found")
        cfg = self._appConfig.config
        self.assertEqual(cfg["key_1"]["key_1_2"], "value_1_2_test")
        self.assertNotEqual(cfg["key_1"]["key_1_2"], "value_1_3_test")
        with self.assertRaises(KeyError):
            value = cfg["key_1"]["key_1_2_3"]
        with self.assertRaises(KeyError):
            value = cfg["key_3"]["key_1_2"]
        

if __name__ == "__main__":
    unittest.main()
