class Patient:
    #all instances of Patient class is kept inside Patients
    Patients = []
    #All mutated patients are kept inside MutatedPatients and they are filled inside main_func()
    MutatedPatients = []
    #BigG is short for biggest generation and finds the youngest person with the longest family tree
    BigG = 1
    '''
    Father and Mother are ids
    '''
    def __init__(self, Fullname, Father, Mother, GenoType, PhenoType, id, Male=False):
        self.Fullname = Fullname
        self.Father = Father
        self.Mother = Mother
        self.GenoType = GenoType
        self.PhenoType = PhenoType
        self.Children = []
        self.id = id
        self.Male = Male
        self.Generation = None
        if Mother != None and Father != None:
            self.Mother.Children.append(self)
            self.Father.Children.append(self)
        Patient.Patients.append(self)

    def gene_merger(self, new_Genes):
        '''
        Merges self's possible genotypes with new_Genes
        input: self.GenoType = ["Ao", "AA"]
               new_Genes     =  [['RR'], ['Rr']]

        result: self.GenoType = ['AARR', 'AARr', 'AoRR', 'AoRr']
        '''
        if self.GenoType == None:
            self.GenoType = new_Genes
        else:
            pos = []
            for i in self.GenoType:
                newString = ""
                for a in i:
                    newString += a
                for b in new_Genes:
                    new1 = ""
                    for c in b:
                        new1 += c
                    pos.append(newString+new1)
            self.GenoType = pos

    @staticmethod
    def Crosser(Genos, toMerge, gonosomal=False, Male=False):
        '''
        Crosses genes of 2 people
        input: Genos = []
                toMerge = [[['A', 'o'], ['A', 'o'], ['A', 'o'],  ['A', 'o']],
                            [['o', 'o'], ['o', 'o']]]
                index 0 = Mothers genes for gene type
                index 1 = Fathers genes for gene type
                gonomosal for gene type and male for sex

        output: newGeno = [['Ao', 16], ['oo', 16]]
                without the Counter method newGeno = ['Ao', 'oo', 'Ao', 'oo', 'Ao', 'oo', 'Ao', 'oo', 'Ao',
                                                'oo', 'Ao', 'oo', 'Ao', 'oo', 'Ao', 'oo', 'Ao', 'oo', 'Ao', 'oo',
                                                'Ao', 'oo', 'Ao', 'oo', 'Ao', 'oo', 'Ao', 'oo', 'Ao', 'oo', 'Ao', 'oo']

                After Counter: newGeno = [['Ao', 16], ['oo', 16]]
                first index ["Ao", 16] shows the gene and the second index shows how many times
                that combination of genes were created

                in the second run the second indexs sum

                Second run: newGeno = [['Aorr', 512], ['oorr', 512]]
        '''
        newGeno = []
        a = toMerge

        if len(Genos) == 0 and gonosomal == False:
            for i in a[0]:
                for b in a[1]:
                    newGeno.append(i[0] + b[0])
                    newGeno.append(i[1] + b[0])
                    newGeno.append(i[0] + b[1])
                    newGeno.append(i[1] + b[1])
            newGeno = Counter(newGeno, True)
            return newGeno

        elif gonosomal == False:
            for i in Genos:
                for b in a[0]:

                    for c in a[1]:
                        newGeno.append([i[0] + b[0] + c[0], i[1]])
                        newGeno.append([i[0] + b[1] + c[0], i[1]])
                        newGeno.append([i[0] + b[0] + c[1], i[1]])
                        newGeno.append([i[0] + b[1] + c[1], i[1]])

            newGeno = Counter(newGeno, mode=True)

            return newGeno
        elif gonosomal and len(Genos) == 0:
            if Male:
                if len(a[0]) == 0:
                    for b in a[1]:
                        newGeno.append(b[0])
                    return newGeno
                else:
                    for b in a[0]:
                        newGeno.append(b[0])
                        newGeno.append(b[1])
                    return newGeno
            else:
                for b in a[0]:
                    for c in a[1]:
                        newGeno.append(b[0] + c[0])
                        newGeno.append(b[1] + c[0])

                newGeno = Counter(newGeno, True)
                return newGeno

        elif gonosomal and len(Genos) != 0:
            if Male:
                if len(a[0]) == 0:
                    for i in Genos:
                        for b in a[1]:
                            newGeno.append([i[0] + b[0], i[1]])
                else:
                    for i in Genos:
                        for b in a[0]:
                            for c in a[1]:
                                newGeno.append([i[0] + b[0], i[1]])
                                newGeno.append([i[0] + b[1], i[1]])
                                newGeno.append([i[0] + c[0], i[1]])
            else:
                if len(a[0]) != 0:
                    for i in Genos:
                        for b in a[0]:
                            for c in a[1]:
                                newGeno.append([i[0] + b[0] + c[0], i[1]])
                                newGeno.append([i[0] + b[1] + c[0], i[1]])
            newGeno = Counter(newGeno, mode=True)
            return newGeno


