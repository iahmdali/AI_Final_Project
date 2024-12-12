import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import json  

# Loading final accuracies
df_accuracies = pd.read_csv('final_accuracies.csv')

# Loading training histories from JSON file
with open('histories.json', 'r') as f:
    histories_data = json.load(f)

# Extracting activation function names
activation_functions = df_accuracies['Activation Function'].tolist()

# Initializing the Dash app
app = dash.Dash(__name__)

# Defining the app layout
app.layout = html.Div(children=[
    html.H1(children='CNN Activation Function Comparison'),

    html.Div(children='''
        Select an Activation function to see its Validation Accuracy and Training History.
    '''),

    dcc.Dropdown(
        id='activation-dropdown',
        options=[{'label': name, 'value': idx} for idx, name in enumerate(activation_functions)],
        value=0,  
        clearable=False
    ),

    html.H2(id='accuracy-output'),

    dcc.Graph(id='accuracy-graph')
])

# Defining callback to update accuracy text and graph
@app.callback(
    [Output('accuracy-output', 'children'),
     Output('accuracy-graph', 'figure')],
    [Input('activation-dropdown', 'value')]
)
def update_output(selected_idx):
    # Getting the selected activation function name
    activation_name = activation_functions[selected_idx]

    # Getting the corresponding final validation accuracy
    val_acc = df_accuracies.loc[df_accuracies['Activation Function'] == activation_name, 'Validation Accuracy'].values[0]

    # Preparing the accuracy text
    accuracy_text = f"Final Validation Accuracy for {activation_name}: {val_acc:.4f}"

    # Getting the training history data
    history_data = histories_data[selected_idx]
    val_acc_history = history_data['val_accuracy']
    epochs = list(range(1, len(val_acc_history) + 1))

    # Creating the Plotly figure
    trace = go.Scatter(
        x=epochs,
        y=val_acc_history,
        mode='lines+markers',
        name='Validation Accuracy',
        hoverinfo='text',
        text=[f'Epoch {epoch}: {acc:.4f}' for epoch, acc in zip(epochs, val_acc_history)]
    )

    layout = go.Layout(
        title=f'Validation Accuracy Over Epochs for {activation_name}',
        xaxis=dict(title='Epoch'),
        yaxis=dict(title='Validation Accuracy'),
        hovermode='closest'
    )

    figure = go.Figure(data=[trace], layout=layout)

    return accuracy_text, figure

if __name__ == '__main__':
    app.run_server(debug=True)
