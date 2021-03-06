'''   Copyright 2021 MOHAMMED YAHYA ANSARI

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''
import pandas as pd
print("\n \t\t\t TDMA Solver\n")
print("\n\tRefer the nTDMA.pdf for the general form of TriDiagonal Matrix Algorithm with n unknowns\n")
n = int(input("\n\tEnter the number of unknowns (n):   "))

# create zeros list/array as per user input
D = [0]*n  # diagonal element
beta = [0]*n  # element to the left of diagonal
alpha = [0]*n  # element to the right of diagonal
c = [0]*n  # value of constant element
A = [0]*n  # intermediate values
C = [0]*n
X = [0]*n  # final answer array

# input element values from user
for i in range(0, n):
    D[i] = float(input("\n\tEnter Diagonal {} value D{}:   ".format((i+1), (i+1))))
print("\n")
for i in range(0, n-1):
    alpha[i] = float(input("\n\tEnter value of \N{GREEK SMALL LETTER ALPHA}{}:   " .format(i+1)))
print("\n")
for i in range(1, n):
    beta[i] = float(input("\n\tEnter value of \N{GREEK SMALL LETTER BETA}{}:   ".format(i+1)))
print("\n")

# input value of constant from the user
for i in range(0, n):
    c[i] = float(input("\n\tEnter value of Constant {}:    ".format(i+1)))
print("\n")
beta[0] = 0  # since there is no element to the left of the diagonal so we assign 0 to the first value of beta
alpha[n-1] = 0  # for the last diagonal element there is no element to the right so we assign 0 to the last value of alpha
# also note that the above value is already 0 in program but to show the complete algorithm, above two lines are written

# solution, forward substitution of intermediate terms
for i in range(0, n):
    A[i] = alpha[i]/(D[i] - beta[i]*A[i-1])
    C[i] = (beta[i]*C[i-1] + c[i])/(D[i] - beta[i]*A[i-1])

# Calculation of final values to get the solution

X[n-1] = C[n-1]  # equating the last X term for backward substitution
j = n-2
while j >= 0:
    X[j] = A[j] * X[j+1] + C[j]
    j = j-1

#Create data for Pandas DataFrame
OUTPUT = list(zip(beta , D , alpha , c , A , C , X))
#create Pandas DataFrame
result = pd.DataFrame(data = OUTPUT, columns = ["\N{GREEK SMALL LETTER BETA}","Diagonal (D)","\N{GREEK SMALL LETTER ALPHA}","Constants","A","C'","X" ])
#Change index to 1,2,3,.....
result.index = result.index + 1
print(result)

#export result ot excel sheet
export = ""
while export != "q":
    print("\n\n\t[ y ] Enter y to export the table to nTDMA.xlsx\n\n\t[ q ] Enter q to exit without exporting\n\n")
    export = input("Enter your choice :\t")

    if (export == "y"):
        result.insert(0, 'Sr.No.', range(1, 1 + len(result))) #add serial no  column at the start of the DataFrame
        result.to_excel('nTDMA.xlsx', sheet_name = 'Output', index = False) #.to_excel to export excel file
        print("\n\n*************** Export to nTDMA.xlsx complete. ***************\n\n")
        break

    elif (export == "q"):
        print("\n\n***** Result not exported to excel. *****\n\n")
        break
    
    else : print("\n\t\tInvalid Choice, Try again!")

# to hold output screen
input()
