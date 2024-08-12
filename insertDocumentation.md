## Selecting or Algorithmically Generating a Custom Model



#### An appropriately sized 3D model can be obtained by selecting one of five pre-sized insoles, or using the algorithmic Python and Blender workflow generate an entirely custom insole from patient photos.

## Insoles of Standard Size
Attached in Thingiverse are inserts that support foot lengths from 22.4 - 31.7 cm (A, B, C, D, and E) and an adjustment cube. To select the appropriate length, determine your shoe size in centimeters1 (or measure your foot directly) and refer to the chart below.

```
    Insert A:  22.4 to 23.6 cm 
    Insert B:  23.7 to 25.3 cm
    Insert C:  25.4 to 27.4 cm
    Insert D:  27.5 to 29.5 cm
    Insert E:  29.6 to 31.7 cm
```

## Algorithmically Generated Insole

#### Using algGenOrtho.py and Blender, follow this tutorial to algorithmically generate a custom insert:
#### https://youtu.be/ML5UwX9cQBY

The code will print a length dimension. Download Blender and opoen 'orthoticInsert.blend.' In the code panel in the center of the screen, replace the variable declaration for length with the printed value, and set heightCM to the desired value, in centimeters. Click the triangle at the top of the window that contains the code to run the script. Finally, export an STL of the scaled insole.

## Prepare for 3D Printing

#### Follow this tutorial to prepare the exported 3D model for printing:
#### https://youtu.be/tZOekoVnqHk

To customize insert height and print, import the model into Cura- a free, open-source slicer by Ultimaker. Ensure that all settings are visible by opening Print settings > Custom, clicking the three lines at the top of the window and selecting All.

If you would like to follow the video tutorial, please see below.

The model downloaded is the right-foot insert. If a left insert or both inserts are needed, hold tight -- height adjustments need to come first. With the model selected, use the Rotate and Move tools to "sink" the model into the build plate, ensuring the insert vertex intersects the build plate. The insert remaining above the build plate will be printed. When adjusting the height, keep in mind that some (as much as 1 in, 2 cm) height will be lost during the forming process.
‍
If a left insert is needed, select the insert and use the Mirror tool from the left toolbar. If both inserts are needed, right click the model and Multiply Selected, creating a copy. Then, move the new model to a free area on the build plate and mirror, as described above.

Navigate to Print settings > Custom. In Quality, set the layer heights as low as possible -- 0.1 or 0.05 mm is recommended. In Walls, set Wall Line Count to 0. In Top/Bottom, set Top Layers and Bottom Layers to 0. In Infill, set Infill Density to 5% and Infill Pattern to Gyroid. Finally, set Infill Line Multiplier to 3.

Add the adjustment cube from the downloaded folder. Using the Scale tool on the left bar, set the size to 180x180 and 1 mm tall. On the left bar select Per Model Settings and select Modify settings for overlaps. Click Select settings, and under Infill check Infill Density. Return to the previous window and set Infill Density to approximately 40%.

If using TPU to create a cushioning zone, repeat the steps above but set the cube thickness to 5 mm or greater and Infill Density to about 30% -- the thickness and infill density will depend on your preference and the hardness of your TPU.

If printing with flexible filament, navigate to Extensions > Post Processing > Modify G-code. Click Add a script and select Pause at height. Type the height of your cushioning zone into Pause Height and close the window. When the printer reaches this layer it will automatically pause, allowing a filament switch from TPU to PLA.

Happy experimentation!


## Thermal Forming
Heated water or a hair dryer may be used for forming. Water is recommended as some hairdryers are not powerful enough to heat the entire insert. If using water, monitor the water temperature with a thermometer; 150 - 160º F will work best.
‍A higher temperature allows for more freedom while molding but requires greater care. In the case of returning the insert to its original position, water is preferable.
‍
For best results, forming should be done inside the shoe. If possible, remove the laces such that the tongue can be pulled as far forward as possible. After the insert has heated sufficiently (about 10 seconds in 160º F water), rapidly transfer it to the shoe. The main objective during forming is keeping the insert pressed against the back of the shoe. While applying pressure with your thumbs to keep the insert held back, carefully slide your foot into the shoe without dragging the insole forward. Before standing up, ensure that the insert is fully seated in the back of the shoe. Then, stand up and make your desired alteration as the insert molds under your heel.

The insert can be compressed flat, so ensure that you monitor your foot pressure so as to establish the correct height. For a Limb Length Discrepancy patient, standing on the insert with monitored pressure should suffice in forming. Pronation or more specialized conditions require a conscious forming approach, tilting your foot so to create a form that will counteract the natural posture.

Trial and error is essential; keep in mind, after the insert hardens, it can be re-heated and will naturally return to its original shape.