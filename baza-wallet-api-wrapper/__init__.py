from typing import Dict

from .baza import BazaAPIWrapper


class DaemonApiWrapperManager(object):
    api_wrappers: Dict = {}

    def initialize_api_wrappers(self):
        self.api_wrappers['baza'] = BazaAPIWrapper()
        res = self.api_wrappers['baza'].open_wallet()
        if res.status_code == 403:
            self.api_wrappers['baza'].wallet_is_open = True
        if res.status_code == 400 and res.json()['errorCode'] == 1:
            res = self.api_wrappers['baza'].create_wallet()
        if res.status_code == 200:
            self.api_wrappers['baza'].wallet_is_open = True


daemon_api_wrapper_manager = DaemonApiWrapperManager()

# On app initialization add this line

daemon_api_wrapper_manager.initialize_api_wrappers()
