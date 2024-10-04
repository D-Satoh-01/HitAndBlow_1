import random
import streamlit as st

def ButtonClick():
    number_inputted = editbox_1.get()

    flag = False
    if len(number_inputted) != 4:
        st.text('入力された値が4桁ではありません')
    else:
        check_int_0_9 = True
        for i in range (4):  # 以下を4回繰り返す
            if (number_inputted[i] < "0") or (number_inputted[i] > "9"):
                st.text('入力された値が数字ではありません')
                check_int_0_9 = False
                break
            if check_int_0_9:
                flag = True
    if flag:
        count_hit = 0
        for i in range(4):
            if number_answer[i] == int(number_inputted[i]):
                count_hit = count_hit + 1
                
        count_blow = 0
        for i_1 in range(4):
            for i_2 in range(4):
                if (int(number_inputted[i_2]) == number_answer[i_1]) and (number_answer[i_1] != int(number_inputted[i_1])) and (number_answer[i_2] != int(number_inputted[i_2])):
                    count_blow += 1
                    break
    
        if count_hit == 4:
            st.text('正解')
        else:
            box_history.insert(st.END, number_inputted + " / H:" + str(count_hit) + " B:" + str(count_blow) + "\n")
        
number_answer = [(random.randint)(0,9),
                 (random.randint)(0,9),
                 (random.randint)(0,9),
                 (random.randint)(0,9)]

st.title('ヒット&ブロー')

box_history = st.text('')

label_1 = st.text('4桁の数字を入力してください')

editbox_1 = st.text_input('', '4桁の数字を入力してください')

button_1 = st.button('チェック', on_click=ButtonClick)