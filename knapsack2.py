import random
import sys
import operator


class Knapsack(object):

    # initialize variables and lists
    def __init__(self):

        self.numofitems = 0
        self.maxofmax = []
        self.C = 0
        self.weights = []
        self.profits = []
        self.opt = []
        self.parents = []
        self.newparents = []
        self.bests = []
        self.best_p = []
        self.iterated = 1
        self.population = 0
        self.index1 = 1
        self.index2 = 1
        self.totaloftoalofselection = 0
        self.countselection = 0
        self.sumofselectweight = 0
        self.sumofselectprofits = 0
        # increase max recursion for long stack
        iMaxStackSize = 15000
        sys.setrecursionlimit(iMaxStackSize)

    def summation(self, sum_w, sum_p):

        sumlistp = []
        sumlistw = []
        for i in range(0, len(self.parents)):
            sumlistp.append(sum_p)
            sumlistw.append(sum_w)
        sumweight = max(sumlistw)
        sumprofit = max(sumlistp)
        return sumweight, sumprofit

    # create the initial population
    def initialize(self):

        for i in range(self.population):
            parent = []
            for k in range(0, self.numofitems):
                k = random.randint(0, 1)
                parent.append(k)
            self.parents.append(parent)

    # set the details of this problem
    def properties(self, weights, profits, opt, C, population, numofitems):
        self.numofitems = numofitems
        self.weights = weights
        self.profits = profits
        self.opt = opt
        self.C = C
        self.population = population
        self.initialize()

    # calculate the fitness function of each list (sack)
    def fitness(self, item):

        sum_w = 0
        sum_p = 0

        sumv=0

        sumw=0


        # get weights and profits
        for index, i in enumerate(item):  # return index and values
            if i == 0:
                continue
            else:
                sum_w += self.weights[index]
                sum_p += self.profits[index]
            print(f"the sum_weights and values are {sum_w}, {sum_p}")
            print("==================================================")
            sumw, sumv = self.summation(sum_w, sum_p)
        print("the maximum value of list after summmation is ", sumv)
        self.maxofmax.append(sumv)
        print("the  maximum overall the generation is :",max(self.maxofmax))


        # if greater than the optimal return -1 or the number otherwise
        if sum_w > self.C:
            return -1
        else:
            return sum_p


    # run generations of GA
    def evaluation(self):

        # loop through parents and calculate fitness
        best_pop = self.population // 2
        for i in range(len(self.parents)):
            parent = self.parents[i]
            print("the parent is :", parent)  # list
            ft = self.fitness(parent)
            self.bests.append((ft, parent))

        # sort the fitness list by fitness
        self.bests.sort(key=operator.itemgetter(0), reverse=True)
        self.best_p = self.bests[:best_pop]
        self.best_p = [x[1] for x in self.best_p]

    # mutate children after certain condition
    def mutation(self, characters):

        for i in range(len(characters)):

            k = random.uniform(0, 1)
            if k < 0.1 or k >0.001:
                # if random float number greater that 0.5 flip 0 with 1 and vice versa
                if characters[i] == 1:
                    characters[i] = 0
                else:
                    characters[i] = 1
        return characters

    # crossover two parents to produce two children by miixing them under random ration each time
    def crossover(self, ch1, ch2):

        threshold = random.randint(1, len(ch1) - 1)
        tmp1 = ch1[threshold:]
        tmp2 = ch2[threshold:]
        ch1 = ch1[:threshold]
        ch2 = ch2[:threshold]
        ch1.extend(tmp2)
        ch2.extend(tmp1)

        return ch1, ch2

    # run the GA algorithm
    def run(self):
        sumofselectweight = 0
        sumofselectprofits = 0
        sum=0
        # run the evaluation once
        self.evaluation()
        newparents = []
        # pop =4
        pop = len(self.best_p) - 1

        # create a list with unique random integers
        # get random values below pop=4 so 0,3,2,1
        # sample = random.sample(range(pop), pop)
        for i in range(0, pop):
            # select the random index of best children to randomize the process
            # i <3 ?

            if i < pop - 1:
                r1 = self.best_p[i]  # first parent
                r2 = self.best_p[i + 1]  # second parent
                nchild1, nchild2 = self.crossover(r1, r2)  # make cross over on them
                newparents.append(nchild1)  # append new children in newparent
                newparents.append(nchild2)
                self.countselection += 1
                print("new parent is {}".format(newparents))
                print("==============================================================")
            x = []
            z = []
            c = 1
            for k in range(0, len(newparents)):
                x = newparents[k]  # list of 1 new parent
                for j in range(0, len(x)):
                    if z == 0:
                        continue
                    z = x[
                        j]  # every element of list 1 0 1 1 0  # [[1, 0, 1, 1, 0], [1, 0, 1, 1, 1], [1, 0, 0, 1, 1], [1, 1, 1, 1, 0]
                    sumofselectweight += self.weights[j]
                    sumofselectprofits += self.profits[j]
                if sumofselectweight > self.C:
                    c = 0
                if c == 1:
                    print(f"the weights for selection is {k} :{sumofselectweight}")
                    print(f"the profits for selection is {k} :{sumofselectprofits}")




            # i==3
        else:
            r1 = self.best_p[i]
            r2 = self.best_p[0]
            nchild1, nchild2 = self.crossover(r1, r2)
            newparents.append(nchild1)
            newparents.append(nchild2)
            print(newparents)
            self.countselection += 1
            x1 = []
            z1 = []
            c2 = 1
            for k1 in range(0, len(newparents)):
                x1 = newparents[k1]  # list of 1 new parent
                for j2 in range(0, len(x1)):
                    if z1 == 0:
                        continue
                    z1 = x[ j2]  # every element of list 1 0 1 1 0  # [[1, 0, 1, 1, 0], [1, 0, 1, 1, 1], [1, 0, 0, 1, 1], [1, 1, 1, 1, 0]
                    sumofselectweight += self.weights[j2]
                    sumofselectprofits += self.profits[j2]
                    if sumofselectweight > self.C:
                        c2 = 0
                if c2 == 1:
                    print(f"the weights for selection is {k1} :{sumofselectweight}")
                    print(f"the profits for selection is {k1} :{sumofselectprofits}")

            print("=============================================================")


        print("the number of selection is :", self.countselection)

        # mutate the new children and potential parents to ensure global optima found
        for i in range(len(newparents)):
            newparents[i] = self.mutation(newparents[i])

        if self.opt in newparents:
            # iterated is a counter to show
            print("optimal found in {} generations".format(self.iterated))
            print(self.opt)
            for i in range (0,self.numofitems):
              if self.opt[i]!= 0:
                  sum+=self.profits[i]
            print("the total value for optimal is :", sum)

        else:
            self.iterated += 1
            print("recreate generations for {} time".format(self.iterated))
            self.parents = newparents
            self.bests = []
            self.best_p = []
            self.run()


# properties for this particular problem

n = int(input('enter the number of test cases :'))

for index in range(0, n):
    weights = []
    profits = []
    optimal = []
    population = int(input('enter the size of knapsack (population):'))
    numofitem = int(input('enter the number of items:'))
    for i in range(0, numofitem):
        x, y = map(int, input().split())
        weights.append(x)
        profits.append(y)

    # number of elements as input
    n = int(input("Enter number of elements for optimal list  : "))

    # iterating till the range
    for i in range(0, n):
        element = int(input("enter optimal inputs but notise list of optimal the same as weights and profits "))

        optimal.append(element)  # adding the element

    print("the optimal list is ", optimal)

    print("==================================================")
    print("the test case index is :", index)
    print("==================================================")
    print("the weights is", weights)
    print("the profits is ", profits)
    print("==================================================")
    Capacity = 26
    k = Knapsack()
    k.properties(weights, profits, optimal, Capacity, population, numofitem)
    k.run()
