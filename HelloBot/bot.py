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
        # Uncomment to silence Maestro errors when disconnected
        # if self.maestro:
        #     self.maestro.RAISE_NOT_CONNECTED = False

        # Fetch the Activity ID from the task:
        # task = self.maestro.get_task(execution.task_id)
        # activity_id = task.activity_id

        # Opens the BotCity website.
        # self.browse("http://www.botcity.dev")

        # Uncomment to mark this task as finished on BotMaestro
        # self.maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )
        
        # Login no Steam
        self.execute(r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Steam\Steam.lnk')
        if not self.find( "FLD_Senha", matching=0.97, waiting_time=20000):
            self.not_found("FLD_Senha")
        self.click_relative(146, 42)
        self.paste(senha)
        self.enter()
        print('\n>>> Inserido Senha e clique em Login com Sucesso!\n')
        
        # # Aguarda carregamento 
        if not self.find( "IMG_SteamLogin", matching=0.97, waiting_time=20000):
            self.not_found("IMG_SteamLogin")
        print('Carregamento feito com sucesso!')
        
        # # Fecha o modal
        # if not self.find( "BTN_CloseModal", matching=0.97, waiting_time=20000):
        #     self.not_found("BTN_CloseModal")
        # self.click()
        # print('Modal fechado com sucesso!')
        
        # Desloga do Steam
        if not self.find( "BTN_Account", matching=0.97, waiting_time=30000):
            self.not_found("BTN_Account")
        self.click()
        print('>>> Carregamento realizado!\n')
        if not self.find( "BTN_CloseSession", matching=0.97, waiting_time=10000):
            self.not_found("BTN_CloseSession")
        self.click()
        if not self.find( "BTN_ClickEndSession", matching=0.97, waiting_time=10000):
            self.not_found("BTN_ClickEndSession")
        self.click()
        print('>>> Finalizado sessao com Sucesso!\n')
        
        # Aguarda ícone da Steam ser visivel novamente
        # self.wait(20000)
        # if not self.find( "BTN_IconSteam", matching=0.97, waiting_time=10000):
        #     self.not_found("BTN_IconSteam")
        # self.click()
        # print('>>> Steam deve abrir novamente?\n')
        
        # Abre tela de Login e clica em fechar
        # self.wait(50000)
        # if not self.find( "BTN_CloseLogin", matching=0.97, waiting_time=10000):
        #     self.not_found("BTN_CloseLogin")
        # self.click()
        # print('>>> Steam é fechado\n')
         
    def not_found(self, label): 
        print(f"Element not found: {label}")

if __name__ == '__main__':
    Bot.main()



