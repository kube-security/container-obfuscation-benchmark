import dockerfiles_obfuscation
import subprocess
import os

images_mappings = {
 "python_app": "python@sha256:d78428228533d961b772473e6c9ec0e1ef8c910034eaa09cf149bc7515d6ed19",

}
tag = os.getenv("TAG")
container_registry = os.getenv("CONTAINER_REGISTRY")
produced_images = []
for name,fn in dockerfiles_obfuscation.__dict__.items():
    if not callable(fn):
        continue
    for image_name,image in images_mappings.items():
        with open("./Dockerfile","w+") as fp:
            fp.write(fn(image))
        subprocess.Popen(f"docker build -f Dockerfile ./app -t {container_registry}/{image_name}_{name}:{tag} --load".split(" ")).wait(120)
        subprocess.Popen(f"docker push {container_registry}/{image_name}_{name}:{tag}".split(" ")).wait(240)
        subprocess.Popen(f"mv ./Dockerfile ./images/{image_name}_{name}.Dockerfile".split(" ")).communicate()    
        produced_images.append(f"{image_name}_{name}")
print(produced_images,sep='\"')