class Disease:
    '''
    Diseases keeps all the instances of Disease class
    '''
    Diseases = []


    def __init__(self, name, Phenotype):
        self.name = name
        self.Phenotype = Phenotype

        Disease.Diseases.append(self)

    def disease_posibility(self, GenoType, Male):
        '''
        Takes a Genotype as a string and returns True if
        person has the disease otherwise returns False

        Male is the sex of the Genotype owner

        Compares Genotype with self.Phenotype and finds the result
        '''
        for gene in Gene.Genes:
            dis = gene.gene_in_pheno(self.Phenotype)
            ph = gene.gene_in_genos([GenoType], Male)

            if len(ph) > 0:
                ph = gene.geno_to_pheno(ph[0])
            if len(dis) > 0:
                dis = gene.geno_to_pheno(dis)
            if len(ph) > 0 and len(dis) > 0:
                if ph != dis:
                    return False
            if gene.gonosomal == True and len(dis) != 0 and len(ph) == 0:
                return False
        return True


class Gene:
    #Genes keeps all the instances of Gene Class
    Genes = []
    '''
    Dominance is the dominance of the letters for example letters = ["A", "B", "o"] and dominance = [1,1,0]
    this means A:1 B:1 and o:0 so if the Genotype is "Ao" the Phenotype is "A"
    but if Genotype is AB then Phenotype is "AB"
    '''
    def __init__(self, name, dominance, letters, gonosomal=False):
        self.name = name
        self.dominance = dominance
        self.letters = letters
        self.gonosomal = gonosomal
        Gene.Genes.append(self)

    def geno_to_pheno(self, geno):
        '''
        Takes relevant genes

        if self.letters = ["A", "B", "o"]
            self.dominance = [1,1,0]
        input: geno = ["A", "o"]

        output: geno = "A"
        '''
        if len(geno) > 1:
            numerical = ""
            for i in range(len(geno)):
                for b in range(len(self.letters)):
                    if geno[i] == self.letters[b]:
                        numerical += str(self.dominance[b])
            if int(numerical[0]) > int(numerical[1]):
                return geno[0]
            elif int(numerical[0]) == int(numerical[1]):
                if geno[0] == geno[1]:
                    return geno[0]
                else:
                    return geno[0] + geno[1]
            elif int(numerical[0]) < int(numerical[1]):
                return geno[1]
        else:
            return geno[0]

    def pheno_to_geno(self, gene, male=False):
        '''
        Takes a Phenotype as a list

        input: gene = ["R"]

        output: [['RR'], ['Rr']]


        input: gene = ["A", "B"]

        output: ["AB"]
        '''

        if male == False:
            posibilities = []
            point = None
            if len(gene) > 1:
                return [["{}{}".format(gene[0], gene[1])]]
            else:
                for i in gene:
                    for a in range(len(self.letters)):
                        if i == self.letters[a]:
                            point = a
                posibilities.append(["{}{}".format(self.letters[point], self.letters[point])])
                for i in range(len(self.dominance)):
                    if self.dominance[point] > self.dominance[i]:
                        posibilities.append(["{}{}".format(self.letters[point], self.letters[i])])

            return posibilities
        else:
            return [["{}".format(gene[0])]]

    def gene_in_genos(self, genes, Male=False):
        '''
        Takes a list of Genotypes

        self determines which genes will return from Genotypes

        input: genes = ['ooRRmmXHXHXrXr', 'ooRRmmXHXhXrXr', 'ooRrmmXHXHXrXr', 'ooRrmmXHXhXrXr']

        output: [['R', 'R'], ['R', 'R'], ['R', 'r'], ['R', 'r']]
        '''
        l = []
        gene = None
        for i in genes:
            first = []
            b = 0
            x = b
            while b < len(i):
                if i[b] == "Y" or i[b] == "X":
                    x = b + 2
                else:
                    x = b + 1
                try:
                    while True:

                        int(i[x])
                        x += 1
                except:
                    gene = Gene.gene_finder(i[b:x])
                    if gene == self:
                        if self.gonosomal == False:
                            if len(first) == 0:
                                first.append(i[b:x])
                                b = x
                            else:
                                first.append(i[b:x])
                                l.append(first)
                                b = len(i)
                        elif Male == True:
                            l.append([i[b:x]])
                            b = len(i)
                        else:
                            if len(first) == 0:
                                first.append(i[b:x])
                                b = x
                            else:
                                first.append(i[b:x])
                                l.append(first)
                                b = len(i)
                    else:
                        b = x
        return l

    def gene_in_pheno(self, pheno):
        '''
        Takes a Phenotype as a string
        Looks for self.letters in pheno
        if cannot find it returns []

        self.letters = ["YO", "Yo"]
        input: pheno = XRXhYo
        output: ['Yo']
        '''
        l = []
        gene = None
        b = 0
        x = b
        while b < len(pheno):
            if pheno[b] == "Y" or pheno[b] == "X":
                x = b + 2
            else:
                x = b + 1
            try:
                while True:

                    int(pheno[x])
                    x += 1
            except:
                gene = Gene.gene_finder(pheno[b:x])
                if gene == self:
                    l.append(pheno[b:x])
                b = x
        return l

    @classmethod
    def gene_finder(cls, letter):
        '''
        looks trough all genes and finds the one with input letters

        input: letter = "Xh"
        output = Gene Class (gene.name = "Hemophili")
        '''
        genes = Gene.Genes
        for gene in genes:
            for i in gene.letters:
                if i == letter:
                    return gene
        return None


