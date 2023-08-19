import random
import pandas as pd
import numpy as np
# グラフ可視化
import plotly.graph_objects as go
import pprint
import copy
#~.iat[列,行]

######################初期集団の生成######################
#[x_1, x_2, x_3]
def GenOriginParty(min_rand, max_rand, number_of_element, number_of_party):
    party = [[random.randint(min_rand,max_rand) for _ in range(number_of_element)] for _ in range(number_of_party)]
    print("The Origin Party")
    pprint.pprint(party)
    return party








def GA(number_of_party, number_of_element, min_rand, max_rand, lower_limit, probability, party):
    ####評価関数の下準備####
    #各要素ごとに固めて、配列化
    party_element_list = []
    for i in range(number_of_element):
        party_element = []
        for j in range(number_of_party):
            party_element.append(party[j][i])
        party_element_list.append(party_element)

    print("Elemented ([[No.0 elements][No.1 elements]...])")
    pprint.pprint(party_element_list)

    ####評価関数####
    for i in range(number_of_element):
        object = party_element_list[i]
        if i==0:
            result_0_list = []
            for j in range(number_of_party):
                result_0 = A(object[j])
                result_0_list.append(result_0)
        elif i==1:
            result_1_list = []
            for j in range(number_of_party):
                result_1 = B(object[j])
                result_1_list.append(result_1)
        elif i==2:
            result_2_list = []
            for j in range(number_of_party):
                result_2 = C(object[j])
                result_2_list.append(result_2)
        elif i==3:
            result_3_list = []
            for j in range(number_of_party):
                result_3 = D(object[j])
                result_3_list.append(result_3)
        elif i==4:
            result_4_list = []
            for j in range(number_of_party):
                result_4 = E(object[j])
                result_4_list.append(result_4)
        elif i==5:
            result_5_list = []
            for j in range(number_of_party):
                result_5 = F(object[j])
                result_5_list.append(result_5)

    evaluation_value_list = []
    evaluation_value_list.append(result_0_list)
    evaluation_value_list.append(result_1_list)
    evaluation_value_list.append(result_2_list)
    evaluation_value_list.append(result_3_list)
    evaluation_value_list.append(result_4_list)
    evaluation_value_list.append(result_5_list)

    print("Evaluation Value ([[No.0 elements][No.1 elements]...])")
    pprint.pprint(evaluation_value_list)


    #得点の集計
    total_point_list = []
    for i in range(number_of_party):
        each_total_point = 0
        for j in range(number_of_element):
            each_total_point = evaluation_value_list[j][i] + each_total_point
        total_point_list.append(each_total_point)

    print("Total Score ([No.0 party score, No.1 party score, ...]])")
    pprint.pprint(total_point_list)

    #パーティ番号の付与
    for i in range(number_of_party):
        party_point = total_point_list[i]
        total_point_list[i] = [party_point, i]

    print("Add party ID ([[No.0 party ID, No.0 party score],[ No.1 party ID, No1 party score], ...]])")
    pprint.pprint(total_point_list)

    ####選択の下準備####
    #ソートする
    sorted_data = sorted(total_point_list, reverse=True)

    print("Sorted Data")
    print(sorted_data)

    ####選択 (エリート戦略)####
    selected_data = sorted_data[:lower_limit]

    selected_party_list = []
    for i in range(lower_limit):
        for j in range(2):
            if j==0:
                pass
            elif j==1:
                selected_party = party[selected_data[i][j]]
        selected_party_list.append(selected_party)

    print("Selected Party list")
    pprint.pprint(selected_party_list)

    #交叉 (1点交叉)
    child = []
    child_list = []
    for i in range(number_of_party - lower_limit):
        number_of_element_molded = number_of_element - 1
        random_choice_1_list = selected_party_list[random.randint(0, lower_limit - 1)]
        random_choice_2_list = selected_party_list[random.randint(0, lower_limit - 1)]
        print("Parents")
        print(random_choice_1_list)
        print(random_choice_2_list)
        random_cut = random.randint(0, number_of_element_molded)
        random_cut_list = random_choice_1_list[:random_cut]
        random_cut_2_list = random_choice_2_list[random_cut:number_of_element]
        print("The parts of Children")
        print(random_cut_list)
        print(random_cut_2_list)
        child = random_cut_list + random_cut_2_list
        child_list.append(child)

    print("赤ちゃん爆誕")
    pprint.pprint(child_list)


    #突然変異
    rest_of_probability = 1 - probability
    for i in range(number_of_party - lower_limit):
        mutation_party = child_list[i]
        flag = np.random.choice([0,1], p=[probability, rest_of_probability])
        if flag==0:
            change_child_part = random.randint(0, number_of_element_molded)
            choice_element_number = random.randint(min_rand, max_rand)
            mutation_party[change_child_part] = choice_element_number
        elif flag==1:
            pass

    print("赤ちゃんの突然変異")
    pprint.pprint(child_list)

    #合体(新しい母集団の完成)
    result = selected_party_list + child_list
    print("合体（新しい母集団の完成）")
    pprint.pprint(result)

    ####グラフ出力####
    #1位のグラフを出力する
    return result






######################初期設定######################
#number_of_party
number_of_party = 100
#number_of_element
number_of_element = 6 #<-今回は変更不可
#the range of rand
min_rand = -100
max_rand = 100
#エリート選択時の下限順位
lower_limit = 5
#突然変異の発生割合 (0~1)
probability = 1
#世代
generation = 1000
#評価関数
def A(x):
    y = (x-1)^(2)-12
    return y

def B(x):
    y = -(x-1)^(2)+12
    return y

def C(x):
    y = x^(3)+x^(2)+x+1
    return y

def D(x):
    y = -x^(3)-x^(2)-x-1
    return y

def E(x):
    y = x
    return y

def F(x):
    y = -x
    return y
######################実行######################
gen=1
party = GenOriginParty(min_rand, max_rand, number_of_element, number_of_party)
while gen <= generation:
    print(f"第{gen}世代")
    party = GA(number_of_party, number_of_element, min_rand, max_rand, lower_limit, probability, party)
    gen = gen + 1