import random

with open('allwords.txt', 'r', encoding = 'utf-8') as aw:
    lines = aw.readlines()
    
# Существительные 

    def noun_m1():
        noun_m1 = []
        noun_m1 = lines[1].split(' ')
        return random.choice(noun_m1)

    def noun_f1():
        noun_f1 = []
        noun_f1 = lines[2].split(' ')
        return random.choice(noun_f1)

    def noun_m2():
        noun_m2 = []
        noun_m2 = lines[3].split(' ')
        return random.choice(noun_m2)

    def noun_f2():
        noun_f2 = []
        noun_f2 = lines[4].split(' ')
        return random.choice(noun_f2)

    def noun_mid2():
        noun_mid2 = []
        noun_mid2 = lines[5].split(' ')
        return random.choice(noun_mid2)

    def noun_m3():
        noun_m3 = []
        noun_m3 = lines[6].split(' ')
        return random.choice(noun_m3)
    
    def noun_f3():
        noun_f3 = []
        noun_f3 = lines[7].split(' ')
        return random.choice(noun_f3)

    def noun_mid3():
        noun_mid3 = []
        noun_mid3 = lines[8].split(' ')
        return random.choice(noun_mid3)

    def noun_m4():
        noun_m4 = []
        noun_m4 = lines[9].split(' ')
        return random.choice(noun_m4)
    
    def noun_f4():
        noun_f4 = []
        noun_f4 = lines[10].split(' ')
        return random.choice(noun_f4)

    def noun_mid4():
        noun_mid4 = []
        noun_mid4 = lines[11].split(' ')
        return random.choice(noun_mid4)

    def noun_m5():
        noun_m5 = []
        noun_m5 = lines[12].split(' ')
        return random.choice(noun_m5)

    def noun_f5():
        noun_f5 = []
        noun_f5 = lines[13].split(' ')
        return random.choice(noun_f5)

    def noun_mid5():
        noun_mid5 = []
        noun_mid5 = lines[14].split(' ')
        return random.choice(noun_mid5)

    def noun_m6():
        noun_m6 = []
        noun_m6 = lines[15].split(' ')
        return random.choice(noun_m6)
    
    def noun_f6():
        noun_f6 = []
        noun_f6 = lines[16].split(' ')
        return random.choice(noun_f6)

    def noun_mid6():
        noun_mid6 = []
        noun_mid6 = lines[17].split(' ')
        return random.choice(noun_mid6)
    
# Глаголы

    def verb_1():
        verb_1 = []
        verb_1 = lines[20].split(' ')
        return random.choice(verb_1)
    
    def verb_2():
        verb_2 = []
        verb_2 = lines[21].split(' ')
        return random.choice(verb_2)
    
    def verb_3():
        verb_3 = []
        verb_3 = lines[22].split(' ')
        return random.choice(verb_3)
    
    def verb_4():
        verb_4 = []
        verb_4 = lines[23].split(' ')
        return random.choice(verb_4)
    
    def verb_5():
        verb_5 = []
        verb_5 = lines[24].split(' ')
        return random.choice(verb_5)
    
    def verb_6():
        verb_6 = []
        verb_6 = lines[25].split(' ')
        return random.choice(verb_6)

# Союзы

    def conj_1():
        conj_1 = []
        conj_1 = lines[28].split(' ')
        return random.choice(conj_1)
    
    def conj_2():
        conj_2 = []
        conj_2 = lines[29].split(' ')
        return random.choice(conj_2)

