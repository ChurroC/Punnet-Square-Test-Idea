from operator import le
from tkinter.tix import Tree
from tracemalloc import DomainFilter

from cv2 import randShuffle
from more_itertools import consecutive_groups


def type_of_cross_input():
    message="What type of punnet square do you wish to solve? Write the number of the the punnet square type.\n"
    message+="1.Complete Dominance(The dominant allele completely makss the trait of the recessive allele. Use when there is only dominant recessive alleles.)\n"
    message+="2.Incomplete Dominance(The heterozygous condition results in a phenotype that is a blend between the dominant and recessive alles. Three possible phenotypes exist.)\n"
    message+="3.Codominanace(The heterozygous condition results in a phenotype that has both the dominant and recessive alles. Three possible phenotypes exist.)\n"
    return input(message)

def grid(row, col, length_of_each_couloumn, message_array):
    message=""
    for i in range((row*col)+1):
        if i>len(message_array):
            if length_of_each_couloumn%2==1:
                message_array.append(" ")
            if length_of_each_couloumn%2==0:
                message_array.append("")

    col_drawing="+"
    for i in range(len(message_array)):
        message_array[i]=str(message_array[i])
    for i in range(length_of_each_couloumn):
        col_drawing+="-"

    for i in range(len(message_array)):
        adjust=int((length_of_each_couloumn-len(message_array[i]))/2)
        message_array[i]=message_array[i].ljust(adjust+len(message_array[i]))
        message_array[i]=message_array[i].rjust(adjust+len(message_array[i]))

    for i in range(row):
        message+='\n' + col_drawing*col + '+\n'
        for j in range(col):
            message+='|'+message_array[j+i*col]
        message+='|'
    message+='\n' + col_drawing*col + '+\n'
    return message

print("Hi, this is Charan's Punnet Square Calculator")

type_of_cross=type_of_cross_input()
while type_of_cross not in ["1","2","3","4","5"]:
    print(type_of_cross)
    print("Your answer was not 1,2,3,4, or 5.")
    type_of_cross=input("Answer again but use 1,2,3,4, or 5.\n")

message=""
if type_of_cross=="1":
    parent_genotype_1=input("Write the genotype of parent 1.\n")
    parent_genotype_2=input("Write the genotype of parent 2.\n")

    if len(parent_genotype_1)!=2 or len(parent_genotype_2)!=2:
        print("Parent genotypes can only have 2 alleles per parent in comp2lete dominance.")
        parent_genotype_1=input("Write the genotype of parent 1.\n")
        parent_genotype_2=input("Write the genotype of parent 2.\n")
    
    message+=f"For complete dominance if you have a parents with {parent_genotype_1} and {parent_genotype_2} you get:\n"
    genotypes=[]

    for i in parent_genotype_1:
        for j in parent_genotype_2:
            genotypes.append(i+j)
    print(grid(len(parent_genotype_1[:]),len(parent_genotype_2[:]),4,(genotypes[:])))

    message+="Genotypes:"
    for i in range(len(genotypes)):message+=f" {genotypes[i]}"
    
    message+="\nPhenotypes:"

    dominant_or_not=False
    for i in genotypes:
        for j in list(i):
            if j.isupper():
                dominant_or_not=True
                break
            dominant_or_not=False
        if dominant_or_not:
            message+=" Dominant"
        else:
            message+=" Reccesive"
        dominant_or_not=False
elif type_of_cross=="2":
    parent_genotype_1=input("Write the genotype of parent 1.\n")
    parent_genotype_2=input("Write the genotype of parent 2.\n")

    if len(parent_genotype_1)!=2 or len(parent_genotype_2)!=2:
        print("Parent genotypes can only have 2 alleles per parent in complete dominance.")
        parent_genotype_1=input("Write the genotype of parent 1.\n")
        parent_genotype_2=input("Write the genotype of parent 2.\n")
    
    message+=f"For incomplete dominance if you have a parents with {parent_genotype_1} and {parent_genotype_2} you get:\n"
    genotypes=[]

    for i in parent_genotype_1:
        for j in parent_genotype_2:
            genotypes.append(i+j)
    print(grid(len(parent_genotype_1[:]),len(parent_genotype_2[:]),4,(genotypes[:])))

    message+="Genotypes:"
    for i in range(len(genotypes)):message+=f" {genotypes[i]}"
    
    message+="\nPhenotypes:"

    dominant_or_not=0
    for i in genotypes:
        for j in list(i):
            if j.isupper():
                dominant_or_not+=1
            else:
                dominant_or_not+=0
        print(dominant_or_not)
        print("dominant_or_not")
        if dominant_or_not==2:
            message+=" Dominant"
        elif dominant_or_not==1:
            message+=" Blend"
        elif dominant_or_not==0:
            message+=" Reccesive"
        dominant_or_not=0
elif type_of_cross=="3":
    parent_genotype_1=input("Write the genotype of parent 1.\n")
    parent_genotype_2=input("Write the genotype of parent 2.\n")

    if len(parent_genotype_1)!=2 or len(parent_genotype_2)!=2:
        print("Parent genotypes can only have 2 alleles per parent in complete dominance.")
        parent_genotype_1=input("Write the genotype of parent 1.\n")
        parent_genotype_2=input("Write the genotype of parent 2.\n")
    
    message+=f"For codominanace if you have a parents with {parent_genotype_1} and {parent_genotype_2} you get:\n"
    genotypes=[]

    for i in parent_genotype_1:
        for j in parent_genotype_2:
            genotypes.append(i+j)
    print(grid(len(parent_genotype_1[:]),len(parent_genotype_2[:2]),4,(genotypes[:])))

    message+="Genotypes:"
    for i in range(len(genotypes)):message+=f" {genotypes[i]}"
    
    message+="\nPhenotypes:"

    dominant_or_not=0
    for i in genotypes:
        for j in list(i):
            if j.isupper():
                dominant_or_not+=1
            else:
                dominant_or_not+=0
        print(dominant_or_not)
        print("dominant_or_not")
        if dominant_or_not==2:
            message+=" Dominant"
        elif dominant_or_not==1:
            message+=" Both"
        elif dominant_or_not==0:
            message+=" Reccesive"
        dominant_or_not=0



print(message)
input("Press enter to exit :)")