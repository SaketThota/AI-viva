import random


def main():
    gene = input("Enter gene in binary representation : ")
    mut_prob = float(input("Enter mutation probability : "))

    gene = list(gene)
    mut_prob_vec = list()
    n = len(gene)

    for i in range(n):
        rand_prob = random.random()
        if(rand_prob >= mut_prob):
            mut_prob_vec.append(1)
        else:
            mut_prob_vec.append(0)

    new_gene = list()

    for i in range(n):
        if mut_prob_vec[i] == 1:
            if gene[i] == '1':
                new_gene.append('0')
            else:
                new_gene.append('1')
        else:
            new_gene.append(gene[i])

    print(''.join(gene))
    print(','.mut_prob_vec)
    print(''.join(new_gene))


main()
