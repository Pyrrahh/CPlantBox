import plantbox as pb
import visualisation.vtk_plot as vp

plant = pb.Plant()  # Create a new plant 

# Open plant and root parameters from a file
path = "/home/jhack/phd/CPlantBox/modelparameter/structural/plant/"
name = "Zea_mays_4_Leitner_2014" #"fspm2023"
plant.readParameters(path + name + ".xml")  
root = plant.getOrganRandomParameter(pb.root) 
stem = plant.getOrganRandomParameter(pb.stem)  
leaf = plant.getOrganRandomParameter(pb.leaf)  
seed = plant.getOrganRandomParameter(pb.seed)  

print(root[1], stem[1], leaf[1], "\n")  # Print parameters of subType 1 of root, stem, and leaf
print(seed[0], "\n")  # Print the seed parameter

# Change a parameter
root[1].r = 5  # Change elongation rate (r [cm/day]) 
root[1].ln = 0.25  # Change inter-lateral distance (ln [cm])
root[2].dx = 0.5  # Change axial resolution (dx [cm])
root[2].dxMin = 0.1  # Change minimal axial resolution (dxMin [cm])

print(root[1])  # Print new root parameters

plant.initialize()

simtime = 40  # days
plant.simulate(simtime)

# Plot
#vp.plot_plant(plant, "organType")
