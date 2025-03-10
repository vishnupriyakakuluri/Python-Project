import gdspy
import oasis

# Read GDSII file
gdsii_lib = gdspy.GdsLibrary(infile="xor.gds2")

# Write to OASIS file
oasis_writer = oasis.OasisWriter("output.oas")
oasis_writer.write(gdsii_lib)
oasis_writer.close()