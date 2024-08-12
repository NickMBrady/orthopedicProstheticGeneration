#  Moldable Orthopedic Prosthetic Generation
Leveraging a novel thermal workflow, this repo outlines my work on algorithmically generated moldable orthotic and prosthetic solutions that deliver superior functionality and comfort.

Employing the gyroid minimal surface as the principle structural element, the resulting devices are highly moldable, agnostic of axis. Due to the accessible thermal characteristics of popular thermoplastics, healthcare providers and patients are able to form a custom shape that hardens in minutes and can be remolded following subsequent heating. Coupled with elastic plastics such as TPU, cushioned areas complement the rigid molded structure for comfort and control.

![molding demo](/assets/orthotic/orthoticMolding-ezgif.com-speed.gif)



## Updates

### Partnership with 2ft Prosthetics - January 11, 2024 

I am overjoyed to announce the beginning of a partnership with 2ft Prosthetics, a nonprofit organization that serves amputees in underprivileged regions. One of the organization's engineers and I will continue the development of my moldable prosthetic socket and orthotic solutions and evaluate them for practical use.


### Form Prosthetic Socket V2 Developed - February 15, 2024

With my learnings from the original prototype, the new thermal molding workflow, and the invaluable experience of 2ft Prosthetics, I am pleased to announce Form Prosthetic Socket V2. This iteration has improved high-temperature resistance, a modified geometry for superior rigidity, and is natively compatible with hardware and silicone sleeves from ST&G Corporation. This model is currently undergoing a comprehensive evaluation by 2ft Prosthetics.  

### [See All](/updates.md)


<br><br>


# Projects

<br>

## Orthotic Insert

![orthotic insert](/assets/orthotic/64c876a31d0d4d84ddcdcf89_Gyroid-Intersection-49.jpg)


Designed for limb-length discrepancy and asymmetry patients, the moldable insert conforms to support and cushion. A hyper-moldable structure of rigid PLA plastic comprises the majority of the height. A thin layer of flexible TPU is printed on top for elastic cushioning. 

### [Images](/assets/orthotic/)    |   [Documentation](/orthoticGenerationDocumentation.md) | [Project Files](https://www.thingiverse.com/thing:6156919)


<br>

## Prosthetic Socket

![prosthetic socket](/assets/prosthetic/661bedfb88e6101d822d0ab9_socket%20upscaled.jpg)

Targeted as a temporary or low-cost alternative, the prosthetic socket can be formed to precisely accomodate the residual limb.

Traditional polypropelene workflows require involved molding and casting, a costly and time-consuming process. This workflow allows for a socket of approximate fit to be precisely contoured to the patient's limb in minutes and at a fraction of the cost.

### [Images](/assets/prosthetic/)    |   [Documentation](/prostheticGenerationDocumentation.md) 




<br>

## Orthotic Insert and Prosthetic Generative Algorithm

![orthotic insert and prosthetic generative agorithm](/assets/orthotic%20generation/ezgif.com-video-to-gif-converter.gif)

The orthotic and prosthetic generative workflows operate in theree stages: image aquisition, algorithmic processing, and 3D generation. 





### Orthotic Generation

A patient first traces their existing shoe insole on standard, letter paper and takes a picture. The script corrects for distortion and applies morphological operations to vertically align and segment the outline. The outline is measured using scale inferred from the paper and dimensions are passed to Blender, where an insole of specified height is constructed.

### [Images](/assets/generation/) | [Documentation](/orthoticGenerationDocumentation.md)


<br>


### Prosthetic Generation

A patient first longitudinally places green markers of known distance on the appendage: two dorsally, two radially. A dorsal and radial picture is taken, and the two images undergo initial processing separately. The algorithm identifies the markers, then distortion corrects, scales, and vertically aligns the image. Multiple morphological operations are applied to segment and outline the apendage, per axis. The outline is measured using scale inferred from the markers, and dorsal and radial dimensions are passed to Blender at several cross sections. With an additional length criteria specified, a socket of specified curvature and size is constructed.

### [Images](/assets/generation/)  |   [Documentation](/prostheticGenerationDocumentation.md)



