# Construction-Site-Duct-Order-Calculator
SUMMARY
This code produces three .csv files: 
1- The number, size of the standard-length size given the duct width, height and length on the shop drawings.
2- The number, size and length of the nonstandard length size ducts (excess parts from part 1).
3- The fitting between these ducts dimensions given the diminutions of the fittings from the shop drawings (a part to be improved).

INTRODUCTION 
I recently completed my engineering training at CSCEC in the MEP-HVAC department and i notices that to complete an order of ducts
for a floor takes more than 2 weeks of continuous work (sometimes 4 weeks). This seems too long for just one floor and I started this program to cut
this time to minimum.

EXPLAINIGN THE PROGRAM
Every construction site has a shop drawing that contains detailed design of every service in the building and HVAC ducts are one of
these services. These drawings are drawn in a scale (i.e. 1:100 means each millimeter on the drawing is 100 millimeters in reality) and contains details like the cross-section dimension which will determine the kind of joint the duct is using (TDC for large ducts above 12*6 and a slip joint for ducts less than that) and the length of these ducts.
The standard TDC duct’s length is 1130mm while the slip joint is 1200mm. This means that most likely each duct line will have some 
extra pieces that are not of standard length. The standard-length ducts number and size are stored in a .csv file while all the 
extra pieces length and dimension are stored in another file.Ducts relate to different fittings that has dimensions too that will
be stored in a separate csv file too. 
VISION & PARTS TO BE IMPROVED
First, I have started taking python courses only recently and GitHub is completely new to me, I will try to keep improving this
code until I can (somehow) make this code extract all the information it needs from the soft AutoCAD copy on the pc with out need 
for entry by any user.All parts of the code can be improved but some parts are more important that the others.
For example, the fittings are stored separately (every fitting in a separate file); it would be nice to store all fitting in 
one csv file. Many parts of the code are up for improvement.





