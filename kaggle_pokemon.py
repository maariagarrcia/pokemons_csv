import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import os

for dirname, _, filenames in os.walk('Pokemon.csv'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

sns.set_style('white')

data = pd.read_csv("Pokemon.csv", index_col=0)
df = pd.DataFrame(data=data)
df
df.dtypes
pokemon_summary = df.describe().transpose()
pokemon_summary
plt.figure(figsize=(12, 8))
plt.title("How are the Attributes distributed?")
sns.boxplot(data=df)
df_pokemon2 = df.copy()
df_pokemon2 = df_pokemon2.drop(['Generation', 'Legendary', 'Total'], 1)
df_pokemon2 = pd.melt(df_pokemon2, id_vars=[
                      "Name", "Type 1", "Type 2"], var_name="Stat")
with sns.color_palette([
    "#8ED752", "#F95643", "#53AFFE", "#C3D221", "#BBBDAF",
    "#AD5CA2", "#F8E64E", "#F0CA42", "#F9AEFE", "#A35449",
    "#FB61B4", "#CDBD72", "#7673DA", "#66EBFF", "#8B76FF",
        "#8E6856", "#C3C1D7", "#75A4F9"], n_colors=18, desat=.9):
    plt.figure(figsize=(20, 14))
    plt.ylim(0, 275)
    sns.stripplot(x="Stat", y="value", data=df_pokemon2,
                  hue="Type 1", dodge=True)
    plt.title("Distribution of Key Performance Attributes")
    plt.legend(bbox_to_anchor=(1, 1), loc=2, borderaxespad=0.)
    plt.figure(figsize=(17, 10))
    plt.title("Correlation of Total Performance with single Performance Attributes")
    a3 = sns.regplot(x="Attack", y="Total", data=df,
                     label="Attack", x_jitter=.2)
    a3 = sns.regplot(x="Defense", y="Total", data=df,
                     label="Defense", x_jitter=.2)
    a3 = sns.regplot(x="Speed", y="Total", data=df, label="Speed", x_jitter=.2)
    a5 = sns.regplot(x="Sp. Atk", y="Total", data=df,
                     label="Sp. Atk", x_jitter=.2)
    a6 = sns.regplot(x="Sp. Def", y="Total", data=df,
                     label="Sp. Def", x_jitter=.2)
    a6 = sns.regplot(x="HP", y="Total", data=df, label="HP", x_jitter=.2)
    plt.xlabel("Performance of Single Performance Attributes")
    plt.legend()
    plt.figure(figsize=(20, 10))
    plt.title("How are the Performance Attributes distributed?")
    plt.xlabel("Value of Feature")
    sns.histplot(data=df_pokemon2)
    sns.catplot(x='Legendary', kind='count', data=df, height=6, aspect=1)
    plt.title("Legendary Pokemons are less than 12% of all Pokemons")
    plt.show()
    ax = sns.catplot(x='Generation', data=df, height=8, aspect=1.2,
                     kind='count').set_axis_labels('Generation', '# of Pokemon')
    plt.title("Distribution of Pokemons per Generation")
    plt.show()
    Pokemon_colors = sns.color_palette([
        "#8ED752", "#F95643", "#53AFFE", "#C3D221", "#BBBDAF",
        "#AD5CA2", "#F8E64E", "#F0CA42", "#F9AEFE", "#A35449",
        "#FB61B4", "#CDBD72", "#7673DA", "#66EBFF", "#8B76FF",
        "#8E6856", "#C3C1D7", "#75A4F9"], n_colors=18, desat=.9)
    plt.figure(figsize=(15, 10))
    sns.countplot(x='Type 1', data=df, palette=Pokemon_colors)
    plt.xlabel("Element for Type 1")
    plt.title("Number of Elements for Type 1")
    plt.xticks(rotation=45)
    plt.show()
    plt.figure(figsize=(15, 8))
crosstab = pd.crosstab(df['Generation'], df['Type 1'])
sns.heatmap(crosstab, annot=True, cmap=sns.color_palette(
    "flare"), cbar=False, linewidths=.5)
plt.tick_params(axis='both', which='major', labelsize=10,
                labelbottom=False, bottom=False, top=False, labeltop=True)
plt.title("Heatmap for Type 1")
plt.show()
plt.figure(figsize=(15, 10))
sns.countplot(x='Type 2', data=df, palette=Pokemon_colors)
plt.xticks(rotation=45)
plt.title("Number of Elements for Type 2")
plt.show()
plt.figure(figsize=(15, 8))
crosstab = pd.crosstab(df['Generation'], df['Type 2'])
sns.heatmap(crosstab, annot=True, cmap=sns.color_palette(
    "flare"), cbar=False, linewidths=.5)
plt.tick_params(axis='both', which='major', labelsize=10,
                labelbottom=False, bottom=False, top=False, labeltop=True)
plt.title("Heatmap for Type 2")
plt.show()
x1 = attack_total = sns.relplot(
    data=df, x="Attack", y="Total", hue="Legendary", height=7)
x2 = defense_total = sns.relplot(
    data=df, x="Defense", y="Total", hue="Legendary", height=7)
x3 = speed_total = sns.relplot(
    data=df, x="Speed", y="Total", hue="Legendary", height=7)
plt.show()
sns.relplot(data=df, y="Total", x="HP", hue="Type 1", height=10)
plt.title("Impact of Type of Pokemon to HP and Total Performance")
plt.show()
sns.relplot(
    data=df, x="Attack", y="Total", col="Generation",
    hue="Legendary", style="Type 1",
    palette=["b", "r"], sizes=(40, 60)
)
sns.relplot(
    data=df, x="Attack", y="Total", col="Generation",
    hue="Legendary", style="Type 2",
    palette=["b", "r"], sizes=(40, 100)
)


def comp(Type, Attribute):
    fig, ax = plt.subplots(3, 1)
    fig.set_size_inches(17, 12)
    fig.suptitle('Analysis of different Types (Type 1)', fontsize=16)
    sns.swarmplot(x=Type, y=Attribute,
                  ax=ax[0], data=df, palette=Pokemon_colors)
    sns.violinplot(x=Type, y=Attribute,
                   ax=ax[1], data=df, palette=Pokemon_colors)
    sns.barplot(x=Type, y=Attribute, ax=ax[2], data=df, palette=Pokemon_colors)


comp('Type 1', 'Total')
comp('Type 2', 'Total')
comp('Type 1', 'Attack')
cm = sns.light_palette("skyblue", as_cmap=True)
df[['Name', 'Type 1', 'Type 2', 'HP', 'Attack', 'Defense', 'Speed', 'Generation', 'Total', 'Legendary']].sort_values(
    by=['Total'], ascending=False).head(10).reset_index(drop=True).style.background_gradient(cmap=cm)
