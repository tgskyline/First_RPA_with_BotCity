from credencial import senha
"""
WARNING:

Please make sure you install the bot with `pip install -e .` in order to get all the dependencies
on your Python environment.

Also, if you are using PyCharm or another IDE, make sure that you use the SAME Python interpreter
as your IDE.

If you get an error like:
```
ModuleNotFoundError: No module named 'botcity'
```

This means that you are likely using a different Python interpreter than the one used to install the bot.
To fix this, you can either:
- Use the same interpreter as your IDE and install your bot with `pip install -e .`
- Use the same interpreter as the one used to install the bot (`pip install -e .`)

Please refer to the documentation for more information at https://documentation.botcity.dev/
"""

from botcity.core import DesktopBot
# Uncomment the line below for integrations with BotMaestro
# Using the Maestro SDK
# from botcity.maestro import *


class Bot(DesktopBot):
    def action(self, execution=None):

        # Login no Steam
        self.execute(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Steam\Steam.lnk')
        if not self.find( "FLD_Senha", matching=0.97, waiting_time=20000):
            self.not_found("FLD_Senha")
        self.click_relative(146, 42)
        self.paste(senha)
        self.enter()
        print('\n>>> Inserido Senha e clique em Login!\n')
        
        # Valida Login
        self.wait(5000)
        if not self.find( "TXT_UsuarioLogado", matching=0.97, waiting_time=30000):
            self.not_found("TXT_UsuarioLogado")
        print('>>> Login feito com Sucesso!\n')
        
        # Desloga do Steam
        self.wait(5000)
        if not self.find( "BTN_Account", matching=0.97, waiting_time=10000):
            self.not_found("BTN_Account")
        self.click()
        print('>>> Carregamento Realizado!\n')
        self.wait(5000)
        if not self.find( "BTN_CloseSession", matching=0.97, waiting_time=10000):
            self.not_found("BTN_CloseSession")
        self.click()
        self.wait(5000)
        if not self.find( "BTN_ClickEndSession", matching=0.97, waiting_time=10000):
            self.not_found("BTN_ClickEndSession")
        self.click()
        print('>>> Finalizado sessao com Sucesso!\n')

         
    def not_found(self, label): 
        print(f"Element not found: {label}")

if __name__ == '__main__':
    Bot.main()



