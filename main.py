import dockerfiles_obfuscation
import subprocess

images_mappings = {
 "python_app": "python:3.10",
 #   "python_distroless": "gcr.io/distroless/python3-debian12:latest",
 #  "python_edited": "jackops93/whoami"

}

produced_images = []
for name,fn in dockerfiles_obfuscation.__dict__.items():
    if not callable(fn):
        continue
    for image_name,image in images_mappings.items():
        with open("./Dockerfile","w+") as fp:
            fp.write(fn(image))
        p = subprocess.Popen(f"docker build -f Dockerfile ./app -t {image_name}_{name} --load".split(" "))
        p.wait(120)
        subprocess.Popen(f"mv ./Dockerfile ./images/{image_name}_{name}.Dockerfile".split(" ")).communicate()    
        produced_images.append(f"{image_name}_{name}")
print(produced_images,sep='\"')