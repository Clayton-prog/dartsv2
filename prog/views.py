from prog import application
# from app import app
from flask import render_template
import dash
import pandas as pd
import numpy as np
# import plotly.express as px
import plotly.graph_objects as go
import plotly
# from plotly.subplots import make_subplots
import json

#Generic Calcualtions
def sort_the_data(player_series, value_series):
    player_names = pd.Series(player_series)
    value_series = pd.Series(value_series)
    the_data = pd.concat([player_series, value_series], axis = 1)
    the_data.columns = ['name', 'score']
    return the_data.sort_values(by=['score'], ascending=False)

def trim_the_data(min_three_games, min_one_win, the_data):
    trimmed_data = the_data
    if(min_one_win == True):
        trimmed_data = the_data.query('score > 0')
    if(min_three_games == True):
        player_series = pd.Series(trimmed_data.name)
        num_games_played = []
        i = 0
        for i in range(len(player_series)):
            num_games_played.append(find_num_games_played(players[i], darts_data))
        value_series = pd.Series(trimmed_data.score)
        num_games_series = pd.Series(num_games_played)
        trimmed_data = pd.concat([player_series, value_series, num_games_series], axis = 1)
        trimmed_data.columns = ['name', 'score','num_games']
        # print("concatanaged dt: ", trimmed_data)
        # print("trimmed_data: ",trimmed_data)
        trimmed_data = trimmed_data.query('num_games >= 3')
        # print("trimmed data after num games query: ", trimmed_data)
    return trimmed_data

def find_num_games_played(players_name, data_frame):
    games_played = data_frame.query('player_name ==@players_name')
    index = games_played.index
    return len(index)

#Bulls Calculations
def find_players_bulls(players_name, data_frame):
    players_data = data_frame.query('player_name ==@players_name')
    players_sums = players_data.sum(axis = 0)
    # print(players_sums.bull)
    return players_sums.bull

def build_total_buls():
    num_bulls = []
    for i in range(len(players)):
        num_bulls.append(find_players_bulls(players[i],darts_data))
    players_in_series = pd.Series(players)
    num_bulls_in_series = pd.Series(num_bulls)
    sorted_data = sort_the_data(players_in_series, num_bulls_in_series)
    fig = go.Figure(data=[go.Bar(
        x=sorted_data.name,
        y=sorted_data.score,
        )])
    fig.update_layout(
        margin=dict(
            l=10,
            r=10,
            b=100,
            t=80,
            pad=1))
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

#Games Won Calculations
def find_players_games_won(players_name, data_frame):
    player_won_game = data_frame.query('player_name ==@players_name & game_won=="Y"')
    index = player_won_game.index
    return len(index)

def build_total_games_won():
    games_won = []
    players_in_series = []
    i = 0
    for i in range(len(players)):
        games_won.append(find_players_games_won(players[i],darts_data))
    players_in_series = pd.Series(players)
    games_won_in_series = pd.Series(games_won)
    sorted_data = sort_the_data(players_in_series, games_won_in_series)
    sorted_data = trim_the_data(False,True,sorted_data)
    fig = go.Figure(data=[go.Bar(
        x=sorted_data.name,
        y=sorted_data.score,
    )])
    fig.update_layout(
        margin=dict(
            l=10,
            r=10,
            b=100,
            t=80,
            pad=1))
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def build_win_percentage():
    player_win_percentage = []
    num_games_played = []
    num_games_won = []
    i = 0
    for i in range(len(players)):
        num_games_won.append(find_players_games_won(players[i],darts_data))
        num_games_played.append(find_num_games_played(players[i],darts_data))
        player_win_percentage.append(num_games_won[i]/num_games_played[i])
    players_in_series = pd.Series(players)
    win_percentage_series = pd.Series(player_win_percentage)
    sorted_data = sort_the_data(players_in_series, win_percentage_series)
    sorted_data = trim_the_data(False,True,sorted_data)
    fig = go.Figure(data=[go.Bar(
        x=sorted_data.name,
        y=sorted_data.score,
    )])
    fig.update_layout(
        margin=dict(
            l=10,
            r=10,
            b=100,
            t=80,
            pad=1))
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

