from dash import Dash, dcc, html, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd


# Custom lib import
from data_analyser import DataReader1 , UEManager  , UniteEnseignement ,GlobalResult


file_path = "D:\Personnel\Dev\Projets\Projet Dataviz\src\data\PV_L1_PC.xlsx" #change if needed
data_reader = DataReader1(file_path, "Etud_" , "XX_FIN_PV_XX")

ue_manager = UEManager( file_path ) 
list_of_all_ue_object =  ue_manager.getListeOfUE()
liste_id_numbers_etudiant  = [item for item in  ue_manager.getStudentListe()["Etud_Numér"]  if item is not None] 

# ue_manager.getStudentListe()["Etud_Numér"] # get list numbers student 

#print(" liste numbers etudiants ")
#print(repr(liste_id_numbers_etudiant  ))


bulletin = ue_manager.getBulletinOfAStudent("583902")

# Example data for the bar chart
grades_dict = {
    "Math": 88.5,
    "Science": 92.3,
    "History": 78.4,
    "English": 85.0,
    "Art": 90.2
}

averages_all_students = {}
for ue in list_of_all_ue_object:
    total_grades = []
    for student_id in liste_id_numbers_etudiant:
        # Obtenir la note de l'étudiant pour cette UE
        grade = ue.getStudentGradeForThisUe(student_id)
        if grade is not None and isinstance(grade, (int, float)):
            # Ajouter la note à la liste
            total_grades.append(grade)
    if total_grades:
        # Calculer la moyenne des notes pour cette UE
        averages_all_students[ue.get_libelle_UE()] = sum(total_grades) / len(total_grades)
    else:
        # Si aucune note n'est disponible, la moyenne est 0
        averages_all_students[ue.get_libelle_UE()] = 0

# Créer le graphique camembert avec les moyennes des notes par UE
fig_all_students = go.Figure(data=[go.Pie(labels=list(averages_all_students.keys()), values=list(averages_all_students.values()))])
fig_all_students.update_layout(title='Moyenne des notes par UE')



# Create a bar chart
fig = px.bar(x=list( bulletin.keys()), y=list(bulletin.values()), labels={'x': 'Subjects', 'y': 'Grades'})
fig.update_layout(title='Grades by Subject', xaxis_title='Subject', yaxis_title='Grade')

# Define the layout for the dashboard
layout = dbc.Container([
    html.H1("Student Grades Dashboard"),
    html.Div([
        html.Div([
            dcc.Graph(id='average-all-students', figure=fig_all_students),
        ], className="camembert"),
    ], className="stat"),

    #html.Hr(),
    html.Div([
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id='student-dropdown',
                    options=[{'label': num, 'value': num} for num in liste_id_numbers_etudiant],
                    value=liste_id_numbers_etudiant[1],
                    clearable=False
                ),
                width=6
            )
        ]),
    ], className="dropdown-student"),
    html.Div([
        dbc.Row([
            dbc.Col(
                dcc.Graph(id='grades-chart'),
                width=12
            )
        ])
    ], className="graph-div")
])


@callback(
    Output('grades-chart', 'figure'),
    Input('student-dropdown', 'value')
)
def update_graph(selected_student):
    # Fetch the bulletin for the selected student
    # This function should be defined to fetch data based on student ID
    bulletin = ue_manager.getBulletinOfAStudent( selected_student )
    
    # Create a new figure with the updated data
    fig = px.bar(x=list(bulletin.keys()), y=list(bulletin.values()), labels={'x': 'Subjects', 'y': 'Grades'})
    fig.update_layout(title='Grades by Subject', xaxis_title='Subject', yaxis_title='Grade')
    
    return fig


layout_dashboard =  html.Div([layout], className="dashboard-container")

"""        html.Div([
            dbc.Label('Liste des UE'),
            dash_table.DataTable(
                id='ue_table',
                columns=[{'name': 'Libellé UE', 'id': 'libelle_ue'}],
                data=[{'libelle_ue': ue.get_libelle_UE()} for ue in list_of_all_ue_object],
                editable=False,
            )
        ], className="ue-list"),"""