def Counter(list, Count=False, mode=False):
    if Count is False and mode == False:
        '''
        removes the same elements from the list
        input: ["AB", "Ao", "AB", "Ao","AB", "AA"]

        output: ["AB", "Ao", "AA"] 
        '''
        a = []
        for i in list:
            g = False
            for b in a:
                if i == b:
                    g = True
            if g is False:
                a.append(i)
        return a
    elif Count and mode == False:
        '''
        Counts all list elements
        input: ["AB", "Ao", "AB", "Ao","AB", "AA"]

        output: [["AB", 3], ["Ao", 2], ["AA", 1]]
        '''
        a = []
        for i in list:
            g = False
            for b in a:
                if i == b[0]:
                    b[1] += 1
                    g = True
            if g is False:
                a.append([i, 1])
        return a
    elif mode == True and Count == False:
        # ["ABRr", 200], ["ABRr", 200], ["ABrr", 200]
        '''
        Given a list with elements first index is a string and the second index is the value
        if the first index is repeated then sums the second index with the repeated elements secon index
        input: ["ABRr", 200], ["ABRr", 200], ["ABrr", 200]

        output: [["ABRr", 400], ["ABrr", 200]]
        '''
        a = []
        for i in list:
            g = False
            for b in a:
                if i[0] == b[0]:
                    b[1] += i[1]
                    g = True
            if g == False:
                a.append([i[0], i[1]])
        return a



