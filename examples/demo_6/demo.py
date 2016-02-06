import sys
owfn_path = "/home/pollo/repos/model_repair/lib"
sys.path.append(owfn_path)

from logger import LOG
from petri_net import PetriNet
from ctl.ctl import GENERAL

model = PetriNet()

""" Adding places, transitions and flow for 'P'"""
model.add_place("p_iddle")
model.add_place("p_active")
model.add_transition("t_1")
model.add_transition("t_2")
model.change_input_flow("p_iddle", "t_1", 1)
model.change_output_flow("p_active", "t_1", 1)
model.change_input_flow("p_active", "t_2", 1)
model.change_output_flow("p_iddle", "t_2", 1)

""" Adding places, transitions and flow for 'P'"""
model.add_place("q_iddle")
model.add_place("q_active")
model.add_transition("t_3")
model.add_transition("t_4")
model.change_input_flow("q_iddle", "t_3", 1)
model.change_output_flow("q_active", "t_3", 1)
model.change_input_flow("q_active", "t_4", 1)
model.change_output_flow("q_iddle", "t_4", 1)

""" Generates a LoLA file """
print model.export_lola({"p_iddle": 1, "q_iddle": 1})
