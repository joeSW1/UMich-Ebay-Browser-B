from flask import Flask, render_template, request
from pulling_data import * 

raw_data = import_ebay_data()

#list = find_multiple_common_neighbors('hat', 'pre_owned', 'top_rated')
#print(list)
#print(len(exported_dict))
#print(convert_node_to_list_raw_data(exported_dict,list))

table_data = {}

app = Flask(__name__)

@app.route('/')
def index():
    #list = import_ebay_data()
    #return '<p>'+ str(list[0]) + '</p>' + '<p>'+ str(text) + '</p>' 
    #if request.form['options']:
    #    data = request.form['options']
    #else:
    category = "hat"
    condition = "pre_owned"
    reputation = "top"

    node_list = find_multiple_common_neighbors('hat', 'pre_owned', 'top_rated')
    #print(list)
    #print(len(exported_dict))
    raw_data_list = convert_node_to_list_raw_data(raw_data,node_list)

    return render_template('selector.html', input_data = raw_data_list, category = category, condition = condition, reputation = reputation)

@app.route('/handle_data', methods=['POST'])
def handle_data():
    category = request.form['category']
    condition = request.form['condition']
    reputation = request.form['reputation']

    node_list = find_multiple_common_neighbors(category, condition, reputation)
    raw_data_list = convert_node_to_list_raw_data(raw_data,node_list)

    return render_template('selector.html', input_data = raw_data_list, category = category, condition = condition, reputation = reputation)


if __name__=='__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)

