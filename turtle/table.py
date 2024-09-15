from prettytable import PrettyTable


table=PrettyTable()
table.add_column("Pokemon",["Pikachu","Squirtle","Charmander"])
table.add_column("type",["electric","water","fire"])
table.align="r"
print(table)


