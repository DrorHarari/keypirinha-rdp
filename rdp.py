import keypirinha as kp
import keypirinha_util as kpu
import os
import winreg
import platform


class Rdp(kp.Plugin):
    ITEMCAT_RDP = kp.ItemCategory.USER_BASE + 1
    MSTSC = f'{os.environ["WINDIR"]}\\system32\\mstsc.exe'
    RDP_SERVERS = r"Software\Microsoft\Terminal Server Client\Servers"

    def __init__(self):
        super().__init__()

    def on_start(self):
        self.access_mode = winreg.KEY_READ
        if '32bit' in platform.architecture():
            self.access_mode |= winreg.KEY_WOW64_64KEY

    def on_activated(self):
        pass

    def on_deactivated(self):
        pass

    def on_events(self, flags):
        if flags & kp.Events.PACKCONFIG:
            self.on_catalog()

    def on_catalog(self):
        catalog = [
            self.create_item(
                    category=kp.ItemCategory.REFERENCE,
                    label="Rdp",
                    short_desc="Open a recent RDP session",
                    target="Rdp",
                    args_hint=kp.ItemArgsHint.REQUIRED,
                    hit_hint=kp.ItemHitHint.NOARGS)
        ]

        self.set_catalog(catalog)

    def on_suggest(self, user_input, items_chain):
        suggestions = []

        if user_input is None:
            return
        else:
            user_input = user_input.lower()

        servers = winreg.OpenKeyEx(winreg.HKEY_CURRENT_USER, self.RDP_SERVERS, 0, self.access_mode)

        n_subkeys, n_values, mod_time = winreg.QueryInfoKey(servers)
        for i in range(n_subkeys):
            server_key = winreg.EnumKey(servers, i).lower()
            if not user_input.lower() in server_key:
                continue

            user = ""
            try:
                server = winreg.OpenKey(winreg.HKEY_CURRENT_USER, f'{self.RDP_SERVERS}\\{server_key}', 0, self.access_mode)
                user = f' as {winreg.QueryValueEx(server, "UsernameHint")[0]}'
            except:
                pass
            suggestions.append(self.create_item(
                category=self.ITEMCAT_RDP,
                label=f'Connect to {server_key}{user}',
                short_desc=f'Connect to {server_key}',
                target=server_key,
                args_hint=kp.ItemArgsHint.FORBIDDEN,
                hit_hint=kp.ItemHitHint.IGNORE))

        self.set_suggestions(suggestions, kp.Match.ANY, kp.Sort.NONE)

    def on_execute(self, item, action):
        if not item:
            return

        kpu.shell_execute(self.MSTSC, args=f'/v:{item.target()}', working_dir='', verb='',
            try_runas=False, detect_nongui=False, api_flags=None, terminal_cmd=None, show=-1)