def main_func():
    #in this function genotype or phenotypes are guessed
    # -----------------------------------First Phase----------------------------------------
    all = []
    fPhase = 0
    sPhase = 0

    # IN THIS FOR LOOP PATİENTS WİTH GENOTYPES BUT NO PHENOTYPE WİLL HAVE PHENOTYPE ADDED TO THEM
    for person in Patient.Patients:
        toAdd = ""
        x = 0
        g = False
        Otogenes = []
        Gonogenes = []
        if person.GenoType != None and person.PhenoType == None:
            for gene in Gene.Genes:
                if gene.gonosomal == False:
                    z = gene.gene_in_genos(person.GenoType)
                    if len(z) > 0:
                        toAdd += gene.geno_to_pheno(z[0])
                        c = gene.gene_in_pheno(toAdd)
                        if len(c) > 1:
                            Otogenes.append([c[0], gene])
                            Otogenes.append([c[1], gene])
                        else:
                            Otogenes.append([toAdd, gene])
                elif gene.gonosomal == True:
                    z = gene.gene_in_genos(person.GenoType, person.Male)
                    if len(z) > 0:
                        toAdd += gene.geno_to_pheno(z[0])
                        c = gene.gene_in_pheno(toAdd)
                        if len(c) > 1:
                            Gonogenes.append([c[0], gene])
                            Gonogenes.append([c[1], gene])
                        else:
                            Gonogenes.append([toAdd, gene])
            all.append([person, Otogenes, Gonogenes])
            person.PhenoType = toAdd
    # IN THIS FOR LOOP PATİENTS WİTH PHENOTYPE BUT NO GENOTYPE WİLL HAVE POSSİBLE GENOTYPES ADDED TO THEM
    for person in Patient.Patients:
        if person.PhenoType != None and person.GenoType == None:
            i = 0
            Pheno = person.PhenoType
            Otogenes = []
            Gonogenes = []
            g = False
            while i < len(Pheno):
                if (str(Pheno[i]).upper() == "Y" or str(Pheno[i]).upper() == "X") and g == False:
                    x = i + 2
                    g = True
                else:
                    x = i + 1
                try:
                    while True:
                        int(Pheno[x])
                        x += 1
                except:
                    gene = Gene.gene_finder(Pheno[i:x])
                if gene.gonosomal == False:
                    Otogenes.append([Pheno[i: x], gene])
                else:
                    Gonogenes.append([Pheno[i: x], gene])
                g = False
                i = x
            i = 0
            if person.GenoType == None:
                while i < len(Otogenes):

                    if i != len(Otogenes) - 1:
                        if Otogenes[i][1] == Otogenes[i + 1][1]:

                            toAdd = Gene.pheno_to_geno(Otogenes[i][1], [Otogenes[i][0], Otogenes[i + 1][0]])
                            person.gene_merger(toAdd)
                            i += 2
                        else:

                            toAdd = Gene.pheno_to_geno(Otogenes[i][1], [Otogenes[i][0]])
                            person.gene_merger(toAdd)
                            i += 1
                    else:

                        toAdd = Gene.pheno_to_geno(Otogenes[i][1], [Otogenes[i][0]])
                        person.gene_merger(toAdd)
                        i += 1
                i = 0
                while i < len(Gonogenes):
                    if i < len(Gonogenes) - 1:
                        if Gonogenes[i][1] == Gonogenes[i + 1][1]:
                            a = Gonogenes[i]
                            b = Gonogenes[i + 1]
                            toAdd = Gene.pheno_to_geno(a[1], [Gonogenes[i][0], Gonogenes[i + 1][0]], person.Male)
                            i += 2
                        else:
                            a = Gonogenes[i]
                            toAdd = Gene.pheno_to_geno(a[1], [Gonogenes[i][0]], person.Male)
                            person.gene_merger(toAdd)
                            i += 1
                    else:
                        a = Gonogenes[i]
                        toAdd = Gene.pheno_to_geno(a[1], [Gonogenes[i][0]], person.Male)
                        person.gene_merger(toAdd)
                        i += 1

            all.append([person, Otogenes, Gonogenes])

    # ------------------------------------Second Phase------------------------------------------------
    # IN THIS WHILE LOOP STARTING FROM BIGGEST GENERATION PATIENTS PARENT WILL BE ANALYZED TO REMOVE
    # WRONG GENOTYPES
    bigG = Patient.BigG
    while bigG > 1:
        for person in Patient.Patients:
            if person.Generation == bigG:
                father = person.Father
                mother = person.Mother
                newFather = []
                newMother = []
                for i in father.GenoType:
                    newFather.append(i)
                for i in mother.GenoType:
                    newMother.append(i)
                childGood = []
                for gene in Gene.Genes:
                    if person.Male == False or gene.gonosomal == False:
                        childgene = gene.gene_in_genos(person.GenoType, person.Male)
                        mothergene = gene.gene_in_genos(newMother, False)
                        fathergene = gene.gene_in_genos(newFather, True)

                        a = Counter(mothergene)
                        b = Counter(fathergene)
                        c = Counter(childgene)

                        fatherGood = []
                        motherGood = []

                        if len(a) > 0 and len(b) > 0 and len(c) > 0:
                            if gene.gonosomal == False:
                                for i in range(len(a)):
                                    for x in range(len(b)):
                                        if len(a[i]) != 0 and len(b[x]) != 0:
                                            v = False
                                            for y in c:
                                                if [a[i][0], b[x][0]] == y or [a[i][0], b[x][1]] == y or [a[i][1],
                                                                                                          b[x][
                                                                                                              0]] == y or [
                                                    a[i][1], b[x][1]] == y:
                                                    fatherGood.append(b[x])
                                                    motherGood.append(a[i])
                                                    childGood.append(y)
                                                elif [b[x][0], a[i][0]] == y or [b[x][1], a[i][0]] == y or [b[x][0],
                                                                                                            a[i][
                                                                                                                1]] == y or [
                                                    b[x][1], a[i][1]] == y:
                                                    fatherGood.append(b[x])
                                                    motherGood.append(a[i])
                                                    childGood.append(y)
                            else:
                                for i in range(len(a)):
                                    for x in range(len(b)):
                                        if len(a[i]) != 0 and len(b[x]) != 0:
                                            v = False
                                            for y in c:
                                                if [a[i][0], b[x][0]] == y or [a[i][1], b[x][0]] == y:

                                                    fatherGood.append(b[x])
                                                    motherGood.append(a[i])
                                                    childGood.append(y)
                                                elif [b[x][0], a[i][0]] == y or [b[x][0], a[i][1]] == y:

                                                    fatherGood.append(b[x])
                                                    motherGood.append(a[i])
                                                    childGood.append(y)

                            motherGood = Counter(motherGood)
                            fatherGood = Counter(fatherGood)
                            i = 0
                            while i < len(fathergene):
                                v = False
                                for x in fatherGood:
                                    if fathergene[i] == x:
                                        v = True
                                if v == False:
                                    fathergene[i] = []
                                    i += 1
                                else:
                                    i += 1
                            i = 0
                            while i < len(mothergene):
                                v = False
                                for x in motherGood:
                                    if mothergene[i] == x:
                                        v = True
                                if v == False:
                                    mothergene[i] = []
                                    i += 1
                                else:
                                    i += 1
                            i = 0
                            while i < len(newFather):
                                if fathergene[i] == []:
                                    newFather.pop(i)
                                    fathergene.pop(i)
                                else:
                                    i += 1
                            i = 0
                            while i < len(newMother):
                                if mothergene[i] == []:
                                    newMother.pop(i)
                                    mothergene.pop(i)
                                else:
                                    i += 1
                    else:
                        childgene = gene.gene_in_genos(person.GenoType, True)
                        fathergene = gene.gene_in_genos(newFather, True)
                        mothergene = gene.gene_in_genos(newMother, False)

                        a = Counter(mothergene)
                        b = Counter(fathergene)
                        c = Counter(childgene)

                        if len(a) == 0:

                            if b != c:
                                Patient.MutatedPatients.append(person)
                        else:
                            for i in range(len(a)):

                                if a[i][0] != c[0][0] and a[i][1] != c[0][0]:
                                    a[i] = []
                            for i in range(len(mothergene)):
                                v = False
                                for b in a:
                                    if mothergene[i] == b:
                                        v = True
                                if v != True:
                                    mothergene[i] = []
                            i = 0
                            while i < len(mothergene):
                                if mothergene[i] == []:
                                    newMother.pop(i)
                                    mothergene.pop(i)
                                else:
                                    i += 1

                if len(newMother) > 0:
                    mother.GenoType = newMother
                elif len(childgene) > 0:

                    Patient.MutatedPatients.append(person)
                if len(newFather) > 0:
                    father.GenoType = newFather
                elif len(childgene) > 0:
                    Patient.MutatedPatients.append(person)
        bigG -= 1
    Patient.MutatedPatients = Counter(Patient.MutatedPatients)

    # IN THIS WHILE LOOP STARTING FROM BIGGEST GENERATION PATIENTS CHILDREN WILL BE ANALYZED TO REMOVE
    # WRONG GENOTYPES
    bigG = Patient.BigG
    while bigG > 1:
        for person in Patient.Patients:
            v = True
            for i in Patient.MutatedPatients:
                if person == i:
                    v = False
            if v and person.Generation == bigG:
                childGood = []
                if person.Male == False:
                    for gene in Gene.Genes:
                        fathergene = person.Father.GenoType
                        fathergene = Gene.gene_in_genos(gene, fathergene)
                        fathergene = Counter(fathergene)

                        mothergene = person.Mother.GenoType
                        mothergene = Gene.gene_in_genos(gene, mothergene)
                        mothergene = Counter(mothergene)

                        Child = Gene.gene_in_genos(gene, person.GenoType)
                        for a in mothergene:
                            for b in fathergene:
                                for c in Child:
                                    if [a[0], b[0]] == c or [a[1], b[0]] == c or [a[0], b[1]] == c or [a[1], b[1]] == c:

                                        childGood.append(c)
                                    elif [b[0], a[0]] == c or [b[0], a[1]] == c or [b[1], a[0]] == c or [b[1],
                                                                                                         a[1]] == c:

                                        childGood.append(c)
                else:
                    for gene in Gene.Genes:
                        if gene.gonosomal == False:

                            fathergene = person.Father.GenoType
                            fathergene = Gene.gene_in_genos(gene, fathergene)
                            fathergene = Counter(fathergene)

                            mothergene = person.Mother.GenoType
                            mothergene = Gene.gene_in_genos(gene, mothergene)
                            mothergene = Counter(mothergene)

                            Child = Gene.gene_in_genos(gene, person.GenoType)
                            Child = Counter(Child)

                            if len(Child) > 0 and len(fathergene) > 0 and len(mothergene) > 0:
                                for a in mothergene:
                                    for b in fathergene:
                                        for c in Child:
                                            if [a[0], b[0]] == c or [a[1], b[0]] == c or [a[0], b[1]] == c or [a[1],
                                                                                                               b[
                                                                                                                   1]] == c:
                                                childGood.append(c)
                                            elif [b[0], a[0]] == c or [b[1], a[0]] == c or [b[0], a[1]] == c or [
                                                b[1], a[1]] == c:
                                                childGood.append(c)

                newChild = person.GenoType
                childGood = Counter(childGood)
                for good in childGood:
                    goods = []
                    gene = Gene.gene_finder(good[0])
                    childgene = Gene.gene_in_genos(gene, newChild)
                    for i in range(len(childgene)):
                        if childgene[i] == good:
                            goods.append(i)
                    c = []
                    for a in range(len(newChild)):
                        p = True
                        for i in goods:
                            if a == i:
                                p = False
                        if p == False:
                            c.append(newChild[a])
                    newChild = c
                if len(newChild) > 0:
                    person.GenoType = newChild
        bigG -= 1


