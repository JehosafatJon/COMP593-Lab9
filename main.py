"""
COMP 593 - Lab 9: Pokemon Stat Viewer

Description:
  Displays stats and information about a pokemon in a simple GUI
  using information from PokeAPI.

Usage:
  python main.py
"""

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from poke_api import search_pokemon

# GUI Init
root = Tk()
root.title("Jon's PokeViewer!")
root.geometry("515x300")
root.resizable(0,0)

# Button Handler
def handle_get_info_button_click():
    # Get the name of the pokemon
    pokemon_name = ent_name.get().strip()
    if pokemon_name == "":
        return # button does nothing if nothing in entry field

    # Get the pokemon info dictionary from poke_api
    poke_info = search_pokemon(pokemon_name)
    if poke_info is None:
        messagebox.showinfo(title='Error', message="Unable to get the info for that pokemon.", icon='error')
        return

    # Set values to labels
    lbl_val_height['text'] = f"{poke_info['height']} dm"
    lbl_val_weight['text'] = f"{poke_info['weight']} hg"
    
    type_text = ""
    for type in [entry['type']['name'] for entry in poke_info['types']]:
        type_text += type.title() if type_text == "" else f", {type.title()}"
    lbl_val_type['text'] = type_text

    # Set values to bars
    bar_hp['value'] = poke_info['stats'][0]['base_stat']
    bar_atk['value'] = poke_info['stats'][1]['base_stat']
    bar_def['value'] = poke_info['stats'][2]['base_stat']
    bar_spc_atk['value'] = poke_info['stats'][3]['base_stat']
    bar_spc_def['value'] = poke_info['stats'][4]['base_stat']
    bar_speed['value'] = poke_info['stats'][5]['base_stat']

    return

# Frame Creation
frm_top = ttk.Frame(root)
frm_top.grid(row=0, column=0, columnspan=2)

frm_bot_left = ttk.LabelFrame(root, text="Info")
frm_bot_left.grid(row=1, column=0, sticky="N", padx=(10,5))

frm_bot_right = ttk.LabelFrame(root, text="Stats")
frm_bot_right.grid(row=1, column=1, padx=(5,10))


# Add Widgets
# Top 
lbl_name = ttk.Label(frm_top, text = "Pokemon Name:")
lbl_name.grid(padx=10)

ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0, column=1)

btn_ent = ttk.Button(frm_top, text = "Get Info", command = handle_get_info_button_click)
btn_ent.grid(row=0, column=2, padx=10, pady=25)


# Bot Left
lbl_height = ttk.Label(frm_bot_left, text = "Height:")
lbl_height.grid(row=0, column=0, sticky="E", pady=(10,5))
lbl_val_height = ttk.Label(frm_bot_left, width=20)
lbl_val_height.grid(row=0, column=1, columnspan=2, pady=(10,5))

lbl_weight = ttk.Label(frm_bot_left, text = "Weight:")
lbl_weight.grid(row=1, column=0, sticky="E", pady=5)
lbl_val_weight = ttk.Label(frm_bot_left, width=20)
lbl_val_weight.grid(row=1, column=1, columnspan=2, pady=5)

lbl_type = ttk.Label(frm_bot_left, text = "Type:")
lbl_type.grid(row=2, column=0, sticky="E", pady=(5,10))
lbl_val_type = ttk.Label(frm_bot_left, width=20)
lbl_val_type.grid(row=2, column=1, columnspan=2, pady=(5,10))


# Bot Right
lbl_hp = ttk.Label(frm_bot_right, text = "HP:")
lbl_hp.grid(row=0, column=0, sticky="E")
bar_hp = ttk.Progressbar(frm_bot_right, length=200, value=0, maximum=255)
bar_hp.grid(row=0, column=1, columnspan=3, padx=10, pady=5)

lbl_atk = ttk.Label(frm_bot_right, text = "Attack:")
lbl_atk.grid(row=1, column=0, sticky="E")
bar_atk = ttk.Progressbar(frm_bot_right, length=200, value=0, maximum=255)
bar_atk.grid(row=1, column=1, columnspan=3, padx=10, pady=5)

lbl_def = ttk.Label(frm_bot_right, text = "Defense:")
lbl_def.grid(row=2, column=0, sticky="E")
bar_def = ttk.Progressbar(frm_bot_right, length=200, value=0, maximum=255)
bar_def.grid(row=2, column=1, columnspan=3, padx=10, pady=5)

lbl_spc_atk = ttk.Label(frm_bot_right, text = "Special Attack:")
lbl_spc_atk.grid(row=3, column=0, sticky="E")
bar_spc_atk = ttk.Progressbar(frm_bot_right, length=200, value=0, maximum=255)
bar_spc_atk.grid(row=3, column=1, columnspan=3, padx=10, pady=5)

lbl_spc_def = ttk.Label(frm_bot_right, text = "Special Defense:")
lbl_spc_def.grid(row=4, column=0, sticky="E")
bar_spc_def = ttk.Progressbar(frm_bot_right, length=200, value=0, maximum=255)
bar_spc_def.grid(row=4, column=1, columnspan=3, padx=10, pady=5)

lbl_spd = ttk.Label(frm_bot_right, text = "Speed:")
lbl_spd.grid(row=5, column=0, sticky="E")
bar_speed = ttk.Progressbar(frm_bot_right, length=200, value=0, maximum=255)
bar_speed.grid(row=5, column=1, columnspan=3, padx=10, pady=(5,10))


# GUI Loop
root.mainloop()