#Per Number percentages
def build_num_percentage(input_number):
    the_percentage = []
    num_hit = []
    num_games_played = []
    i = 0
    players_in_series = pd.Series(players)
    #thinking here
    if(input_number == 0):
        for i in range(len(players)):
            num_games_played.append(find_num_games_played(players[i],darts_data))
            num_hit.append(find_total_bulls_hit(players[i],darts_data))
            the_percentage.append(num_hit[i]/num_games_played[i])
    if(input_number == 20):
        for i in range(len(players)):
            num_games_played.append(find_num_games_played(players[i],darts_data))
            num_hit.append(find_total_twenties_hit(players[i],darts_data))
            the_percentage.append(num_hit[i]/num_games_played[i])
    if(input_number == 19):
        for i in range(len(players)):
            num_games_played.append(find_num_games_played(players[i],darts_data))
            num_hit.append(find_total_nineteens_hit(players[i],darts_data))
            the_percentage.append(num_hit[i]/num_games_played[i])
    if(input_number == 18):
        for i in range(len(players)):
            num_games_played.append(find_num_games_played(players[i],darts_data))
            num_hit.append(find_total_eighteens_hit(players[i],darts_data))
            the_percentage.append(num_hit[i]/num_games_played[i])
    if(input_number == 17):
        for i in range(len(players)):
            num_games_played.append(find_num_games_played(players[i],darts_data))
            num_hit.append(find_total_seventeens_hit(players[i],darts_data))
            the_percentage.append(num_hit[i]/num_games_played[i])
    if(input_number == 16):
        for i in range(len(players)):
            num_games_played.append(find_num_games_played(players[i],darts_data))
            num_hit.append(find_total_sixteens_hit(players[i],darts_data))
            the_percentage.append(num_hit[i]/num_games_played[i])
    if(input_number == 15):
        for i in range(len(players)):
            num_games_played.append(find_num_games_played(players[i],darts_data))
            num_hit.append(find_total_fifteens_hit(players[i],darts_data))
            the_percentage.append(num_hit[i]/num_games_played[i])
    the_percentage = pd.Series(the_percentage)
    sorted_data = sort_the_data(players_in_series, the_percentage)
    sorted_data = trim_the_data(True,False,sorted_data)
    sorted_data = sort_the_data(sorted_data.name,sorted_data.score)
    fig = go.Figure(data=[go.Bar(
        x=sorted_data.name,
        y=sorted_data.score,
    )])
    fig.update_layout(
        margin=dict(
            l=10,
            r=10,
            b=100,
            t=80,
            pad=1))
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

def find_total_bulls_hit(players_name,data_frame):
    players_data = data_frame.query('player_name ==@players_name')
    sumed_data = players_data.sum(axis = 0)
    return sumed_data.bull

def find_total_twenties_hit(players_name,data_frame):
    players_data = data_frame.query('player_name ==@players_name')
    sumed_data = players_data.sum(axis = 0)
    return sumed_data.twenty

def find_total_nineteens_hit(players_name,data_frame):
    players_data = data_frame.query('player_name ==@players_name')
    sumed_data = players_data.sum(axis = 0)
    return sumed_data.nineteen

def find_total_eighteens_hit(players_name,data_frame):
    players_data = data_frame.query('player_name ==@players_name')
    sumed_data = players_data.sum(axis = 0)
    return sumed_data.eighteen

def find_total_seventeens_hit(players_name,data_frame):
    players_data = data_frame.query('player_name ==@players_name')
    sumed_data = players_data.sum(axis = 0)
    return sumed_data.seventeen

def find_total_sixteens_hit(players_name,data_frame):
    players_data = data_frame.query('player_name ==@players_name')
    sumed_data = players_data.sum(axis = 0)
    return sumed_data.sixteen

def find_total_fifteens_hit(players_name,data_frame):
    players_data = data_frame.query('player_name ==@players_name')
    sumed_data = players_data.sum(axis = 0)
    return sumed_data.fifteen

def find_total_games_played():
    num_games_played = darts_data.game_id.unique()
    return len(num_games_played)

#Supulataves calculations here
def find_most_seasoned_vet():
    num_games_played = []
    for i in range(len(players)):
        num_games_played.append(find_num_games_played(players[i],darts_data))
    players_in_series = pd.Series(players)
    num_games_played_series = pd.Series(num_games_played)
    sorted_data = sort_the_data(players_in_series, num_games_played_series)
    sorted_data = sorted_data.reset_index(drop=True)
    return sorted_data.name[0]

