import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Variables de entrada.
visualizaciones = ctrl.Antecedent(np.arange(0, 100000001, 1000), 'Visualizaciones (millones)')
tiempo_estreno = ctrl.Antecedent(np.arange(0, 12, 1), 'Tiempo de Estreno (meses)')

# Variable de salida.
probabilidad_exito = ctrl.Consequent(np.arange(0, 101, 1), 'Probabilidad de Éxito')

# Funciones de membresía para las visualizaciones
visualizaciones['muy_baja'] = fuzz.trimf(visualizaciones.universe, [0, 0, 1000000])
visualizaciones['baja'] = fuzz.trimf(visualizaciones.universe, [900000, 3000000, 5100000])
visualizaciones['media'] = fuzz.trimf(visualizaciones.universe, [5000000, 30000000, 55000000])
visualizaciones['alta'] = fuzz.trimf(visualizaciones.universe, [25000000, 100000000, 100000000])

# Funciones de membresía para el tiempo de estreno.
tiempo_estreno['muy_corto'] = fuzz.trimf(tiempo_estreno.universe, [0, 0, 2])
tiempo_estreno['corto'] = fuzz.trimf(tiempo_estreno.universe, [1, 3, 5])
tiempo_estreno['medio'] = fuzz.trimf(tiempo_estreno.universe, [4, 6, 8])
tiempo_estreno['largo'] = fuzz.trimf(tiempo_estreno.universe, [7, 12, 12])

probabilidad_exito['muy_baja'] = fuzz.trimf(probabilidad_exito.universe, [0, 0, 20])
probabilidad_exito['baja'] = fuzz.trimf(probabilidad_exito.universe, [10, 30, 50])
probabilidad_exito['media'] = fuzz.trimf(probabilidad_exito.universe, [40, 60, 80])
probabilidad_exito['alta'] = fuzz.trimf(probabilidad_exito.universe, [70, 80, 90])
probabilidad_exito['muy_alta'] = fuzz.trimf(probabilidad_exito.universe, [80, 100, 100])

# Reglas difusas.
rule1 = ctrl.Rule(visualizaciones['muy_baja'] & tiempo_estreno['muy_corto'], probabilidad_exito['baja'])
rule2 = ctrl.Rule(visualizaciones['muy_baja'] & tiempo_estreno['corto'], probabilidad_exito['baja'])
rule3 = ctrl.Rule(visualizaciones['muy_baja'] & tiempo_estreno['medio'], probabilidad_exito['muy_baja'])
rule4 = ctrl.Rule(visualizaciones['muy_baja'] & tiempo_estreno['largo'], probabilidad_exito['muy_baja'])

rule5 = ctrl.Rule(visualizaciones['baja'] & tiempo_estreno['muy_corto'], probabilidad_exito['alta'])
rule6 = ctrl.Rule(visualizaciones['baja'] & tiempo_estreno['corto'], probabilidad_exito['alta'])
rule7 = ctrl.Rule(visualizaciones['baja'] & tiempo_estreno['medio'], probabilidad_exito['alta'])
rule8 = ctrl.Rule(visualizaciones['baja'] & tiempo_estreno['largo'], probabilidad_exito['alta'])

rule9 = ctrl.Rule(visualizaciones['media'] & tiempo_estreno['muy_corto'], probabilidad_exito['muy_alta'])
rule10 = ctrl.Rule(visualizaciones['media'] & tiempo_estreno['corto'], probabilidad_exito['muy_alta'])
rule11 = ctrl.Rule(visualizaciones['media'] & tiempo_estreno['medio'], probabilidad_exito['muy_alta'])
rule12= ctrl.Rule(visualizaciones['media'] & tiempo_estreno['largo'], probabilidad_exito['muy_alta'])

rule13 = ctrl.Rule(visualizaciones['alta'] & tiempo_estreno['muy_corto'], probabilidad_exito['muy_alta'])
rule14 = ctrl.Rule(visualizaciones['alta'] & tiempo_estreno['corto'], probabilidad_exito['muy_alta'])
rule15 = ctrl.Rule(visualizaciones['alta'] & tiempo_estreno['medio'], probabilidad_exito['muy_alta'])
rule16 = ctrl.Rule(visualizaciones['alta'] & tiempo_estreno['largo'], probabilidad_exito['muy_alta'])

# Sistema de control.
sistema_control = ctrl.ControlSystem(
    [
    rule1,
    rule2, 
    rule3,
    rule4,
    rule5,
    rule6,
    rule7,
    rule8,
    rule9,
    rule10,
    rule11,
    rule12,
    rule13,
    rule14,
    rule15,
    rule16
    ]
    )

# Asocia el sistema de control con las variables de entrada y salida.
controlador = ctrl.ControlSystemSimulation(sistema_control)

# Evaluar el controlador con diferentes situaciones
controlador.input['Visualizaciones (millones)'] = 800000
controlador.input['Tiempo de Estreno (meses)'] = 1
controlador.compute()
print("Probabilidad de Exito_1:", controlador.output['Probabilidad de Éxito'])

controlador.input['Visualizaciones (millones)'] = 15000000
controlador.input['Tiempo de Estreno (meses)'] = 2
controlador.compute()
print("Probabilidad de Exito_2:", controlador.output['Probabilidad de Éxito'])

controlador.input['Visualizaciones (millones)'] = 90000000
controlador.input['Tiempo de Estreno (meses)'] = 6
controlador.compute()
print("Probabilidad de Exito_3:", controlador.output['Probabilidad de Éxito'])

# Visualización de las funciones de membresía.
visualizaciones.view()
tiempo_estreno.view()
probabilidad_exito.view()
plt.show()