def disease_posibility_person(id):
    '''
    input: id of a person

    output: if id is wrong False
            else returns a list of disease names and percentage of having the disease
    '''
    target = None
    for person in Patient.Patients:
        if person.id == id:
            target = person
    if target == None:
        return False
    else:
        Genos = target.GenoType
        Male = target.Male
        all = []
        for disease in Disease.Diseases:
            a = 0
            b = 0
            for gene in Genos:
                if disease.disease_posibility(gene, Male):
                    a += 1
                    b += 1
                else:
                    b += 1
            result = round((a / b) * 100, 2)
            all.append([disease.name, result])
        return all


def child_disease_posibility(father_id, mother_id):
    '''
    Takes an id of father and a mother
    if mother or father's id is wrong returns False
    else Crosses the genes via Patient.Crosser and produces both male and female childs

    example male child: [['AorrXHXRYoMM', 294], ['AorrXHXRYoMm', 98], ['AorrXHXRYomM', 98]]
    first index is value and the second index is the number of times it appeared so we have an idea of the chance of
    that genotype appearing

    then disease.disease_posibility returns wheter or not the genotype has the disease
    b is all posibilities and a is the ones that has the disease

    we divide a by b and then multiply with 100 and round with 2 digits after comma
    '''
    result = []
    father = None
    mother = None
    male_child = []
    female_child = []
    for person in Patient.Patients:
        if person.id == father_id:
            father = person

    for person in Patient.Patients:
        if person.id == mother_id:
            mother = person
    if father == None or mother == None:
        return False
    else:
        for gene in Gene.Genes:
            a = gene.gene_in_genos(mother.GenoType, False)
            b = gene.gene_in_genos(father.GenoType, True)
            if len(a) != 0 and len(b) != 0:
                male_child = Patient.Crosser(male_child, [a, b], gene.gonosomal, True)
                female_child = Patient.Crosser(female_child, [a, b], gene.gonosomal, False)
            if gene.letters[0][0] == "Y":
                male_child = Patient.Crosser(male_child, [a, b], gene.gonosomal, True)
        toAdd = []
        print(male_child)
        for disease in Disease.Diseases:
            a = 0
            b = 0
            for geno in male_child:
                if disease.disease_posibility(geno[0], True):
                    a += geno[1]
                b += geno[1]
            res = round((a / b) * 100, 2)
            toAdd.append([disease.name, res])
        result.append(toAdd)
        toAdd = []
        for disease in Disease.Diseases:
            a = 0
            b = 0
            for geno in female_child:
                if disease.disease_posibility(geno[0], False):
                    a += geno[1]
                b += geno[1]
            res = round((a / b) * 100, 2)
            toAdd.append([disease.name, res])
        result.append(toAdd)

        return result