# Прилагательные

    def adj_m1():
        adj_m1 = []
        adj_m1 = lines[32].split(' ')
        return random.choice(adj_m1)
    
    def adj_m2():
        adj_m2 = []
        adj_m2 = lines[33].split(' ')
        return random.choice(adj_m2)
        
    def adj_f2():
        adj_f2 = []
        adj_f2 = lines[34].split(' ')
        return random.choice(adj_f2)
    
    def adj_m3():
        adj_m3 = []
        adj_m3 = lines[35].split(' ')
        return random.choice(adj_m3)
           
    def adj_f3():
        adj_f3 = []
        adj_f3 = lines[36].split(' ')
        return random.choice(adj_f3)
        
    def adj_mid3():
        adj_mid3 = []
        adj_mid3 = lines[37].split(' ')
        return random.choice(adj_mid3)
    
    def adj_m4():
        adj_m4 = []
        adj_m4 = lines[38].split(' ')
        return random.choice(adj_m4)
           
    def adj_f4():
        adj_f4 = []
        adj_f4 = lines[39].split(' ')
        return random.choice(adj_f4)
        
    def adj_mid4():
        adj_mid4 = []
        adj_mid4 = lines[40].split(' ')
        return random.choice(adj_mid4)
    
    def adj_m5():
        adj_m5 = []
        adj_m5 = lines[41].split(' ')
        return random.choice(adj_m5)
           
    def adj_f5():
        adj_f5 = []
        adj_f5 = lines[42].split(' ')
        return random.choice(adj_f5)
        
    def adj_mid5():
        adj_mid5 = []
        adj_mid5 = lines[43].split(' ')
        return random.choice(adj_mid5)
    
    def adj_m6():
        adj_m6 = []
        adj_m6 = lines[44].split(' ')
        return random.choice(adj_m6)
           
    def adj_f6():
        adj_f6 = []
        adj_f6 = lines[45].split(' ')
        return random.choice(adj_f6)
        
    def adj_mid6():
        adj_mid6 = []
        adj_mid6 = lines[46].split(' ')
        return random.choice(adj_mid6)

# Наречия   

    def adv_2():
        adv_2 = []
        adv_2 = lines[49].split(' ')
        return random.choice(adv_2)
            
    def adv_3():
        adv_3 = []
        adv_3 = lines[50].split(' ')
        return random.choice(adv_3)
            
    def adv_4():
        adv_4 = []
        adv_4 = lines[51].split(' ')
        return random.choice(adv_4)
            
    def adv_5():
        adv_5 = []
        adv_5 = lines[52].split(' ')
        return random.choice(adv_5)
            
    def adv_6():
        adv_6 = []
        adv_6 = lines[53].split(' ')
        return random.choice(adv_6)
    
