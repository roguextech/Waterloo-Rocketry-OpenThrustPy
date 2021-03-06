import configparser

SETTINGS_PATH = "./settings.cfg"

def writeSettingsToFile(ParserObject, settingsPath, cfg):
    # Takes a dictionary of values and writes it to the settings file
    config = ParserObject
    readSettingsFromFile(config, settingsPath)
    
    config.set(
            "Rocket Dimensions",     
            "Oxidizer Tank Volume (L)",      
            cfg["ox_tank_vol_L"]
            )
    config.set(
            "Rocket Dimensions",     
            "Nozzle Throat Area (cm^2)",      
            cfg["noz_thr_area_cm2"]
            )
    config.set(
            "Rocket Dimensions",     
            "Nozzle Exit Area (cm^2)",        
            cfg["noz_ext_area_cm2"]
            )
    config.set(
            "Rocket Dimensions",
            "Injector Area (cm^2)",
            cfg["inj_area_cm2"]
            )
    config.set(
            "Rocket Properties",     
            "Average Oxidizer/Fuel Ratio",   
            cfg["ox_fuel_ratio"]
            )
    config.set(
            "Rocket Properties",     
            "Ramp Up Time (s)",              
            cfg["ramp_up_s"]
            )
    config.set(
            "Rocket Properties",     
            "Ramp Down Time (s)",
            cfg["ramp_down_s"]
            )
    config.set(
            "Simulation Settings",   
            "Time Step (s)",                 
            cfg["time_step_s"]
            )
    config.set(
            "Simulation Settings",   
            "Convergence Weighting",         
            cfg["conv_weight"]
            )
    config.set(
            "Simulation Settings",   
            "Flow Model",                    
            cfg["flow_model"]
            )
    config.set(
            "Simulation Settings",   
            "Addams Integration",             
            cfg["integ_type"]
            )
    config.set(
            "Simulation Settings",   
            "Calculate Thrust Coefficient",  
            cfg["calc_thrust_coef"]
            )
    config.set(
            "Simulation Settings",   
            "C12",                           
            cfg["C12"]
            )
    config.set(
            "Simulation Settings",   
            "Vaporization Factor",                           
            cfg["vapor_factor"]
            )
    
    with open(SETTINGS_PATH, 'w') as configfile:
        config.write(configfile)
    
    return True

def readSettingsFromFile(ParserObject, settingsPath):
    # Takes the settings file and generates a dictionary
    config = ParserObject
    config.read(settingsPath)
    try:
        rDim = config["Rocket Dimensions"]
        rProp = config["Rocket Properties"]
        simSet = config["Simulation Settings"]
        cfg = {}
        cfg["ox_tank_vol_L"]        = rDim["Oxidizer Tank Volume (L)"]
        cfg["noz_thr_area_cm2"]     = rDim["Nozzle Throat Area (cm^2)"]
        cfg["noz_ext_area_cm2"]     = rDim["Nozzle Exit Area (cm^2)"]
        cfg["inj_area_cm2"]         = rDim["Injector Area (cm^2)"]
        cfg["ox_fuel_ratio"]        = rProp["Average Oxidizer/Fuel Ratio"]
        cfg["ramp_up_s"]            = rProp["Ramp Up Time (s)"]
        cfg["ramp_down_s"]          = rProp["Ramp Down Time (s)"]
        cfg["time_step_s"]          = simSet["Time Step (s)"]
        cfg["conv_weight"]          = simSet["Convergence Weighting"]
        cfg["flow_model"]           = simSet["Flow Model"]
        cfg["integ_type"]           = simSet["Addams Integration"]
        cfg["calc_thrust_coef"]     = simSet["Calculate Thrust Coefficient"]
        cfg["C12"]                  = simSet["C12"]
        cfg["vapor_factor"]         = simSet["Vaporization Factor"]
        return cfg
    except:
        print("Improperly formatted settings file, creating new one...")
        createNewSettingsFile(settingsPath)
        config.read(settingsPath)
        return readSettingsFromFile(config, settingsPath)
    

def createNewSettingsFile(settingsPath):
    config = configparser.ConfigParser()
    config["Rocket Dimensions"] = {}
    config["Rocket Properties"] = {}
    config["Simulation Settings"] = {}
    config["Rocket Dimensions"]["Oxidizer Tank Volume (L)"]         = "6.9"
    config["Rocket Dimensions"]["Nozzle Throat Area (cm^2)"]        = "3.82646"
    config["Rocket Dimensions"]["Nozzle Exit Area (cm^2)"]          = "18.1001"
    config["Rocket Dimensions"]["Injector Area (cm^2)"]             = "0.2826"

    config["Rocket Properties"]["Average Oxidizer/Fuel Ratio"]      = "2.1"
    config["Rocket Properties"]["Ramp Up Time (s)"]                 = "4"
    config["Rocket Properties"]["Ramp Down Time (s)"]               = "6"

    config["Simulation Settings"]["Time Step (s)"]                  = "0.05"
    config["Simulation Settings"]["Convergence Weighting"]          = "0.2"
    config["Simulation Settings"]["Flow Model"]                     = "2"
    config["Simulation Settings"]["Addams Integration"]             = "2"
    config["Simulation Settings"]["Calculate Thrust Coefficient"]   = "0"
    config["Simulation Settings"]["C12"]                            = "2.23"
    config["Simulation Settings"]["Vaporization Factor"]            = "0.005"

    with open(settingsPath, 'w') as configfile:
        config.write(configfile)
