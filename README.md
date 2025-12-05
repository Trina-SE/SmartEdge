# SmartEdge
User-friendly automatic Image Sharpening that works without manually adjusting any settings and produces natural-looking results.
- Existing sharpening methods require manual parameter tuning (trial-and-error).
- This method automatically adapts to each image
- Shows practical applications (medical retinal images, aerial photos, etc.)
- Proposes energy-efficient on-chip implementation
# Project Description
Developed an automatic image sharpening filter combining Prewitt gradient and Retinex-inspired contrast measures for edge enhancement. Implemented adaptive parameter estimation eliminating manual tuning requirements. Applied to medical imaging (retinal fundus), low-light photography, and compressed image restoration. Achieved 100% increase in edge visibility with preserved image naturalness (PSNR, SSIM metrics).
# What it does:
Makes blurry or poorly-lit images sharper by enhancing edges, making details more visible.
- Existing sharpening methods require manual parameter tuning (trial-and-error).
- This method automatically adapts to each image
- Shows practical applications (medical retinal images, aerial photos, etc.)
- Proposes energy-efficient on-chip implementation

Main contribution: A new mathematical filter (algorithm) for sharpening
Bonus: A hardware design to implement it on camera chips

# Speciality/Noble points:
- Automatic parameter setting - User doesn't need to think about settings. Uses gradient + Retinex-inspired contrast measure (unique combination)
- Works well on low-light and blurry images
- Less aggressive than standard Laplacian sharpening (more natural results)
- Can be built into camera hardware for real-time processing with very low power
# Tech Stack: 
Python, OpenCV, NumPy, Matplotlib
# Research Paper
https://ieeexplore.ieee.org/document/11192240
