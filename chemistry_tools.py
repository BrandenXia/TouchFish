from re import compile
import streamlit as st

chemistry_data = {
    "H": ["hydrogen", 1, 1.007],
    "He": ["helium", 2, 4.002],
    "Li": ["lithium", 3, 6.941],
    "Be": ["beryllium", 4, 9.012],
    "B": ["boron", 5, 10.811],
    "C": ["carbon", 6, 12.0107],
    "N": ["nitrogen", 7, 14.006],
    "O": ["oxygen", 8, 15.999],
    "F": ["fluorine", 9, 18.998],
    "Ne": ["neon", 10, 20.179],
    "Na": ["sodium", 11, 22.989],
    "Mg": ["magnesium", 12, 24.305],
    "Al": ["aluminum", 13, 26.981],
    "Si": ["silicon", 14, 28.085],
    "P": ["phosphorus", 15, 30.973],
    "S": ["sulfur", 16, 32.065],
    "Cl": ["chlorine", 17, 35.453],
    "Ar": ["argon", 18, 39.948],
    "K": ["potassium", 19, 39.098],
    "Ca": ["calcium", 20, 40.078],
    "Sc": ["scandium", 21, 44.955],
    "Ti": ["titanium", 22, 47.867],
    "V": ["vanadium", 23, 50.942],
    "Cr": ["chromium", 24, 51.996],
    "Mn": ["manganese", 25, 54.938],
    "Fe": ["iron", 26, 55.845],
    "Co": ["cobalt", 27, 58.933],
    "Ni": ["nickel", 28, 58.693],
    "Cu": ["copper", 29, 63.546],
    "Zn": ["zinc", 30, 65.38],
    "Ga": ["gallium", 31, 69.723],
    "Ge": ["germanium", 32, 72.61],
    "As": ["arsenic", 33, 74.922],
    "Se": ["selenium", 34, 78.971],
    "Br": ["bromine", 35, 79.904],
    "Kr": ["krypton", 36, 83.798],
    "Rb": ["rubidium", 37, 85.468],
    "Sr": ["strontium", 38, 87.62],
    "Y": ["yttrium", 39, 88.906],
    "Zr": ["zirconium", 40, 91.224],
    "Nb": ["niobium", 41, 92.906],
    "Mo": ["molybdenum", 42, 95.95],
    "Tc": ["technetium", 43, 98],
    "Ru": ["ruthenium", 44, 101.07],
    "Rh": ["rhodium", 45, 102.906],
    "Pd": ["palladium", 46, 106.42],
    "Ag": ["silver", 47, 107.868],
    "Cd": ["cadmium", 48, 112.411],
    "In": ["indium", 49, 114.818],
    "Sn": ["tin", 50, 118.71],
    "Sb": ["antimony", 51, 121.76],
    "Te": ["tellurium", 52, 127.6],
    "I": ["iodine", 53, 126.904],
    "Xe": ["xenon", 54, 131.293],
    "Cs": ["cesium", 55, 132.905],
    "Ba": ["barium", 56, 137.327],
    "La": ["lanthanum", 57, 138.905],
    "Ce": ["cerium", 58, 140.116],
    "Pr": ["praseodymium", 59, 140.908],
    "Nd": ["neodymium", 60, 144.242],
    "Pm": ["promethium", 61, 145],
    "Sm": ["samarium", 62, 150.36],
    "Eu": ["europium", 63, 151.964],
    "Gd": ["gadolinium", 64, 157.25],
    "Tb": ["terbium", 65, 158.925],
    "Dy": ["dysprosium", 66, 162.5],
    "Ho": ["holmium", 67, 164.93],
    "Er": ["erbium", 68, 167.259],
    "Tm": ["thulium", 69, 168.934],
    "Yb": ["ytterbium", 70, 173.04],
    "Lu": ["lutetium", 71, 174.967],
    "Hf": ["hafnium", 72, 178.49],
    "Ta": ["tantalum", 73, 180.948],
    "W": ["tungsten", 74, 183.84],
    "Re": ["rhenium", 75, 186.207],
    "Os": ["osmium", 76, 190.23],
    "Ir": ["iridium", 77, 192.217],
    "Pt": ["platinum", 78, 195.084],
    "Au": ["gold", 79, 196.9665],
    "Hg": ["mercury", 80, 200.59],
    "Tl": ["thallium", 81, 204.383],
    "Pb": ["lead", 82, 207.2],
    "Bi": ["bismuth", 83, 208.9804],
    "Po": ["polonium", 84, 209],
    "At": ["astatine", 85, 210],
    "Rn": ["radon", 86, 222],
    "Fr": ["francium", 87, 223],
    "Ra": ["radium", 88, 226],
    "Ac": ["actinium", 89, 227],
    "Th": ["thorium", 90, 232.0381],
    "Pa": ["protactinium", 91, 231.0359],
    "U": ["uranium", 92, 238.0289],
    "Np": ["neptunium", 93, 237],
    "Pu": ["plutonium", 94, 244],
    "Am": ["americium", 95, 243],
    "Cm": ["curium", 96, 247],
    "Bk": ["berkelium", 97, 247],
    "Cf": ["californium", 98, 251],
    "Es": ["einsteinium", 99, 252],
    "Fm": ["fermium", 100, 257],
    "Md": ["mendelevium", 101, 258],
    "No": ["nobelium", 102, 259],
    "Lr": ["lawrencium", 103, 262],
    "Rf": ["rutherfordium", 104, 261],
    "Db": ["dubnium", 105, 262],
    "Sg": ["seaborgium", 106, 266],
    "Bh": ["bohrium", 107, 264],
    "Hs": ["hassium", 108, 277],
    "Mt": ["meitnerium", 109, 268],
    "Ds": ["darmstadtium", 110, 281],
    "Rg": ["roentgenium", 111, 280],
    "Cn": ["copernicium", 112, 285]
}

