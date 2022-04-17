import imp
from inspect import FrameInfo
from tkinter import *
from tkinter import ttk
from pokeapi import get_pokemon_info

def main():
    
    #Create window
    root = Tk()
    root.title("Pokemon Info Viewer")
    root.iconbitmap("Poke-Ball.ico")
    root.resizable(False, False)
    
    #Create the root window(window frame)

    from_user_input = ttk.Frame(root)
    from_user_input.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    from_info = ttk.LabelFrame(root, text='Info')
    from_info.grid(row=1, column=0, padx=10, pady=10, sticky=N)

    from_stats = ttk.LabelFrame(root, text='Stats')
    from_stats.grid(row=1, column=1, padx=10, pady=10, sticky=N)

    #Populate the widgets in the user input frame

    lbl_name = ttk.Label(from_user_input, text = 'Pokemon Name :')
    lbl_name.grid(row=0, column=0, padx=10, pady=10)

    ent_name = ttk.Entry(from_user_input)
    ent_name.grid(row=0, column=1,pady=10)

    def btn_get_info_click():

        #Get the Pokemon Info Form PokeAPI
        pokemon_name = ent_name.get()
        poke_dict = get_pokemon_info(pokemon_name)

        #Populate displayed Pokemon values
        if poke_dict:
            lbl_height_val['text'] = str(poke_dict['height']) + ' dm'

            lbl_weight_val['text'] = str(poke_dict['weight']) + ' hg'

            types_list = [t['type']['name'] for t in poke_dict['types']]
            lbl_type_val['text' ] = ', '.join(types_list)

            prg_hp['value'] = poke_dict['stats'][0]['base_stat']

            prg_attkack['value'] = poke_dict['stats'][1]['base_stat']

            prg_defense['value'] = poke_dict['stats'][2]['base_stat']

            prg_special_attack['value'] = poke_dict['stats'][3]['base_stat']

            prg_special_defense['value'] = poke_dict['stats'][4]['base_stat']

            prg_speed['value'] = poke_dict['stats'][5]['base_stat']

    btn_get_info= ttk.Button(from_user_input, text = 'Get Info', command=btn_get_info_click)
    btn_get_info.grid(row=0, column=2, padx=10, pady=10)

    #Populate the widgets in the info frame

    lbl_height = ttk.Label(from_info, text = "Height : ")
    lbl_height.grid(row=10, column=10, padx=(0,10), pady=10, sticky=E)
    lbl_height_val = ttk.Label(from_info, text = " TBD ")
    lbl_height_val.grid(row=10, column=20, padx=(0,10), pady=10, sticky=W)

    lbl_weight = ttk.Label(from_info, text = "Weight : ")
    lbl_weight.grid(row=20, column=10, padx=(0,10), pady=10, sticky=E)
    lbl_weight_val = ttk.Label(from_info, text = " TBD ")
    lbl_weight_val.grid(row=20, column=20, padx=(0,10), pady=10, sticky=W)

    lbl_type = ttk.Label(from_info, text = "Type : ")
    lbl_type.grid(row=30, column=10, padx=(0,10), pady=10, sticky=E)
    lbl_type_val = ttk.Label(from_info, text = " TBD ")
    lbl_type_val.grid(row=30, column=20, padx=(0,10), pady=10, sticky=W)


    #Populate the widgets in the stats
    
    lbl_hp= ttk.Label(from_stats, text = "HP:")
    lbl_hp.grid(row=10 , column=10, padx=(0,10), pady=10, sticky=E)
    prg_hp= ttk.Progressbar(from_stats , length= 200 , maximum= 255)
    prg_hp.grid(row=10 , column=20, padx=(0,10), pady=10, sticky=W)

    lbl_attack= ttk.Label(from_stats, text = "Attack:")
    lbl_attack.grid(row=20 , column=10, padx=(0,10), pady=10, sticky=E)
    prg_attkack= ttk.Progressbar(from_stats , length= 200 , maximum= 255)
    prg_attkack.grid(row=20 , column=20, padx=(0,10), pady=10, sticky=W)

    lbl_defense= ttk.Label(from_stats, text = "Defense:")
    lbl_defense.grid(row=30 , column=10, padx=(0,10), pady=10, sticky=E)
    prg_defense= ttk.Progressbar(from_stats , length= 200 , maximum= 255)
    prg_defense.grid(row=30 , column=20, padx=(0,10), pady=10, sticky=W)

    lbl_special_attack= ttk.Label(from_stats, text = "Special Attack:")
    lbl_special_attack.grid(row=40 , column=10, padx=(0,10), pady=10, sticky=E)
    prg_special_attack= ttk.Progressbar(from_stats , length= 200 , maximum= 255)
    prg_special_attack.grid(row=40 , column=20, padx=(0,10), pady=10, sticky=W)

    lbl_special_defense= ttk.Label(from_stats, text = "Special Defense:")
    lbl_special_defense.grid(row=50 , column=10, padx=(0,10), pady=10, sticky=E)
    prg_special_defense= ttk.Progressbar(from_stats , length= 200 , maximum= 255)
    prg_special_defense.grid(row=50 , column=20, padx=(0,10), pady=10, sticky=W)

    lbl_speed= ttk.Label(from_stats, text = "Speed:")
    lbl_speed.grid(row=60 , column=10, padx=(0,10), pady=10, sticky=E)
    prg_speed= ttk.Progressbar(from_stats , length= 200 , maximum= 255)
    prg_speed.grid(row=60 , column=20, padx=(0,10), pady=10, sticky=W)

    root.mainloop()
main()