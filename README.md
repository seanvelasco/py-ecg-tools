# Platforms 
# --platform manylinux2014_x86_64 
# --platform manylinux2014_aarch64


pip install \
    --platform manylinux2014_aarch64 \
    --target=python \
    --implementation cp \
    --python 3.9 \
    --only-binary=:all: --upgrade \
    numpy matplotlib lxml

zip -r ./ecg-generation-layer.zip .