# Числительные
                    
    def numeral_m2():
        numeral_m2 = []
        numeral_m2 = lines[56].split(' ')
        return random.choice(numeral_m2)
                        
    def numeral_f2():
        numeral_f2 = []
        numeral_f2 = lines[57].split(' ')
        return random.choice(numeral_f2)
                        
    def numeral_mid2():
        numeral_mid2 = []
        numeral_mid2 = lines[58].split(' ')
        return random.choice(numeral_mid2)
                        
    def numeral_m3():
        numeral_m3 = []
        numeral_m3 = lines[59].split(' ')
        return random.choice(numeral_m3)
                            
    def numeral_f3():
        numeral_f3 = []
        numeral_f3 = lines[60].split(' ')
        return random.choice(numeral_f3)
                            
    def numeral_mid3():
        numeral_mid3 = []
        numeral_mid3 = lines[61].split(' ')
        return random.choice(numeral_mid3)
                        
    def numeral_m4():
        numeral_m4 = []
        numeral_m4 = lines[62].split(' ')
        return random.choice(numeral_m4)
                            
    def numeral_f4():
        numeral_f4 = []
        numeral_f4 = lines[63].split(' ')
        return random.choice(numeral_f4)
                            
    def numeral_mid4():
        numeral_mid4 = []
        numeral_mid4 = lines[64].split(' ')
        return random.choice(numeral_mid4)
                        
    def numeral_m5():
        numeral_m5 = []
        numeral_m5 = lines[65].split(' ')
        return random.choice(numeral_m5)
                            
    def numeral_f5():
        numeral_f5 = []
        numeral_f5 = lines[66].split(' ')
        return random.choice(numeral_f5)
                            
    def numeral_mid2():
        numeral_mid5 = []
        numeral_mid5 = lines[67].split(' ')
        return random.choice(numeral_mid5)
                            
    def numeral_f6():
        numeral_f6 = []
        numeral_f6 = lines[68].split(' ')
        return random.choice(numeral_f6)
                            
    def numeral_mid6():
        numeral_mid6 = []
        numeral_mid6 = lines[69].split(' ')
        return random.choice(numeral_mid6)
    
    def row_1_5():
        phrase_of_5_1 =[adj_m1() + ' ' + noun_m4(), adj_m2() + ' ' + noun_m3(), adj_m3() + ' ' + noun_m2(), adj_m4() + ' ' + noun_m1(),
                        numeral_m2() + ' ' + noun_m1() + ' ' + verb_2(), numeral_m2() + ' ' + noun_m2() + ' ' + verb_1(),
                        numeral_m2() + ' ' + noun_m3(), numeral_m3() + ' ' + noun_m1() + ' ' + verb_1(), numeral_m3() + ' ' + noun_m2(),
                        adj_f2() + ' ' + noun_f3(), adj_f3() + ' ' + noun_f2(), adj_f4() + ' ' + noun_f1(),
                        numeral_f2() + ' ' + noun_f1() + ' ' + verb_2(), numeral_f2() + ' ' + noun_f2() + ' ' + verb_2(), numeral_f2() + ' ' + noun_f3(),
                        numeral_f3() + ' ' + noun_f1() + ' ' + verb_1(), numeral_f3() + ' ' + noun_f2(),
                        numeral_mid2() + ' ' + verb_2(), numeral_mid2() + ' ' + noun_mid2() + ' ' + verb_1(),
                        numeral_mid2() + ' ' + noun_mid3(),
                        numeral_mid3() +  ' ' + verb_1(), numeral_mid3() + ' ' + noun_mid2(),noun_m5(), noun_f5(), noun_mid5()]
        return random.choice(phrase_of_5_1)

    def row_1_7():
        phrase_of_7_1 =[adv_2() + ' ' + verb_5(), adv_3() + ' ' + verb_4(), adv_4() + ' ' + verb_3(), adv_5() + ' ' + verb_2(), adv_6() + ' ' + verb_1(),
                        adv_2() + ' ' + verb_4() + ' ' + conj_1(), adv_2() + ' ' + verb_3() + ' ' + conj_2(),
                        adv_3() + ' ' + verb_3() + ' ' + conj_1(), adv_3() + ' ' + verb_2() + ' ' + conj_2(),
                        adv_4() + ' ' + verb_2() + ' ' + conj_1(), adv_4() + ' ' + verb_1() + ' ' + conj_2(),
                        adv_5() + ' ' + verb_1() + ' ' + conj_1(), adv_5() + ' ' + conj_2(),
                        adv_6() + ' ' + conj_1()]
        return random.choice(phrase_of_7_1)

    def row_2_5():
        phrase_of_5_2 =[verb_1() + ' ' + noun_m4(), verb_2() + ' ' + noun_m3(), verb_3() + ' ' + noun_m2(), verb_4() + ' ' + noun_m1(),
                        verb_1() + ' ' + noun_f4(), verb_2() + ' ' + noun_f3(), verb_3() + ' ' + noun_f2(), verb_4() + ' ' + noun_f1(),
                        verb_1() + ' ' + noun_mid4(), verb_2() + ' ' + noun_mid3(), verb_3() + ' ' + noun_mid2()]
        return random.choice(phrase_of_5_2)


    def row_2_7():
        phrase_of_7_2 =[noun_m1() + ' ' + verb_6(),noun_m2() + ' ' + verb_5(),noun_m3() + ' ' + verb_4(),noun_m4() + ' ' +verb_3(),
                        noun_m5() + ' ' + verb_2(),
                        noun_m6() + ' ' + verb_1(),
                        noun_f1() + ' ' + verb_6(), noun_f2() + ' ' + verb_5(), noun_f3() + ' ' + verb_4(), noun_f4() + ' ' + verb_3(),
                        noun_f5() + ' ' + verb_2(),
                        noun_f6() + ' ' + verb_1(), noun_mid2() + ' ' + verb_5(), noun_mid3() + ' ' + verb_4(), noun_mid4() + ' ' + verb_3(),
                        noun_mid5() + ' ' + verb_2(),
                        noun_mid6() + ' ' + verb_1()]
        return random.choice(phrase_of_7_2)

    def row_3_5():
        phrase_of_5_3 =[verb_5(), adv_5()]
        return random.choice(phrase_of_5_3)

    def haiku():
        ready = [row_2_5() + '\n' + row_2_7() + '\n' + row_1_5(),
                 row_3_5() + '\n' + row_2_7() + '\n' + row_3_5(),
                 row_1_5() + '\n' + row_1_7() + '\n' + row_3_5()]
        return random.choice(ready)
print(haiku()) 
