FROM jupyter/scipy-notebook:x86_64-ubuntu-22.04

# Set working directory inside the container
WORKDIR /home/jovyan/work

# Install additional Python packages
RUN pip install --no-cache-dir \
    matplotlib \
    numpy \
    openpyxl \
    pandas \
    pyarrow \
    scikit-learn \
    seaborn

# Expose Jupyter port
EXPOSE 8888

# Jupyter Lab starts automatically (inherited from base image)
