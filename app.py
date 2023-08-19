import dash
import dash_core_components as dcc
import dash_html_components as html
# グラフ可視化
import plotly.graph_objects as go
import random
import pprint



######################初期集団の生成######################
#[x_1, x_2, x_3]
def GenOriginParty(min_rand, max_rand, number_of_element, number_of_party):
    party = [[random.randint(min_rand,max_rand) for _ in range(number_of_element)] for _ in range(number_of_party)]
    return party








def GA(number_of_party, number_of_element, min_rand, max_rand, lower_limit, party):
    ####評価関数の下準備####
    #各要素ごとに固めて、配列化
    party_element_list = []
    for i in range(number_of_element):
        party_element = []
        for j in range(number_of_party):
            party_element.append(party[j][i])
        party_element_list.append(party_element)
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
    #得点の集計
    total_point_list = []
    for i in range(number_of_party):
        each_total_point = 0
        for j in range(number_of_element):
            each_total_point = evaluation_value_list[j][i] + each_total_point
        total_point_list.append(each_total_point)
    #パーティ番号の付与
    for i in range(number_of_party):
        party_point = total_point_list[i]
        total_point_list[i] = [party_point, i]
    ####選択の下準備####
    #ソートする
    sorted_data = sorted(total_point_list, reverse=True)
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
    #ランダム生成
    child_list = [[random.randint(min_rand,max_rand) for _ in range(number_of_element)] for _ in range(number_of_party -lower_limit)]
    #合体(新しい母集団の完成)
    result = selected_party_list + child_list
    ####グラフ出力####
    #1位のグラフを出力する
    top_result = selected_party_list[0]
    return result, top_result






######################初期設定######################
#number_of_party
number_of_party = 10
#number_of_element
number_of_element = 6 #<-今回は変更不可
#the range of rand
min_rand = -100
max_rand = 100
#エリート選択時の下限順位
lower_limit = 5
#世代
generation = 2000
#評価関数
def A(x):
    y = (x-12)^(2)-10
    return y

def B(x):
    y = -(x-12)^(2)+10
    return y

def C(x):
    y = x^(3)+x^(2)+x+1
    return y

def D(x):
    y = -x^(3)-x^(2)-x-1
    return y

def E(x):
    y = x+10
    return y

def F(x):
    y = -x+10
    return y
######################実行######################
gen=1
element_0 = []
element_1 = []
element_2 = []
element_3 = []
element_4 = []
element_5 = []

party = GenOriginParty(min_rand, max_rand, number_of_element, number_of_party)
while gen <= generation:
    party, top_result = GA(number_of_party, number_of_element, min_rand, max_rand, lower_limit, party)
    element_0.append(top_result[0])
    element_1.append(top_result[1])
    element_2.append(top_result[2])
    element_3.append(top_result[3])
    element_4.append(top_result[4])
    element_5.append(top_result[5])
    gen = gen + 1

####グラフ化####
graph_gen = generation + 1
gen_number = list(range(1,graph_gen,1))

fig = go.Figure()

fig.add_trace(
    go.Scatter(x = gen_number, #X_label
               y = element_0, #y_label
              text = "(x-12)²-10", #
              mode = 'lines', #折れ線グラフ
              name = 'y=(x-12)²-10', #line_name
              line=dict(color='rgb(239, 85, 59)', width=1, dash='solid') #line_type_detail      
    )
)
fig.add_trace(
    go.Scatter(x = gen_number,
               y = element_1,
              text = "-(x-12)²+10",
              mode = 'lines',
              name = 'y=-(x-12)²+10',
              line=dict(color='rgb(25, 211, 243)', width=1, dash='solid')  
              
    )
)

fig.add_trace(
    go.Scatter(x = gen_number,
               y = element_2,
              text = "x³+x²+x+1",
              mode = 'lines',
              name = 'y=x³+x²+x+1',
              line=dict(color='rgb(188, 189, 34)', width=1, dash='solid'),
              
    )
)

fig.add_trace(
    go.Scatter(x = gen_number,
               y = element_3,
              text = "-x³-x²-x-1",
              mode = 'lines',
              name = 'y=-x³-x²-x-1',
              line=dict(color='firebrick', width=1, dash='solid'),
    )
)

fig.add_trace(
    go.Scatter(x = gen_number,
               y = element_4,
              text = "-x+10",
              mode = 'lines',
              name = 'y=-x+10',
              line=dict(color='rgb(48, 73, 125)', width=1, dash='solid'),
    )
)

fig.add_trace(
    go.Scatter(x = gen_number,
               y = element_5,
              text = "x+10",
              mode = 'lines',
              name = 'y=x+10',
              line=dict(color='rgb(255, 185, 0)', width=1, dash='solid'),
    )
)

fig.update_layout(
    xaxis_title = '',
    yaxis_title = 'Maximum value',
    title=dict(text='<b>The maximum value of variable functions',
                font=dict(size=26,
                    color='grey'),
                x=0.5,
                xanchor='center',
    ),
)

#Import css
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#Rendering
app.layout = html.Div(children=[
    html.H1(children='Hello World'),

    dcc.Graph(
        id='multifunc-engine-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(port="2023", debug=True)