FROM jupyter/scipy-notebook:latest

# Set working directory inside the container
WORKDIR /home/jovyan/work

# Install additional Python packages
RUN pip install --no-cache-dir \
    pandas \
    numpy \
    matplotlib \
    seaborn \
    scikit-learn \
    pyarrow \
    openpyxl

# Expose Jupyter port
EXPOSE 8888

# Jupyter Lab starts automatically (inherited from base image)