def child_phenotype_posibility(father_id, mother_id):
    #Returns all of the possible phenotypes with the percentage of appearing
    father = None
    mother = None
    male_child = []
    female_child = []
    for person in Patient.Patients:
        if person.id == father_id:
            father = person

    for person in Patient.Patients:
        if person.id == mother_id:
            mother = person
    if father == None or mother == None:
        return False
    else:
        for gene in Gene.Genes:
            a = gene.gene_in_genos(mother.GenoType, False)
            b = gene.gene_in_genos(father.GenoType, True)
            if len(a) != 0 and len(b) != 0:
                male_child = Patient.Crosser(male_child, [a, b], gene.gonosomal, True)
                female_child = Patient.Crosser(female_child, [a, b], gene.gonosomal, False)
            if gene.letters[0][0] == "Y":
                male_child = Patient.Crosser(male_child, [a, b], gene.gonosomal, True)
    for geno in range(len(male_child)):
        toAdd = ""
        for gene in Gene.Genes:
            if gene.gonosomal == False:
                 z = gene.gene_in_genos([male_child[geno][0]])
                 if len(z) > 0:
                      toAdd += gene.geno_to_pheno(z[0])
            elif gene.gonosomal == True:
                z = gene.gene_in_genos([male_child[geno][0]], True)
                if len(z) > 0:
                   toAdd += gene.geno_to_pheno(z[0])
        male_child[geno][0] = toAdd

    for geno in range(len(female_child)):
        toAdd = ""
        for gene in Gene.Genes:
            if gene.gonosomal == False:
                 z = gene.gene_in_genos([female_child[geno][0]])
                 if len(z) > 0:
                    toAdd += gene.geno_to_pheno(z[0])
            elif gene.gonosomal == True:
                z = gene.gene_in_genos([female_child[geno][0]], False)
                if len(z) > 0:
                     toAdd += gene.geno_to_pheno(z[0])
        female_child[geno][0] = toAdd

    female_child = Counter(female_child, mode=True, Count=False)
    male_child = Counter(male_child, mode=True, Count=False)
    a = 0
    b = 0
    fem_list = []
    male_list = []
    for gen in female_child:
        a = gen[1]
        b = 0
        for c in female_child:
            b += c[1]
        fem_list.append([gen[0], round(a*100/b, 2)])
    for gen in male_child:
        a = gen[1]
        b = 0
        for c in male_child:
            b += c[1]
        male_list.append([gen[0], round(a*100/b, 2)])
    return [male_list, fem_list]
    print("Female phenotypes and posibilities: {}".format(fem_list))
    print("Male phenotypes and posibilities: {}".format(male_list))


