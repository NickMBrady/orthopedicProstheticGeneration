## Algorithmic Generation of a Custom Prosthetic Socket

A custom prosthetic socket can be created using two annotated reference photos of the target appendage. In order for scale to be inferred from the images, four bright green tracking markers must be longitudinally and centrally placed on the appendage, 90 degrees apart (to satisfy the dorsal (top) and radial (side) views), according to the following measurements: 5 cm between them, and 2 cm from the limb termination (see below). If marked correctly, two markers will be visible from the top and two will be visible from the side.

![marking guide](/assets/generation/Screenshot%202024-08-12%20152954.png)

*Take two images of the appendage — a top view and a side view, as shown above — against a white sheet of paper. Then, run the following script, correcting the file path for both input images.*

#### Using algGenPros.py and Blender, follow this tutorial to algorithmically generate a custom insert:
#### https://youtu.be/_WsbkCI7pn4

The code will print four width dimensions, measured at equidistant quarters along the length of the prosthesis, and a height dimension. Download Blender and open the attached Blender file. In the code panel in the center of the screen, replace the list declarations for x_scales, y_scales, and z with the printed values. Click the triangle at the top of the window that contains the code to run the script. Adjustments to the curvature of the socket walls are made with  line 72; adjustments to the curvature of the top of the socket are made in line 61. Adjustments to the thickness of the prosthetic walls are made in line 79. Finally, export an STL of the scaled socket.

A ready-to-print model of the V2 can be downloaded at this link:
https://drive.google.com/file/d/1lVZ05xqshKqhCnZhrd5PjvsZDPWH4sRr/view?usp=drive_link

## 3D Printing and Assembly

Import the model into Cura- a free, open-source slicer by Ultimaker. Ensure that all settings are visible by opening Print settings > Custom, clicking the three lines at the top of the window and selecting All.

Navigate to Print settings > Custom. In Quality, set a layer height of 0.2 mm or lower. In Walls, set Wall Line Count to 0. In Top/Bottom, set Top Layers and Bottom Layers to 0. The balance of strength and capacity for thermal deformation is optimized with a low-percentage infill and very wide lines. In Infill, set Infill Density to around 10%, Infill Pattern to Gyroid, and Infill Line Multiplier approximately 8 (assuming a 0.4 mm nozzle). Trial and error may be necessary depending on the filament and the geometry of the socket.

Printing with PETG is recomended for its moderate glass transition temperature that allows easy forming and structural integrity in warm environments.

The V2 socket is designed for use with the Base Shuttle Lock, 4-Hole Pyramid, and a silicone liner from St&G Corporation.


## Thermal Forming

The socket is formed by relaxing into a state of compression around the residual limb. The forming process is accomplished through two heating stages: Expansion and Forming. During the first stage, the entire socket is heated and a tool is used to expand the diameter of the socket. During the second stage, the socket is placed over the residual limb and a heat gun is used to reheat the expanded socket, contracting it over the residual limb to achieve a custom fit. Once fully formed, the process can be repeated indefinitely as long as heating cycles are not excessive and no extreme deformation is requested of the material.

![compression example](/assets/prosthetic/661c2c9d61ce40d73ae270f4_partially%20formed%20prosthetic%20cross%20sectoin.jpg)
*A cross section of a prosthetic socket, originally circular, demonstrating forming. The cross section was expanded and allowed to cool in the enlarged state (red). Then, one side was reheated, returning the plastic to its original size (blue). This proess is used to form the socket to the residual limb.*

![compression example](/assets/prosthetic/661c2e5eec1547345fcc2ab8_exhaust%20expander.jpg)
*The tool developed for expanding the prosthetic socket, stage one. It consists of a modified exhaust pipe expander with multiple wedges to extend its reach.*



#### Stage One: Expansion
The socket should be heated using an oven or water bath. The oven's temperature should be approximately 70° F higher than the glass transition temperature of the plastic; the heating temperature of the water bath should be approximately 10° F higher than the glass transition temperature. Carefully monitor the plasticity of the device during heating to prevent overheating and annealing of the socket. A tool capable of high-strength radial expansion is inserted into the socket and used to expand its diameter. In our application a modified exhaust pipe expander (pictured above) was used. To enable a greater range of expansion and for even greater strength, a purpose-built tool is ideal.

#### Stage Two: Forming
Once cooled in the expanded position, the socket is placed over the residual limb and silicone liner to be worn with the device. While supporting the socket to maintain its centerization over the limb, a heat gun is used to heat the socket. As the plastic reheats, the socket will return to its former, unexpanded form, softly compressing around the residual limb and taking its form.

Once cooled, the socket is ready for use.