def find_most_likely_to_win():
    player_win_percentage = []
    num_games_played = []
    num_games_won = []
    i = 0
    for i in range(len(players)):
        num_games_won.append(find_players_games_won(players[i],darts_data))
        num_games_played.append(find_num_games_played(players[i],darts_data))
        player_win_percentage.append(num_games_won[i]/num_games_played[i])
    players_in_series = pd.Series(players)
    win_percentage_series = pd.Series(player_win_percentage)
    sorted_data = sort_the_data(players_in_series, win_percentage_series)
    sorted_data = trim_the_data(True,True,sorted_data)
    sorted_data = sorted_data.sort_values(by=['score'], ascending=False)
    sorted_data = sorted_data.reset_index(drop=True)
    return sorted_data.name[0]

def find_most_likely_bulls():
    the_percentage = []
    num_hit = []
    num_games_played = []
    i = 0
    players_in_series = pd.Series(players)
    for i in range(len(players)):
        num_games_played.append(find_num_games_played(players[i],darts_data))
        num_hit.append(find_total_bulls_hit(players[i],darts_data))
        the_percentage.append(num_hit[i]/num_games_played[i])
    the_percentage = pd.Series(the_percentage)
    sorted_data = sort_the_data(players_in_series, the_percentage)
    sorted_data = trim_the_data(True,True,sorted_data)
    sorted_data = sorted_data.sort_values(by=['score'],ascending=False)
    sorted_data = sorted_data.reset_index(drop=True)
    # print("most likely to bulls sorted_data: ",sorted_data)
    return sorted_data.name[0]

def find_player_photo(name):
    file_string = '/static/img/players/'+ name + '.jpg'
    # print("file string: ", file_string)
    return file_string

def find_king_of_the_hill(data_frame):
    player_won_game = data_frame.query('game_won=="Y"')
    winning_players = pd.Series(player_won_game.player_name)
    winning_players = winning_players.reset_index(drop=True)
    return winning_players[len(winning_players)-1]

#APP Starts Here
darts_data = pd.read_csv('DartsLog.csv')
players = darts_data.player_name.unique()
#bulls stuff
total_bulls_fig = build_total_buls()
#games won stuff
total_wins_fig = build_total_games_won()
win_percentage_fig = build_win_percentage()
bull_percentage_fig = build_num_percentage(0)
twenties_percentage_fig = build_num_percentage(20)
ninteens_percentage_fig = build_num_percentage(19)
eighteen_percentage_fig = build_num_percentage(18)
seventeen_percentage_fig = build_num_percentage(17)
sixteen_percentage_fig = build_num_percentage(16)
fifteen_percentage_fig = build_num_percentage(15)
most_seasoned_vet = find_most_seasoned_vet()
most_likely_to_win = find_most_likely_to_win()
most_likely_bulls = find_most_likely_bulls()
king_of_the_hill = find_king_of_the_hill(darts_data)

@application.route("/")
def index():
    return render_template("index.html",most_bulls_JSON=total_bulls_fig,
        most_wins_JSON=total_wins_fig,
        winning_percentage_JSON=win_percentage_fig,
        total_bulls_JSON=total_bulls_fig,
        bull_percent_JSON=bull_percentage_fig,
        twenty_percent_JSON=twenties_percentage_fig,
        ninteen_percent_JSON=ninteens_percentage_fig,
        eighteen_percent_JSON=eighteen_percentage_fig,
        seventeen_percent_JSON=seventeen_percentage_fig,
        sixteen_percent_JSON=sixteen_percentage_fig,
        fifteen_percent_JSON=fifteen_percentage_fig,
        most_seasoned_vet=most_seasoned_vet,
        most_likely_to_win=most_likely_to_win,
        most_likely_bulls=most_likely_bulls,
        most_seasoned_vet_pic=find_player_photo(most_seasoned_vet),
        most_likely_to_win_pic=find_player_photo(most_likely_to_win),
        most_likely_bulls_pic=find_player_photo(most_likely_bulls),
        king_of_the_hill=king_of_the_hill,
        king_of_the_hill_pic=find_player_photo(king_of_the_hill))

@application.route("/about")
def about():
    return """
    <h1 style='color: red;'>I'm a red H1 heading!</h1>
    <p>This is a lovely little paragraph</p>
    <code>Flask is <em>awesome</em></code>
    """