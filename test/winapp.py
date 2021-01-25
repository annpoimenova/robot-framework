from pywinauto.application import Application
import pywinauto
import time
import warnings
warnings.simplefilter('ignore', category=UserWarning)
app = Application().start(cmd_line=u'"C:\Program Files (x86)\Poimenov\CommunalPayments\CommunalPayments.WPF.exe"')
main_dlg = app.Payments
main_dlg.wait('visible')
main_dlg = app.window(title="Communal Payments")
main_dlg.print_control_identifiers()
app.About.click()

