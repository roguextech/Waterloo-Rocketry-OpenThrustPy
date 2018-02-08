from __future__ import unicode_literals
import matplotlib
import webbrowser
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtWidgets

import cfgreader

# =============================================================================
# Classes
# =============================================================================

class MplCanvas(FigureCanvas):
    
    def __init__(self, parent=None, width=5, height=3, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.initialFig=self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass

class DynamicMplCanvas(MplCanvas):
    
    def __init__(self, ModelInstance, *args, **kwargs):
        self.ModelInstance = ModelInstance
        MplCanvas.__init__(self, *args, **kwargs)
        self.graph = "thrust"
        
    def setGraph(self, graph):
        self.graph = graph.lower()

    def compute_initial_figure(self):
        self.line, =self.axes.plot([], [],color='red',label='thrust')
        self.axes.set_xlim(0, 20)
        self.axes.set_ylim(0, +2000)
        self.axes.set_xlabel('Time (s)')
        self.axes.set_ylabel('Thrust (N)')
        legend = self.axes.legend(loc='best', shadow=False, fontsize='medium')
        legend.get_frame().set_alpha(0.5)

    def update_figure(self):
        a = self.ModelInstance.grabArrays()
        x = a["Time Array"]
        if self.graph == "thrust":
            y = a["Thrust Array"]
        elif self.graph == "tank temperature":
            y = a["Tank Temperature Array"]
        elif self.graph == "injector mass flow":
            y = a["Injector Mass Flow Array"]
        elif self.graph == "chamber pressure":
            y = a["Chamber Pressure Graph"]
        self.line.set_ydata(y)
        self.line.set_xdata(x)
        #self.axes.plot(x, y, 'r')
        self.draw()

# =============================================================================
# GUI Functions
# =============================================================================

def showWindow(windowWidget):
    windowWidget.show()
    
def settingsGrab(window):
    # Grabs the settings data in the variables window and returns it as cfg
    cfg = {
       'ox_tank_vol_L':     str(window.SpinBoxOxTank.value()), 
       'noz_thr_area_cm2':  str(window.SpinBoxThroatA.value()), 
       'noz_ext_area_cm2':  str(window.SpinBoxExitA.value()), 
       'ox_fuel_ratio':     str(window.SpinBoxOxFuel.value()), 
       'ramp_up_s':         str(window.SpinBoxRampUp.value()), 
       'ramp_down_s':       str(window.SpinBoxRampDown.value()), 
       'time_step_s':       str(window.SpinBoxTimeStep.value()), 
       'conv_weight':       str(window.SpinBoxConverge.value()), 
       'flow_model':        str(window.checkBoxFlowModel.isChecked()), 
       'integ_type':        str(window.checkBoxIntType.isChecked()), 
       'calc_thrust_coef':  str(window.checkBoxCalcCf.isChecked()), 
       'C12':               str(window.SpinBoxC12.value()),
       'inj_area_cm2':      str(window.SpinBoxInjA.value()),
       'vapor_factor':      str(window.SpinBoxVaporFactor.value())
       }
    return cfg

def settingsSet(window, cfg):
    # Sets the settings data in the variables window based off of cfg
    window.SpinBoxOxTank.setValue           (float(cfg['ox_tank_vol_L']))
    window.SpinBoxThroatA.setValue         (float(cfg['noz_thr_area_cm2']))
    window.SpinBoxExitA.setValue            (float(cfg['noz_ext_area_cm2']))
    window.SpinBoxOxFuel.setValue           (float(cfg['ox_fuel_ratio']))
    window.SpinBoxRampUp.setValue           (float(cfg['ramp_up_s']))
    window.SpinBoxRampDown.setValue         (float(cfg['ramp_down_s']))
    window.SpinBoxTimeStep.setValue         (float(cfg['time_step_s']))
    window.SpinBoxConverge.setValue         (float(cfg['conv_weight']))
    window.checkBoxFlowModel.setCheckState  (bool(cfg['flow_model']))
    window.checkBoxIntType.setCheckState    (bool(cfg['integ_type']))
    window.checkBoxCalcCf.setCheckState    (bool(cfg['calc_thrust_coef']))
    window.SpinBoxC12.setValue              (float(cfg['C12']))
    window.SpinBoxInjA.setValue          (float(cfg['inj_area_cm2']))
    window.SpinBoxVaporFactor.setValue      (float(cfg['vapor_factor']))
    
def settingsSave(Parser, settingsPath, window):
    # Saves settings data from GUI to file
    cfgreader.writeSettingsToFile(Parser, settingsPath, settingsGrab(window))

def openFileNameDialog(window):    
    options = QtWidgets.QFileDialog.Options()
    options |= QtWidgets.QFileDialog.DontUseNativeDialog
    fileName, _ = QtWidgets.QFileDialog.getOpenFileName(window,"File Picker", "","All Files (*);;Python Files (*.py)", options=options)
    if fileName:
        print(fileName)

def saveFileDialog(window):    
    options = QtWidgets.QFileDialog.Options()
    options |= QtWidgets.QFileDialog.DontUseNativeDialog
    fileName, _ = QtWidgets.QFileDialog.getSaveFileName(window,"File Picker","","All Files (*);;Text Files (*.txt)", options=options)
    if fileName:
        print(fileName)

def grabSetSettings(VariablesWindowUI):
    Parser = cfgreader.configparser.ConfigParser()
    try: 
        Parser.read(cfgreader.SETTINGS_PATH)
        settingsSet(VariablesWindowUI, cfgreader.readSettingsFromFile(Parser,cfgreader.SETTINGS_PATH))
    except:
        print("Settings values inputted wrong, using default settings...")
        cfgreader.createNewSettingsFile(cfgreader.SETTINGS_PATH)
        Parser.read(cfgreader.SETTINGS_PATH)
        settingsSet(VariablesWindowUI, cfgreader.readSettingsFromFile(Parser, cfgreader.SETTINGS_PATH))

def openGithub():
    webbrowser.open("https://github.com/waterloo-rocketry/OpenThrustPy")
    
def openTeamSite():
    webbrowser.open("http://waterloorocketry.com")
    
def printToGui(text, textBrowser):
    textBrowser.append(str(text))


# =============================================================================
# Button Functions
# =============================================================================


def setVariablesButtonClicked(WindowWidget, WindowUI):
    showWindow(WindowWidget)
    grabSetSettings(WindowUI)
    
def variablesWindowSaveButtonClicked(WindowUI):
    Parser = cfgreader.configparser.ConfigParser()
    settingsSave(Parser, cfgreader.SETTINGS_PATH, WindowUI)

def loadDatabasesButtonClicked(WindowWidget,WindowUI):
    showWindow(WindowWidget)

def startButtonClicked(WindowWidget, WindowUI, ModelInstance):
    if ModelInstance.running == False:
        ModelInstance.running = True
        WindowUI.statusbar.showMessage("Running...")
        WindowUI.startButton.setDisabled(True)
        WindowUI.cancelButton.setEnabled(True)
        ModelInstance.runModel()
        WindowUI.resetButton.setEnabled(True)
        WindowUI.cancelButton.setDisabled(True)
        ModelInstance.running = False
        WindowUI.statusbar.showMessage("Idle")
        
def cancelButtonClicked(WindowWidget, WindowUI, ModelInstance):
    if ModelInstance.running == True:
        ModelInstance.cancel = True
    
def resetButtonClicked(WindowWidget, WindowUI, ModelInstance):
    ModelInstance.reset()
    WindowUI.resetButton.setDisabled(True)
    WindowUI.startButton.setEnabled(True)
    WindowUI.cancelButton.setDisabled(True)
    