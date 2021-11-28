#Name: Shahida Hoque
#Email: shahida.hoque03@myhunter.cuny.edu
#Date: March 26, 2020

message1 = input("Enter name of input file: ")
message2 = input("Enter name of output file: ")

import pandas as pd
import matplotlib.pyplot as plt

homeless = pd.read_csv(message1)
homeless["Fraction Single"] = homeless["Total Single Adults in Shelter"]/homeless["Total Individuals in Shelter"]
homeless.plot(x = "Date of Census", y = "Fraction Single")

plt.show()
fig = plt.gcf()
fig.savefig(message2)