st.title("Chemistry Tools")
elements_info_search, relative_mass_cal = st.tabs(["Elements Information Searching", "Relative Mass Calculation"])
with elements_info_search:
    line = st.text_input("Enter some symbols of elements")

    elements_symbols = compile(r"[A-Z][a-z]{0,2}")

    all_elements = elements_symbols.findall(line)

    for element in all_elements:
        try:
            information = chemistry_data[element]
            st.text(
                f"""
                Element Name: {information[0]}
                Atomic Number: {information[1]}
                Relative Atomic Mass: {information[2]}
                """
            )
        except KeyError:
            st.text(f"Element {element} does not exit!")
with relative_mass_cal:
    line = st.text_input("Enter a chemical formula")

    atomic_group = compile(r"\(([A-Za-z0-9]+)\)")
    atomic_group_num = compile(r"\([A-Za-z0-9]+\)(\d+)?")
    atomic_group_quoted = compile(r"\([A-Za-z0-9]+\)[\d+]?")
    elements_symbols = compile(r"([A-Z][a-z]{0,2})")
    elements_symbols_num = compile(r"[A-Z][a-z]{0,2}(\d+)?")

    chem_res = atomic_group.findall(line)
    num_res = atomic_group_num.findall(line)
    quoted_atomic_group = atomic_group_quoted.findall(line)

    var = []
    for i in num_res:
        try:
            i = int(i)
        except ValueError:
            i = 1
        var.append(i)
    num_res = var

    full_res = dict(zip(chem_res, num_res))

    excluded_atomic_group = line
    for i in quoted_atomic_group:
        excluded_atomic_group = excluded_atomic_group.replace(i, "")
    print(excluded_atomic_group)

    relative_mass = 0

    for key in full_res:
        element = elements_symbols.findall(key)
        element_num = elements_symbols_num.findall(key)

        var = []
        for i in element_num:
            try:
                i = int(i)
            except ValueError:
                i = 1
            var.append(i)
        element_num = var
        all_elements = dict(zip(element, element_num))

        for i in all_elements:
            relative_mass += chemistry_data[i][2] * all_elements[i]

    element = elements_symbols.findall(excluded_atomic_group)
    element_num = elements_symbols_num.findall(excluded_atomic_group)

    var = []
    for i in element_num:
        try:
            i = int(i)
        except ValueError:
            i = 1
        var.append(i)
    element_num = var
    del var
    all_elements = dict(zip(element, element_num))

    for i in all_elements:
        relative_mass += chemistry_data[i][2] * all_elements[i]
    st.text(f"Relative Mass: {relative_mass}")
