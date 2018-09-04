# Construction-Site-Duct-Order-Calculator
SUMMARY
This code produces three .csv files: 
1- The number and size of the standard-length size; given the duct width, height and length from the shop drawings.
2- The number, size and length of the nonstandard length size ducts (excess parts from part 1).
3- The fittings between these ducts dimensions given the dimensions of the fittings from the shop drawings (a part to be improved).

INTRODUCTION 
I recently completed my engineering training at CSCEC in the MEP-HVAC department and I notices that to complete an order of ducts
for a floor it takes more than 2 weeks of continuous work (sometimes 4 weeks). This seems too long for just one floor. I started this program to cut this time to minimum and put this time to better use.

EXPLAINIGN THE PROGRAM
Every construction site has a shop drawing that contains detailed design of every service in the building and HVAC ducts are one of these services. These drawings are drawn in a scale (i.e. 1:100 means each millimeter on the drawing is 100 millimeters in reality) and contains details like the cross-section dimension which will determine the kind of joint the duct is using (TDC for large ducts above 12*6 inches and a slip joint for ducts less than that) and the length of these ducts.
The standard TDC duct’s length is 1130mm while the slip joint is 1200mm. This means that most likely each duct line will have some extra pieces that aren't of standard length. The standard-length ducts number and size are stored in a .csv file while all the 
extra pieces length and dimension are stored in another file. Ducts are connected to each other with different kinds of fittings that has dimensions too that will be stored in a separate .csv file too. 

VISION & PARTS TO BE IMPROVED
First of all I have started taking python courses only recently on Udemy and GitHub is completely new to me, I will try to keep apllyign what I learn for improving this code until I can (somehow) make this code extract all the information it needs from the soft AutoCAD copy on the PC of the designer with out need for manual entry by any user. All parts of the code can be improved but some parts are more important that the others.
Here are Some suggestions:
-The fittings are stored separately (every fitting in a separate file); it would be nice to store all fitting in one csv file.Done -The programm will crash if the user enters an unregistered commmand.
-Starting a front end with tkinter library for a GUI.
-Converting the whole code into an OOP.


