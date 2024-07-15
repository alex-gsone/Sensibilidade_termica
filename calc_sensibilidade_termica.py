# coding=UTF-8
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib.gridspec as gridspec
from scipy.optimize import curve_fit
import plot_thermal as pt

data = np.loadtxt("dados21_decayExponetial.dat")
Temperatura_data = data[:,0]
R_data = data[:,1]

class AjusteBoltzmann():
    def boltzmann(self, x, a, b, c):
        # Níveis termicamente acoplados use a distribuição de Boltzmann:
        return a * np.exp(-b / x) + c
    
    def deriv_boltzmann(self, x, a, b, c):
        return (a*b*np.exp(-b / x))/x**2

class AjusteExp():
    def ajuste_exp(self, x, a, b, c):
        # Níveis termicamente acoplados use a distribuição de Boltzmann:
        return a * np.exp(b * x) + c
    
    def deriv_ajuste_exp(self, x, a, b, c):
        return a*b*np.exp(b*x)
    
#class AjusteExp2():
    def ajuste_exp2(self, x, a, b, c):
        # Níveis termicamente acoplados use a distribuição de Boltzmann:
        return a*np.exp(-b*x) + c
    
    def deriv_ajuste_exp2(self, x, a, b, c):
        return -a*b*np.exp(-b*x)
    
def calc_s():
    while True:
        print('''
        --- Cálculo da Sensibilidade térmica relativa:

        [1] - Ajuste Exponencial (Níveis termicamente acoplados: a*e**(-b/x)+c)
        [2] - Ajuste Exponencial crescente (Níveis não-termicamente acoplados: a*np.exp(+b*x)+c)
        [3] - Ajuste Exponencial decrescente (Níveis não-termicamente acoplados: a*np.exp(-b*x)+c)
        [4] - Ajuste Polinomial 
        [5] - Sair
            ''', end = '')
        N = int(input('Escolha uma opção: '))
        
        if N == 1:
            # Encontre a aproximação
            popt, pcov = curve_fit( AjusteBoltzmann().boltzmann, Temperatura_data, R_data)
        
            # calcule f e sua derivada
            f = AjusteBoltzmann().boltzmann( Temperatura_data, *popt)
            df = AjusteBoltzmann().deriv_boltzmann( Temperatura_data, *popt)
        
            # Calcule a Sensibilidade térmica relativa
            S = ( abs(df) / f )*100  # S = (1/R)|dR/dT| Sensibilidade térmica relativa.
        
            # Plot os gráficos:
            pt.PlotTermal().ajuste_edados(Temperatura_data, R_data, f)
            pt.PlotTermal().sensibilidade_t_relativa(Temperatura_data, S)
            plt.show()
            break
        elif N == 2:
            # Encontre a aproximação
            popt, pcov = curve_fit( AjusteExp().ajuste_exp, Temperatura_data, R_data)
        
            # calcule f e sua derivada
            f = AjusteExp().ajuste_exp( Temperatura_data, *popt)
            df = AjusteExp().deriv_ajuste_exp( Temperatura_data, *popt)
        
            # Calcule a Sensibilidade térmica relativa
            S = ( abs(df) / f )*100  # S = (1/R)|dR/dT| Sensibilidade térmica relativa.
        
            # Plot os gráficos:
            pt.PlotTermal().ajuste_edados(Temperatura_data, R_data, f)
            pt.PlotTermal().sensibilidade_t_relativa(Temperatura_data, S)
            plt.show()
            break
        elif N == 3:
            # Encontre a aproximação
            popt, pcov = curve_fit( AjusteExp().ajuste_exp2, Temperatura_data, R_data)
        
            # calcule f e sua derivada
            f = AjusteExp().ajuste_exp2( Temperatura_data, *popt)
            df = AjusteExp().deriv_ajuste_exp2( Temperatura_data, *popt)
        
            # Calcule a Sensibilidade térmica relativa
            S = ( abs(df) / f )*100  # S = (1/R)|dR/dT| Sensibilidade térmica relativa.
        
            # Plot os gráficos:
            pt.PlotTermal().ajuste_edados(Temperatura_data, R_data, f)
            pt.PlotTermal().sensibilidade_t_relativa(Temperatura_data, S)
            plt.show()
            break
        elif N == 4:
            n = int(input('''
            Digite o grau do polinômio n = '''))
            
            # Encontre o polinômio por aproximação
            polinomio = np.polyfit(Temperatura_data, R_data, n)
            
            # Encontre a derivada do polinomio
            d_polinomio = np.polyder(polinomio, 1)
            
            # calcule o polinomio sua derivada nos valores de Temperatura:
            f = np.polyval(polinomio, Temperatura_data)
            df = np.polyval(d_polinomio, Temperatura_data)

            # Calcule a Sensibilidade térmica relativa
            S = ( abs(df) / f )*100  # S = (1/R)|dR/dT| Sensibilidade térmica relativa
            
            # Plot os gráficos:
            pt.PlotTermal().ajuste_edados(Temperatura_data, R_data, f)
            pt.PlotTermal().sensibilidade_t_relativa(Temperatura_data, S)
            plt.show()
            break
        
        elif N == 5:
            break           

if __name__ == '__main__':
    calc_s()


